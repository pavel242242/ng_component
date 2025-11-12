# K2 REST API Driver

A Python driver for K2 accounting/ERP software REST API, following the driver design specification v2.0.

## Overview

K2 is a comprehensive enterprise resource planning (ERP) system primarily used in Czech and Slovak markets. This driver provides a clean, Pythonic interface to interact with K2's REST API, enabling integration with external systems, data analytics, and automation workflows.

### What is K2?

K2 organizes data into "evidences" (similar to tables in databases or objects in other systems). Common evidences include:
- **faktura-vydana** - Issued invoices (sales)
- **faktura-prijata** - Received invoices (purchases)
- **adresar** - Address book (customers and vendors)
- **cenik** - Pricelist (products/parts)
- **banka** - Bank accounts

## Features

✅ **Read-only MVP Implementation**
- `list_objects()` - Discover available K2 evidences
- `get_fields(object_name)` - Get field schema for any evidence
- `read(evidence, ...)` - Query data with filtering and pagination

✅ **Production-Ready**
- Automatic retry logic with exponential backoff
- Connection validation on initialization
- Comprehensive error handling
- Debug logging support
- Context manager support

✅ **Well-Documented**
- Detailed docstrings with examples
- Type hints throughout
- Clear error messages with suggestions

## Installation

### Prerequisites

- Python 3.8 or higher
- K2 server with REST API enabled
- Valid K2 credentials (username and password)

### Install Dependencies

```bash
pip install requests python-dotenv
```

### Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your K2 credentials:
```env
K2_API_URL=http://your-k2-server.com/restservice
K2_USERNAME=your_username
K2_PASSWORD=your_password
K2_COMPANY_ID=your_company_id
```

## Quick Start

### Basic Usage

```python
from k2_driver import K2Client

# Initialize client
client = K2Client(
    api_url="http://localhost:8000",
    username="demo",
    password="demo",
    company_id="demo"
)

# List available evidences
evidences = client.list_objects()
print(evidences)  # ['faktura-vydana', 'adresar', 'cenik', ...]

# Get field schema
fields = client.get_fields("faktura-vydana")
print(fields['kod'])  # {'name': 'kod', 'type': 'string', ...}

# Query data
invoices = client.read(
    evidence="faktura-vydana",
    conditions="stav=Nezaplaceno",
    fields="id,kod,nazev,castka"
)

client.close()
```

### Using Context Manager (Recommended)

```python
from k2_driver import K2Client

with K2Client(api_url, username, password, company_id) as client:
    # List evidences
    evidences = client.list_objects()

    # Get fields
    fields = client.get_fields("adresar")

    # Query data
    customers = client.read(
        evidence="adresar",
        conditions="stav=Active"
    )
```

## API Reference

### K2Client

Main client class for interacting with K2 REST API.

#### `__init__(api_url, username, password, company_id, timeout=30, max_retries=3, debug=False)`

Initialize K2 API client.

**Parameters:**
- `api_url` (str): Base URL of K2 REST API
- `username` (str): K2 username for authentication
- `password` (str): K2 password for authentication
- `company_id` (str): Company identifier in K2 system
- `timeout` (int): Request timeout in seconds (default: 30)
- `max_retries` (int): Maximum number of retries (default: 3)
- `debug` (bool): Enable debug logging (default: False)

**Raises:**
- `AuthenticationError`: If credentials are invalid
- `ConnectionError`: If unable to connect to API

**Example:**
```python
client = K2Client(
    api_url="http://localhost:8000",
    username="user",
    password="pass",
    company_id="demo",
    debug=True
)
```

---

#### `list_objects() -> List[str]`

List all available K2 evidence types (objects).

**Returns:**
- List of evidence names

**Raises:**
- `AuthenticationError`: If authentication fails
- `ConnectionError`: If connection fails

**Example:**
```python
evidences = client.list_objects()
print(evidences)
# Output: ['faktura-vydana', 'faktura-prijata', 'adresar', 'cenik', 'banka']
```

---

#### `get_fields(object_name) -> Dict[str, Any]`

Get field schema for a K2 evidence (object).

**Parameters:**
- `object_name` (str): Name of the evidence

**Returns:**
- Dictionary mapping field names to their properties

**Raises:**
- `ObjectNotFoundError`: If evidence is not found
- `AuthenticationError`: If authentication fails
- `ConnectionError`: If connection fails

**Example:**
```python
fields = client.get_fields("faktura-vydana")
print(fields['kod'])
# Output: {
#     'name': 'kod',
#     'type': 'string',
#     'label': 'Kod',
#     'isRequired': True,
#     'isReadOnly': False,
#     'length': 255
# }
```

---

#### `read(evidence, fields=None, conditions=None, limit=None, offset=None) -> List[Dict[str, Any]]`

Query K2 evidence data.

**Parameters:**
- `evidence` (str): Evidence name
- `fields` (str, optional): Comma-separated list of fields to return
- `conditions` (str, optional): Filter conditions in K2 format
- `limit` (int, optional): Maximum number of records to return
- `offset` (int, optional): Number of records to skip for pagination

**Returns:**
- List of records as dictionaries

**Raises:**
- `ObjectNotFoundError`: If evidence is not found
- `QueryError`: If query execution fails
- `AuthenticationError`: If authentication fails
- `ConnectionError`: If connection fails

**Example:**
```python
# Get all records
records = client.read("adresar")

# Get specific fields
records = client.read("adresar", fields="kod,nazev,email")

# Filter by condition
records = client.read(
    evidence="faktura-vydana",
    conditions="stav=Nezaplaceno"
)

# Pagination
records = client.read(
    evidence="adresar",
    limit=10,
    offset=0
)
```

---

#### `get_object_count(evidence, conditions=None) -> int`

Get the count of records in an evidence.

**Parameters:**
- `evidence` (str): Evidence name
- `conditions` (str, optional): Filter conditions

**Returns:**
- Number of records

**Example:**
```python
# Total customers
count = client.get_object_count("adresar")

# Active customers only
count = client.get_object_count("adresar", conditions="stav=Active")
```

---

#### `close()`

Close the client session and release resources.

**Example:**
```python
client = K2Client(api_url, username, password, company_id)
try:
    data = client.read("adresar")
finally:
    client.close()
```

## K2 Query Syntax (Conditions Parameter)

The `conditions` parameter in the `read()` method supports K2's filtering syntax:

### Basic Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `=` | `stav=Active` | Equality |
| `>` | `castka>1000` | Greater than |
| `<` | `datum<2024-11-01` | Less than |
| `>=` | `castka>=1000` | Greater than or equal |
| `<=` | `datum<=2024-12-31` | Less than or equal |

### Logical Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `AND` | `stav=Active AND castka>1000` | Both conditions must be true |
| `OR` | `stav=Paid OR stav=Cancelled` | Either condition must be true |

### Examples

```python
# Single condition
client.read("adresar", conditions="stav=Active")

# Multiple conditions with AND
client.read(
    "faktura-vydana",
    conditions="stav=Nezaplaceno AND castka>5000"
)

# Multiple conditions with OR
client.read(
    "faktura-vydana",
    conditions="stav=Paid OR stav=Cancelled"
)

# Date comparison
client.read(
    "faktura-vydana",
    conditions="datum>=2024-01-01 AND datum<=2024-12-31"
)
```

## Common Use Cases

### 1. E-commerce Integration

Sync products and create invoices automatically:

```python
with K2Client(api_url, username, password, company_id) as client:
    # Get products for e-shop
    products = client.read(
        evidence="cenik",
        fields="kod,nazev,cena,sklad",
        conditions="stav=Active"
    )

    # Query unpaid invoices to check payment status
    unpaid = client.read(
        evidence="faktura-vydana",
        conditions="stav=Nezaplaceno"
    )
```

### 2. Financial Reporting

Generate reports and analytics:

```python
with K2Client(api_url, username, password, company_id) as client:
    # Get all invoices for the month
    invoices = client.read(
        evidence="faktura-vydana",
        conditions="datum>=2024-11-01 AND datum<=2024-11-30"
    )

    # Calculate totals
    total = sum(float(inv.get('castka', 0)) for inv in invoices)
    print(f"Total revenue: {total}")
```

### 3. Customer Management

Sync customer data with CRM:

```python
with K2Client(api_url, username, password, company_id) as client:
    # Get active customers
    customers = client.read(
        evidence="adresar",
        fields="kod,nazev,email,telefon,mesto",
        conditions="stav=Active"
    )

    # Export to CRM
    for customer in customers:
        # sync_to_crm(customer)
        pass
```

### 4. Data Analytics

Extract data for Business Intelligence tools:

```python
import pandas as pd

with K2Client(api_url, username, password, company_id) as client:
    # Get invoice data
    invoices = client.read(
        evidence="faktura-vydana",
        fields="datum,castka,firma,stav"
    )

    # Convert to DataFrame
    df = pd.DataFrame(invoices)

    # Analyze
    print(df.groupby('stav')['castka'].sum())
```

## Error Handling

The driver provides specific exception classes for different error scenarios:

```python
from k2_driver import (
    K2Client,
    AuthenticationError,
    ConnectionError,
    ObjectNotFoundError,
    QueryError
)

try:
    client = K2Client(api_url, username, password, company_id)
    data = client.read("non-existent-evidence")

except AuthenticationError as e:
    print(f"Authentication failed: {e}")
    # Check credentials

except ConnectionError as e:
    print(f"Connection failed: {e}")
    # Check API URL and network

except ObjectNotFoundError as e:
    print(f"Evidence not found: {e}")
    # Error message includes suggestions

except QueryError as e:
    print(f"Query failed: {e}")
    # Check query syntax

finally:
    client.close()
```

## Examples

The `examples/` directory contains working examples:

- `list_evidences.py` - List all available evidences
- `get_invoice_fields.py` - Get field schema for invoices
- `query_unpaid_invoices.py` - Query unpaid invoices
- `query_active_customers.py` - Query active customers
- `discover_evidence.py` - Full discovery workflow

### Running Examples

```bash
# Set up environment
cp .env.example .env
# Edit .env with your credentials

# Run examples
python examples/list_evidences.py
python examples/query_unpaid_invoices.py
```

## Testing

### Test Connection

```bash
python test_connection.py
```

Or with custom credentials:

```bash
python test_connection.py http://localhost:8000 demo demo demo
```

### Using Mock API

Start the mock K2 API server for testing:

```bash
cd ../mock_k2_api
python main.py
```

Then run the driver against the mock API:

```bash
# In another terminal
export K2_API_URL=http://localhost:8000
python examples/list_evidences.py
```

## Troubleshooting

### Authentication Errors

**Problem**: `AuthenticationError: Authentication failed`

**Solutions**:
- Verify username and password are correct
- Ensure user has API access permissions in K2
- Check that the account is active

### Connection Errors

**Problem**: `ConnectionError: Failed to connect to K2 API`

**Solutions**:
- Verify API URL is correct (include `/restservice` path)
- Check network connectivity to K2 server
- Ensure K2 server and API are running
- Check firewall rules

### Object Not Found

**Problem**: `ObjectNotFoundError: Evidence 'xyz' not found`

**Solutions**:
- Check evidence name spelling (case-sensitive)
- Use `list_objects()` to see available evidences
- Error message includes suggestions for similar names

### Query Errors

**Problem**: `QueryError: Query execution failed`

**Solutions**:
- Check conditions syntax
- Verify field names exist using `get_fields()`
- Ensure data types match (e.g., numbers without quotes)

## Limitations (MVP)

This is a **read-only MVP** implementation. The following features are not yet implemented:

- ❌ Write operations (`create`, `update`, `delete`)
- ❌ Formation service (scripts and reports)
- ❌ Batch operations
- ❌ Transactions
- ❌ Advanced filtering (IN, LIKE, etc.)
- ❌ Field-level validation

For production use, consider implementing these features based on your requirements.

## Driver Capabilities

This driver conforms to the Driver Design Specification v2.0:

**Discovery Methods** (✅ Implemented):
- `list_objects()` - Enumerate available evidences
- `get_fields(object_name)` - Return field schemas

**Read Operations** (✅ Implemented):
- `read(evidence, ...)` - Execute queries with filtering and pagination

**Write Operations** (❌ Not Implemented):
- Create, update, delete operations

**Capabilities**:
- Pagination: `OFFSET` style (PageNumber/PageSize)
- Query Language: K2 Conditions syntax
- Authentication: Basic (username/password)
- Retry Logic: Exponential backoff
- Rate Limiting: Automatic retry with backoff

## Contributing

This driver is part of the `ng_component` project. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test against mock API
5. Submit a pull request

## License

MIT License - See repository root for details.

## Resources

- [K2 Official Website](https://www.k2.cz/)
- [K2 API Documentation](https://help.k2.cz/)
- [Driver Design Specification v2.0](../../docs/driver_design_v2.md)
- [ng_component Repository](https://github.com/padak/ng_component)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the examples
3. Open an issue in the ng_component repository

---

**Version**: 1.0.0
**Last Updated**: November 2024
**Status**: MVP (Read-Only)
