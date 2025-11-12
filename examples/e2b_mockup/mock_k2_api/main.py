"""FastAPI application simulating K2 REST API."""

import re
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import base64

from models import (
    EvidenceBasic,
    EvidenceListResponse,
    FieldProperty,
    EvidenceProperties,
    PagedListResponse,
    QueryResult,
    ErrorResponse,
    HealthResponse,
)
from db import get_db, close_db, EVIDENCE_TABLE_MAP


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events."""
    # Startup
    yield
    # Shutdown
    close_db()


app = FastAPI(
    title="K2 REST API Mock",
    description="Mock K2 REST API backed by DuckDB",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Type mapping from DuckDB to K2
DUCKDB_TO_K2_TYPE = {
    "VARCHAR": "string",
    "INTEGER": "int",
    "BIGINT": "long",
    "DOUBLE": "double",
    "DECIMAL": "decimal",
    "DATE": "date",
    "TIMESTAMP": "datetime",
    "BOOLEAN": "boolean",
    "TEXT": "text",
}


def map_duckdb_type_to_k2(duckdb_type: str) -> str:
    """Map DuckDB type to K2 field type."""
    # Extract base type (e.g., "VARCHAR" from "VARCHAR(255)")
    base_type = duckdb_type.split("(")[0].upper()
    return DUCKDB_TO_K2_TYPE.get(base_type, "string")


def get_field_property(col_name: str, col_type: str, nullable: bool) -> FieldProperty:
    """Create a FieldProperty from DuckDB column info."""
    k2_type = map_duckdb_type_to_k2(col_type)

    # Extract length for VARCHAR fields
    length = None
    if "VARCHAR" in col_type.upper() and "(" in col_type:
        try:
            length = int(col_type.split("(")[1].split(")")[0])
        except:
            pass

    return FieldProperty(
        name=col_name,
        type=k2_type,
        label=col_name.replace("_", " ").title(),
        length=length,
        isRequired=not nullable and col_name.lower() != "id",
        isReadOnly=col_name.lower() == "id",
    )


def check_auth(request: Request) -> bool:
    """Check Basic authentication (simple mock)."""
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return False

    try:
        # Parse "Basic base64(username:password)"
        auth_type, credentials = auth_header.split(" ", 1)
        if auth_type.lower() != "basic":
            return False

        decoded = base64.b64decode(credentials).decode("utf-8")
        username, password = decoded.split(":", 1)

        # Simple mock authentication (accept any non-empty credentials)
        return bool(username and password)
    except:
        return False


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "K2 REST API Mock Server",
        "version": "1.0.0",
        "endpoints": [
            "/c/{company}/evidence-list",
            "/c/{company}/{evidence}/properties",
            "/Data/{evidence}",
            "/Formation/{folder}/{name}/{ext}",
        ]
    }


@app.get("/c/{company}/evidence-list", response_model=EvidenceListResponse)
async def list_evidences(company: str, request: Request):
    """
    List all available K2 evidence types.

    Args:
        company: Company identifier

    Returns:
        List of available evidences (objects) in the K2 system.
    """
    if not check_auth(request):
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    db = get_db()
    tables = db.list_tables()

    evidences = []
    for table in tables:
        evidence_name = db.get_evidence_name(table)
        if evidence_name:
            evidences.append(
                EvidenceBasic(
                    evidence=evidence_name,
                    evidencePath=f"c/{company}/{evidence_name}",
                    url=f"/c/{company}/{evidence_name}",
                )
            )

    return EvidenceListResponse(evidences=evidences)


@app.get("/c/{company}/{evidence}/properties", response_model=EvidenceProperties)
async def get_evidence_properties(company: str, evidence: str, request: Request):
    """
    Get field schema for a K2 evidence type.

    Args:
        company: Company identifier
        evidence: Evidence name (e.g., 'faktura-vydana', 'adresar')

    Returns:
        Detailed metadata including all fields and their types.
    """
    if not check_auth(request):
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    db = get_db()
    table_name = db.get_table_name(evidence)

    if not table_name:
        raise HTTPException(
            status_code=404,
            detail=f"Evidence '{evidence}' not found"
        )

    try:
        schema = db.get_table_schema(table_name)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve schema: {str(e)}"
        )

    properties = [
        get_field_property(col["name"], col["type"], col["null"])
        for col in schema
    ]

    return EvidenceProperties(
        evidence=evidence,
        evidencePath=f"c/{company}/{evidence}",
        properties=properties,
    )


@app.get("/Data/{evidence}")
async def query_evidence(
    evidence: str,
    request: Request,
    Fields: Optional[str] = Query(None, description="Comma-separated field list"),
    Conditions: Optional[str] = Query(None, description="Filter conditions"),
    PageNumber: Optional[int] = Query(1, description="Page number"),
    PageSize: Optional[int] = Query(100, description="Records per page"),
):
    """
    Query K2 evidence data.

    Args:
        evidence: Evidence name (e.g., 'faktura-vydana', 'adresar')
        Fields: Comma-separated list of fields to return
        Conditions: Filter conditions (e.g., "stav=Active")
        PageNumber: Page number for pagination
        PageSize: Number of records per page

    Returns:
        Paged list of records.

    Examples:
        - /Data/faktura-vydana
        - /Data/faktura-vydana?Fields=id,kod,nazev,castka
        - /Data/faktura-vydana?Conditions=stav=Nezaplaceno
        - /Data/adresar?Conditions=stav=Active&Fields=kod,nazev,email
    """
    if not check_auth(request):
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    db = get_db()
    table_name = db.get_table_name(evidence)

    if not table_name:
        raise HTTPException(
            status_code=404,
            detail=f"Evidence '{evidence}' not found"
        )

    try:
        # Build SQL query
        select_fields = "*"
        if Fields:
            select_fields = Fields.replace(",", ", ")

        sql = f"SELECT {select_fields} FROM {table_name}"

        # Add WHERE clause if conditions provided
        if Conditions:
            # Simple condition parsing (e.g., "stav=Active" or "castka>1000")
            where_clause = Conditions.replace("=", "='").replace(" AND ", "' AND ").replace(" OR ", "' OR ")
            if not where_clause.endswith("'"):
                where_clause += "'"
            sql += f" WHERE {where_clause}"

        # Add pagination
        offset = (PageNumber - 1) * PageSize
        sql += f" LIMIT {PageSize} OFFSET {offset}"

        # Execute query
        records = db.execute_query(sql)

        # Get total count for pagination
        count_sql = f"SELECT COUNT(*) as count FROM {table_name}"
        if Conditions:
            count_sql += f" WHERE {where_clause}"
        total_count = db.execute_query(count_sql)[0]["count"]

        # Calculate pagination URLs
        base_url = str(request.url).split("?")[0]
        total_pages = (total_count + PageSize - 1) // PageSize

        first_url = f"{base_url}?PageNumber=1&PageSize={PageSize}"
        last_url = f"{base_url}?PageNumber={total_pages}&PageSize={PageSize}"
        next_url = f"{base_url}?PageNumber={PageNumber + 1}&PageSize={PageSize}" if PageNumber < total_pages else None
        prev_url = f"{base_url}?PageNumber={PageNumber - 1}&PageSize={PageSize}" if PageNumber > 1 else None

        # Add query parameters to URLs
        if Fields:
            for url_var in [first_url, last_url, next_url, prev_url]:
                if url_var:
                    url_var += f"&Fields={Fields}"
        if Conditions:
            for url_var in [first_url, last_url, next_url, prev_url]:
                if url_var:
                    url_var += f"&Conditions={Conditions}"

        response = {
            "PagedList": {
                "Items": records,
                "FirstPageURL": first_url,
                "NextPageURL": next_url,
                "PrevPageURL": prev_url,
                "LastPageURL": last_url,
            }
        }

        return JSONResponse(content=response)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Query execution failed: {str(e)}"
        )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    try:
        db = get_db()
        tables = db.list_tables()
        return HealthResponse(
            status="healthy",
            database=db.db_path,
            tables_count=len(tables),
        )
    except Exception as e:
        return HealthResponse(
            status="unhealthy",
            error=str(e)
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
