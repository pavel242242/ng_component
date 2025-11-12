# Mock K2 REST API

A FastAPI-based mock implementation of the K2 (Czech ERP/accounting software) REST API for testing and development purposes.

## Features

- **Evidence List**: Get available K2 evidence types (objects)
- **Field Schema**: Retrieve field definitions for each evidence
- **Data Queries**: Query evidence data with filtering and pagination
- **Authentication**: Basic HTTP authentication
- **Test Data**: Pre-populated DuckDB database with sample K2 data

## Available Evidences

- `faktura-vydana` - Issued invoices
- `faktura-prijata` - Received invoices
- `adresar` - Address book (customers/vendors)
- `cenik` - Pricelist (products/parts)
- `banka` - Bank accounts

## Running the Server

### Start the server:

```bash
./run.sh
```

Or manually:

```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### Root
```
GET /
```
Returns API information and available endpoints.

### List Evidences
```
GET /c/{company}/evidence-list
```
Returns list of available evidence types.

### Get Evidence Properties
```
GET /c/{company}/{evidence}/properties
```
Returns field schema for specified evidence.

### Query Evidence Data
```
GET /Data/{evidence}?Fields={fields}&Conditions={conditions}&PageNumber={page}&PageSize={size}
```
Query evidence data with filtering and pagination.

## Authentication

The mock API uses Basic authentication. For testing, any non-empty username and password will work.

Example:
```bash
curl -u demo:demo http://localhost:8000/c/demo/evidence-list
```

## Example Requests

### List available evidences
```bash
curl -u demo:demo http://localhost:8000/c/demo/evidence-list
```

### Get invoice fields
```bash
curl -u demo:demo http://localhost:8000/c/demo/faktura-vydana/properties
```

### Query unpaid invoices
```bash
curl -u demo:demo "http://localhost:8000/Data/faktura-vydana?Conditions=stav=Nezaplaceno&Fields=id,kod,nazev,castka"
```

### Query active customers
```bash
curl -u demo:demo "http://localhost:8000/Data/adresar?Conditions=stav=Active&Fields=kod,nazev,email"
```

## Test Data

The mock API creates a DuckDB database with sample data:

- **4 issued invoices** (some paid, some unpaid)
- **4 addresses** (3 customers, 1 vendor)
- **4 products** in pricelist
- **2 bank accounts**

## Health Check

```bash
curl http://localhost:8000/health
```

## Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
