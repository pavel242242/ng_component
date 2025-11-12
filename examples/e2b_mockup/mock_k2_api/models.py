"""Pydantic models for K2 REST API responses."""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class EvidenceBasic(BaseModel):
    """Basic evidence (object) information."""
    evidence: str = Field(..., description="Evidence name (e.g., 'faktura-vydana', 'adresar')")
    evidencePath: str = Field(..., description="API path for evidence")
    url: str = Field(..., description="Full URL to evidence")


class EvidenceListResponse(BaseModel):
    """Response from evidence list endpoint."""
    evidences: List[EvidenceBasic] = Field(default_factory=list)


class FieldProperty(BaseModel):
    """Field property definition."""
    name: str = Field(..., description="Field name")
    type: str = Field(..., description="Data type (string, int, decimal, date, boolean)")
    label: str = Field(..., description="Human-readable label")
    isRequired: bool = Field(default=False, description="Whether field is required")
    isReadOnly: bool = Field(default=False, description="Whether field is read-only")
    length: Optional[int] = Field(None, description="Maximum length for string fields")
    defaultValue: Optional[Any] = Field(None, description="Default value")


class EvidenceProperties(BaseModel):
    """Evidence (object) properties/schema."""
    evidence: str = Field(..., description="Evidence name")
    evidencePath: str = Field(..., description="API path")
    properties: List[FieldProperty] = Field(default_factory=list, description="Field definitions")


class PagedListResponse(BaseModel):
    """Paged list response for data queries."""
    PagedList: Dict[str, Any] = Field(..., description="Paged list container")


class QueryResult(BaseModel):
    """Query execution result."""
    totalSize: int = Field(..., description="Total number of records")
    records: List[Dict[str, Any]] = Field(default_factory=list, description="Result records")


class ErrorResponse(BaseModel):
    """Error response."""
    Error: Dict[str, str] = Field(..., description="Error details")


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    database: Optional[str] = None
    tables_count: Optional[int] = None
    error: Optional[str] = None
