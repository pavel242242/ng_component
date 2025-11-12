"""DuckDB connection and query helpers for K2 API."""

import duckdb
import os
from typing import List, Dict, Any, Optional
from pathlib import Path


# Map K2 evidence names to DuckDB table names
EVIDENCE_TABLE_MAP = {
    "faktura-vydana": "invoices_issued",  # Issued invoices
    "faktura-prijata": "invoices_received",  # Received invoices
    "adresar": "addresses",  # Address book (customers/vendors)
    "cenik": "pricelist",  # Products/Parts
    "banka": "bank_accounts",  # Bank accounts
    "interni-doklad": "internal_documents",  # Internal documents
}

# Reverse mapping
TABLE_EVIDENCE_MAP = {v: k for k, v in EVIDENCE_TABLE_MAP.items()}


class K2DBConnection:
    """Manages DuckDB connection and queries for K2 mock API."""

    def __init__(self, db_path: Optional[str] = None):
        """Initialize connection to DuckDB."""
        if db_path is None:
            # Default path relative to this file
            current_dir = Path(__file__).parent
            db_path = str(current_dir.parent / "test_data" / "k2.duckdb")

        self.db_path = db_path
        self._conn = None

    @property
    def conn(self):
        """Get or create database connection."""
        if self._conn is None:
            if not os.path.exists(self.db_path):
                # Create database if it doesn't exist
                self._create_test_database()
            self._conn = duckdb.connect(self.db_path)
        return self._conn

    def _create_test_database(self):
        """Create test database with sample K2 data."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = duckdb.connect(self.db_path)

        # Create invoices_issued table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS invoices_issued (
                id VARCHAR PRIMARY KEY,
                kod VARCHAR,
                nazev VARCHAR,
                datum DATE,
                castka DECIMAL(15, 2),
                firma VARCHAR,
                stav VARCHAR,
                splatnost DATE,
                poznamka VARCHAR
            )
        """)

        # Insert sample data
        conn.execute("""
            INSERT INTO invoices_issued VALUES
            ('1', 'INV001', 'Faktúra za služby', '2024-11-01', 15000.00, 'CUST001', 'Nezaplaceno', '2024-12-01', 'Služby za október'),
            ('2', 'INV002', 'Faktúra za tovar', '2024-11-05', 8500.50, 'CUST002', 'Zaplaceno', '2024-12-05', NULL),
            ('3', 'INV003', 'Faktúra za konzultace', '2024-11-10', 22000.00, 'CUST001', 'Nezaplaceno', '2024-12-10', 'Poradenství'),
            ('4', 'INV004', 'Faktúra za software', '2024-11-12', 45000.00, 'CUST003', 'Nezaplaceno', '2024-12-12', NULL)
        """)

        # Create addresses table (customers/vendors)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS addresses (
                id VARCHAR PRIMARY KEY,
                kod VARCHAR,
                nazev VARCHAR,
                email VARCHAR,
                telefon VARCHAR,
                ic VARCHAR,
                dic VARCHAR,
                adresa VARCHAR,
                mesto VARCHAR,
                psc VARCHAR,
                stav VARCHAR
            )
        """)

        conn.execute("""
            INSERT INTO addresses VALUES
            ('1', 'CUST001', 'ABC Corporation s.r.o.', 'contact@abc.com', '420555123456', '12345678', 'CZ12345678', 'Hlavní 123', 'Praha', '11000', 'Active'),
            ('2', 'CUST002', 'XYZ Ltd', 'info@xyz.com', '420555234567', '23456789', 'CZ23456789', 'Nová 456', 'Brno', '60200', 'Active'),
            ('3', 'CUST003', 'Tech Solutions a.s.', 'hello@tech.com', '420555345678', '34567890', 'CZ34567890', 'Vysoká 789', 'Ostrava', '70200', 'Active'),
            ('4', 'VEND001', 'Supplier One s.r.o.', 'sales@supplier1.com', '420555456789', '45678901', 'CZ45678901', 'Průmyslová 12', 'Plzeň', '30100', 'Active')
        """)

        # Create pricelist table (products/parts)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS pricelist (
                id VARCHAR PRIMARY KEY,
                kod VARCHAR,
                nazev VARCHAR,
                popis VARCHAR,
                cena DECIMAL(15, 2),
                cenaSDph DECIMAL(15, 2),
                mj VARCHAR,
                sklad INTEGER,
                stav VARCHAR
            )
        """)

        conn.execute("""
            INSERT INTO pricelist VALUES
            ('1', 'PROD001', 'Software licence', 'Roční licence pro software', 12000.00, 14520.00, 'ks', 50, 'Active'),
            ('2', 'PROD002', 'Konzultační hodina', 'Odborné poradenství', 1500.00, 1815.00, 'hod', 999, 'Active'),
            ('3', 'PROD003', 'Notebook', 'Pracovní notebook', 25000.00, 30250.00, 'ks', 15, 'Active'),
            ('4', 'PROD004', 'Školení', 'Celodenní školení', 8000.00, 9680.00, 'den', 100, 'Active')
        """)

        # Create bank_accounts table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS bank_accounts (
                id VARCHAR PRIMARY KEY,
                kod VARCHAR,
                nazev VARCHAR,
                cislo_uctu VARCHAR,
                banka VARCHAR,
                stav VARCHAR
            )
        """)

        conn.execute("""
            INSERT INTO bank_accounts VALUES
            ('1', 'BA001', 'Hlavní účet', '123456789/0100', 'Komerční banka', 'Active'),
            ('2', 'BA002', 'EUR účet', '987654321/0300', 'ČSOB', 'Active')
        """)

        conn.commit()
        conn.close()

    def close(self):
        """Close the database connection."""
        if self._conn:
            self._conn.close()
            self._conn = None

    def get_table_name(self, evidence: str) -> Optional[str]:
        """Convert K2 evidence name to DuckDB table name."""
        return EVIDENCE_TABLE_MAP.get(evidence)

    def get_evidence_name(self, table: str) -> Optional[str]:
        """Convert DuckDB table name to K2 evidence name."""
        return TABLE_EVIDENCE_MAP.get(table)

    def list_tables(self) -> List[str]:
        """List all tables in the database."""
        result = self.conn.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='main'"
        ).fetchall()
        return [row[0] for row in result]

    def get_table_schema(self, table_name: str) -> List[Dict[str, Any]]:
        """Get schema information for a table."""
        result = self.conn.execute(
            f"DESCRIBE {table_name}"
        ).fetchall()

        columns = []
        for row in result:
            columns.append({
                "name": row[0],
                "type": row[1],
                "null": row[2] == "YES",
                "key": row[3] if len(row) > 3 else None,
                "default": row[4] if len(row) > 4 else None,
            })
        return columns

    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Execute a SQL query and return results as list of dicts."""
        try:
            result = self.conn.execute(query)
            columns = [desc[0] for desc in result.description]
            rows = result.fetchall()

            # Convert rows to dicts, handling date serialization
            records = []
            for row in rows:
                record = {}
                for col, val in zip(columns, row):
                    # Convert date objects to strings for JSON serialization
                    if hasattr(val, 'isoformat'):
                        val = val.isoformat()
                    record[col] = val
                records.append(record)

            return records
        except Exception as e:
            raise ValueError(f"Query execution failed: {str(e)}")

    def get_record_count(self, table_name: str) -> int:
        """Get total record count for a table."""
        result = self.conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
        return result[0] if result else 0


# Global connection instance
_db = None


def get_db() -> K2DBConnection:
    """Get the global database connection."""
    global _db
    if _db is None:
        _db = K2DBConnection()
    return _db


def close_db():
    """Close the global database connection."""
    global _db
    if _db:
        _db.close()
        _db = None
