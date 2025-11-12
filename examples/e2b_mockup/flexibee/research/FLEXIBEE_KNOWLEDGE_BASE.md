# FlexiBee API Knowledge Base

**Cloud-based accounting and business management system with comprehensive REST API**

---

## Table of Contents

1. [Overview](#overview)
2. [Information Sources](#information-sources)
   - [Official Documentation](#official-documentation)
   - [GitHub Integrations & Libraries](#github-integrations--libraries)
   - [Case Studies](#case-studies)
   - [Integration Platforms](#integration-platforms)
   - [Community Resources](#community-resources)
3. [API Fundamentals](#api-fundamentals)
   - [Authentication](#authentication)
   - [Base URL Structure](#base-url-structure)
   - [Data Formats](#data-formats)
   - [Demo Server Access](#demo-server-access)
   - [Rate Limits](#rate-limits)
4. [Core Concepts](#core-concepts)
   - [Evidence Types](#evidence-types)
   - [Record Identifiers](#record-identifiers)
   - [Primary Entities](#primary-entities)
5. [Getting Data from FlexiBee](#getting-data-from-flexibee)
   - [Reading Data (GET)](#reading-data-get)
   - [Creating Data (POST/PUT)](#creating-data-postput)
   - [Updating Data (PUT)](#updating-data-put)
   - [Deleting Data (DELETE)](#deleting-data-delete)
   - [Filtering and Querying](#filtering-and-querying)
   - [Pagination and Sorting](#pagination-and-sorting)
   - [Field Selection](#field-selection)
6. [Real-World Examples](#real-world-examples)
   - [E-Commerce Integration](#e-commerce-integration)
   - [Invoice Automation](#invoice-automation)
   - [Inventory Synchronization](#inventory-synchronization)
   - [Payment Processing](#payment-processing)
   - [Multi-System ERP Integration](#multi-system-erp-integration)
7. [User Personas & Common Questions](#user-personas--common-questions)
   - [CFO / Finance Manager](#cfo--finance-manager)
   - [Sales Manager](#sales-manager)
   - [Operations Manager](#operations-manager)
   - [E-Commerce Manager](#e-commerce-manager)
   - [Accountant / Bookkeeper](#accountant--bookkeeper)
   - [Business Owner / Entrepreneur](#business-owner--entrepreneur)
8. [Integration Patterns](#integration-patterns)
   - [Direct API Integration](#direct-api-integration)
   - [Event-Driven with Webhooks](#event-driven-with-webhooks)
   - [Middleware/iPaaS Integration](#middlewareipaas-integration)
   - [Data Warehouse Integration](#data-warehouse-integration)
9. [Quick Reference](#quick-reference)
   - [Common Endpoints](#common-endpoints)
   - [Filter Syntax Examples](#filter-syntax-examples)
   - [URL Parameters](#url-parameters)
   - [Error Codes](#error-codes)
   - [Implementation Checklist](#implementation-checklist)

---

## Overview

FlexiBee is a comprehensive cloud-based accounting and business management software system designed primarily for small and medium-sized businesses (SMBs) in Czech Republic, Slovakia, and Central Europe. It combines invoicing, inventory management, payroll, bank reconciliation, and financial reporting capabilities with a powerful REST API for seamless integration with external systems.

### Key Characteristics

- **Open, well-documented REST API** enabling easy integration from any programming language
- **Multi-format support** (JSON, XML, CSV, EDI, ISDOC)
- **Real-time webhook capabilities** for event-driven integrations
- **Cloud-based and self-hosted options** available
- **Developed by ABRA Systems** (official name: ABRA FlexiBee)

---

## Information Sources

This section provides a comprehensive list of all available FlexiBee API resources, documentation, libraries, case studies, and integration platforms.

### Official Documentation

| Resource | URL | Description |
|----------|-----|-------------|
| **Official Website** | [flexibee.eu](https://www.flexibee.eu) | Primary corporate site |
| **Main API Documentation** | [flexibee.eu/api](https://www.flexibee.eu/api/) | Official REST API documentation - comprehensive guide on REST API functionality and CRUD operations |
| **Reference Documentation** | [flexibee.eu/api/dokumentace/ref](https://www.flexibee.eu/api/dokumentace/ref/) | Detailed reference covering all API endpoints, parameters, and data structures |
| **REST API Collection** | [podpora.flexibee.eu - REST API](https://podpora.flexibee.eu/en/collections/2592813-dokumentacia-rest-api) | 87 articles covering authentication, record management, pagination, webhooks, and advanced commands |
| **Filtering Documentation** | [flexibee.eu/api/dokumentace/ref/filters](https://www.flexibee.eu/api/dokumentace/ref/filters/) | Complete guide to filtering records with supported operators and examples |
| **URL Parameters Guide** | [flexibee.eu/url-parametry](https://www.flexibee.eu/url-parametry/) | Documentation on all available URL parameters for pagination, sorting, and filtering |
| **Record Identifiers** | [podpora.flexibee.eu - identifikatory-zaznamov](https://podpora.flexibee.eu/en/articles/4725798-identifikatory-zaznamov) | Explains how to use internal IDs, code identifiers (code:), and external identifiers (ext:) |
| **Changes API & WebHooks** | [podpora.flexibee.eu - changes-api-a-webhooks](https://podpora.flexibee.eu/en/articles/3421857-changes-api-a-webhooks) | Real-time monitoring of database changes, webhook setup, and synchronization patterns |
| **Changes API (Slovak)** | [podpora.flexibee.eu - zmeny-api](https://podpora.flexibee.eu/en/articles/4744362-zmeny-api) | Additional Changes API documentation |
| **FAQ - API Questions** | [podpora.flexibee.eu - casto-kladene-otazky-api](https://podpora.flexibee.eu/en/articles/4786953-casto-kladene-otazky-api) | Frequently asked questions about API usage |
| **Common API Questions** | [flexibee.eu - tri-nejcastejsi-otazky](https://www.flexibee.eu/tri-nejcastejsi-otazky-pri-pouzivani-abra-flexibee-api/) | Three most common questions when using ABRA FlexiBee API |
| **Tutorial Part 2** | [podpora.flexibee.eu - ako-zacat-2-6](http://podpora.flexibee.eu/en/articles/3638738-ako-zacat-s-flexi-api-2-6) | Getting started: URL construction and basic concepts |
| **Tutorial Part 3** | [podpora.flexibee.eu - ako-zacat-3-6](http://podpora.flexibee.eu/en/articles/3638743-ako-zacat-s-rozhranim-flexi-api-3-6) | Getting started: Reading data via REST API |
| **Tutorial Part 6** | [podpora.flexibee.eu - ako-zacat-6-6](http://podpora.flexibee.eu/en/articles/3638757-ako-zacat-s-rozhranim-flexi-api-6-6) | Getting started: Creating and updating records |
| **API Query Usage** | [podpora.flexibee.eu - pouzivanie-query-v-api-v2](https://podpora.flexibee.eu/en/articles/5264924-pouzivanie-query-v-api-v2) | Guide on using /query parameter in API v2 for advanced filtering |
| **Demo Instance** | [demo.flexibee.eu](https://demo.flexibee.eu) | Test installation with latest FlexiBee version (credentials: winstrom/winstrom) |
| **Evidence List** | [demo.flexibee.eu/c/demo/evidence-list](https://demo.flexibee.eu/c/demo/evidence-list) | Browse all available evidence types with their properties and structure |
| **Demo Documentation** | [flexibee.eu/api/demo-flexibee-eu](https://www.flexibee.eu/api/demo-flexibee-eu/) | Documentation specifically about the demo environment setup and usage |

### GitHub Integrations & Libraries

#### Python Libraries

| Repository | URL | Description |
|------------|-----|-------------|
| **flexibee-scripts** | [github.com/braiins/flexibee-scripts](https://github.com/braiins/flexibee-scripts) | Python scripts for FlexiBee automation including importing bitcoin exchange rates and processing bank transactions |

#### PHP Libraries

| Repository | URL | Description |
|------------|-----|-------------|
| **php-abraflexi** | [github.com/Spoje-NET/php-abraflexi](https://github.com/Spoje-NET/php-abraflexi) | PHP 8.1+ library with 20+ practical examples, debug mode, PHPUnit tests, Composer integration |
| **FlexiPeeHP** | [github.com/Spoje-NET/FlexiPeeHP](https://github.com/Spoje-NET/FlexiPeeHP) | Earlier version of PHP library (deprecated) |
| **VitexSoftware/php-flexibee** | [github.com/VitexSoftware/php-flexibee](https://github.com/VitexSoftware/php-flexibee) | Alternative PHP library maintained by VitexSoftware |
| **Ecomailcz/flexibee-client** | [github.com/Ecomailcz/flexibee-client](https://github.com/Ecomailcz/flexibee-client) | Simple cURL-based FlexiBee client for making API requests |

#### Java Libraries

| Repository | URL | Description |
|------------|-----|-------------|
| **adleritech/flexibee** | [github.com/adleritech/flexibee](https://github.com/adleritech/flexibee) | Unofficial Java library with builder pattern for creating invoices (Maven: com.adleritech:flexibee:0.0.12) |

#### Ruby Libraries

| Repository | URL | Description |
|------------|-----|-------------|
| **danpecher/flexibee.rb** | [github.com/danpecher/flexibee.rb](https://github.com/danpecher/flexibee.rb) | Ruby wrapper for FlexiBee JSON REST API with pagination support and Active Resource compatibility |

#### Developer Tools

| Tool | URL | Description |
|------|-----|-------------|
| **Flexplorer** | [github.com/VitexSoftware/Flexplorer](https://github.com/VitexSoftware/Flexplorer) | Web-based developer console for exploring and testing the FlexiBee API with graphical interface, query builder, webhook management |

#### Integration Frameworks

| Framework | URL | Description |
|-----------|-----|-------------|
| **Unimapper/flexibee** | [github.com/unimapper/flexibee](https://github.com/unimapper/flexibee) | FlexiBee integration with Unimapper framework |
| **FlexiBee Topics** | [github.com/topics/flexibee](https://github.com/topics/flexibee) | Central hub for browsing all FlexiBee-related repositories (20 PHP, 2 Java, 1 JavaScript, 1 Ruby) |

### Case Studies

| Company | URL | Description |
|---------|-----|-------------|
| **Revolgy** | [revolgy.com/case-studies/moving-flexibee-to-appstream](https://www.revolgy.com/case-studies/moving-flexibee-to-appstream) | AWS AppStream migration case study - redesigning and migrating FlexiBee to AWS cloud infrastructure |
| **ESONIC** | [easyredmine.com/solutions/case-studies/esonic](https://www.easyredmine.com/solutions/case-studies/esonic-easy-redmine-synchronization-with-existing-enterprise-systems-flexibee-abra-iso) | Enterprise system integration - FlexiBee with Easy Redmine and ABRA ISO using XML files and REST API |
| **Easy Project** | [easyproject.com/solutions/easy-project-management-case-studies](https://www.easyproject.com/solutions/easy-project-management-case-studies/project-management-in-manufacturing-construction) | Financial monitoring - linking Easy Project with FlexiBee for transaction monitoring |

### Integration Platforms

#### E-Commerce Integrations

| Platform | URL | Description |
|----------|-----|-------------|
| **Shopify + FlexiBee (MakeBeCool)** | [makebecool.com/integration/abra-flexibee](https://www.makebecool.com/integration/abra-flexibee) | Automatic transfer of orders and products between Shopify and FlexiBee |
| **Shopify + FlexiBee (Dativery)** | [dativery.com/en/s/shopify-to-flexibee](https://www.dativery.com/en/s/shopify-to-flexibee/) | Order and product synchronization with stock status updates |
| **Shoptet Integration** | [dativery.com/en/s/shoptet-to-flexibee](https://www.dativery.com/en/s/shoptet-to-flexibee/) | Automatic transfer between Shoptet e-shop and FlexiBee |
| **WooCommerce Integration** | [make.com/en/integrations/woocommerce/flexibee](https://www.make.com/en/integrations/woocommerce/flexibee) | WooCommerce to ABRA FlexiBee automated workflow integration |

#### Workflow Automation

| Platform | URL | Description |
|----------|-----|-------------|
| **Make.com** | [make.com/en/integrations/flexibee](https://www.make.com/en/integrations/flexibee) | Visual workflow automation platform with 1000+ app integrations, webhook-based processing |
| **Dativery** | [dativery.com/en/apps/flexibee](https://www.dativery.com/en/apps/flexibee/) | Integration platform connecting FlexiBee with various web applications and e-commerce platforms |
| **Keboola Data Export** | [keboola.com/components/export-data-from-flexibee](https://www.keboola.com/components/export-data-from-flexibee) | Data export component for extracting FlexiBee data into data pipelines |

#### Document Automation

| Service | URL | Description |
|---------|-----|-------------|
| **Rossum.AI** | [dativery.com/en/support/help-center/rossum-ai-flexibee](https://www.dativery.com/en/support/help-center/applying-scenarios/extracting-invoices-using-rossum-ai-for-flexibee/) | AI-powered invoice extraction for FlexiBee using Rossum.AI technology |

### Community Resources

| Resource | URL | Description |
|----------|-----|-------------|
| **API Tracker** | [apitracker.io/a/flexibee-eu](https://apitracker.io/a/flexibee-eu) | Third-party developer documentation aggregator for ABRA FlexiBee API with SDKs and authentication guides |
| **CharlieBlog Tutorial** | [charlieblog.eu/clanek-flexibee-api-url-parametry](https://charlieblog.eu/clanek-flexibee-api-url-parametry) | Tutorial specifically focused on FlexiBee API URL parameters |
| **Integration Example (Czech)** | [petrhnilica.cz/cs/blog/2018/02/04](https://petrhnilica.cz/cs/blog/2018/02/04/integrace-a-komunikace-s-flexibee-02-integromat-z-objednavky-zakazka-poslat-gmail-zapsat-do-gsheets/) | Practical integration example with Integromat (now Make), Gmail, and Google Sheets |

---

## API Fundamentals

### Authentication

FlexiBee supports multiple authentication methods for API access:

#### HTTP Basic Authentication

The most common method uses HTTP Basic Auth with username and password.

**cURL Example:**

```bash
# Using demo credentials
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json"
```

**Python Example:**

```python
import requests
from requests.auth import HTTPBasicAuth

# Demo server credentials
base_url = "https://demo.flexibee.eu:5434"
username = "winstrom"
password = "winstrom"
company = "demo"

# Make authenticated request
response = requests.get(
    f"{base_url}/c/{company}/adresar.json",
    auth=HTTPBasicAuth(username, password)
)

if response.status_code == 200:
    data = response.json()
    print(f"Success! Retrieved {len(data.get('winstrom', {}).get('adresar', []))} records")
else:
    print(f"Error: {response.status_code}")
```

#### API Key Authentication

For production environments, API keys are generated in Site Settings → API section.

**cURL Example:**

```bash
# Using API key
curl "https://yourdomain.flexibee.eu/mod/api/?api_key=YOUR_API_KEY&method=checkConnection"
```

**Python Example:**

```python
import requests

api_key = "YOUR_API_KEY"
base_url = "https://yourdomain.flexibee.eu"

# Check connection with API key
response = requests.get(
    f"{base_url}/mod/api/",
    params={
        "api_key": api_key,
        "method": "checkConnection"
    }
)

print(response.json())
```

#### Security Best Practices

- Always use HTTPS for API calls (never HTTP in production)
- Rotate API keys periodically
- Never commit API keys to version control
- Store credentials in environment variables
- Use separate API keys for different integrations

**Python Example with Environment Variables:**

```python
import os
import requests
from requests.auth import HTTPBasicAuth

# Load credentials from environment
FLEXIBEE_URL = os.getenv("FLEXIBEE_URL")
FLEXIBEE_USER = os.getenv("FLEXIBEE_USER")
FLEXIBEE_PASSWORD = os.getenv("FLEXIBEE_PASSWORD")
FLEXIBEE_COMPANY = os.getenv("FLEXIBEE_COMPANY", "demo")

# Create reusable session
session = requests.Session()
session.auth = HTTPBasicAuth(FLEXIBEE_USER, FLEXIBEE_PASSWORD)
session.headers.update({"Content-Type": "application/json"})

# Make requests
response = session.get(f"{FLEXIBEE_URL}/c/{FLEXIBEE_COMPANY}/adresar.json")
```

### Base URL Structure

FlexiBee API follows a consistent URL pattern:

```
https://{server}:{port}/c/{company}/{evidence}/{id}.{format}
```

**URL Components:**

- `{server}` - Your FlexiBee server domain (e.g., `demo.flexibee.eu` or `yourdomain.flexibee.eu`)
- `{port}` - API port (typically `5434` for HTTPS, `5433` for HTTP)
- `{company}` - Company identifier (e.g., `demo`, or your company code)
- `{evidence}` - Evidence type/entity (e.g., `adresar`, `faktura-vydana`, `banka`)
- `{id}` - Optional record identifier (numeric ID, `code:VALUE`, or `ext:SYSTEM:ID`)
- `{format}` - Response format: `json`, `xml`, `csv`, `xls`, `vcf`, `ical`

**Examples:**

```bash
# Get all contacts in JSON format
https://demo.flexibee.eu:5434/c/demo/adresar.json

# Get specific invoice by ID in XML format
https://demo.flexibee.eu:5434/c/demo/faktura-vydana/123.xml

# Get record by code identifier
https://demo.flexibee.eu:5434/c/demo/adresar/code:CUST001.json

# Get record by external ID
https://demo.flexibee.eu:5434/c/demo/faktura-vydana/ext:SHOPIFY:10001.json
```

### Data Formats

FlexiBee supports multiple input and output formats:

| Format | Extension | Input | Output | Use Case |
|--------|-----------|-------|--------|----------|
| **JSON** | `.json` | ✓ | ✓ | Modern API integrations (recommended) |
| **XML** | `.xml` | ✓ | ✓ | Legacy systems, bulk operations |
| **CSV** | `.csv` | ✓ | ✓ | Spreadsheet exports/imports |
| **Excel** | `.xls` | ✗ | ✓ | Excel exports only |
| **DBF** | `.dbf` | ✗ | ✓ | Legacy database exports |
| **VCard** | `.vcf` | ✗ | ✓ | Contact exports |
| **iCalendar** | `.ical` | ✗ | ✓ | Calendar/event exports |
| **EDI** | `.edi` | ✓ | ✓ | Electronic Data Interchange |

**JSON Response Structure:**

```json
{
  "winstrom": {
    "success": "true",
    "@version": "1.0",
    "adresar": [
      {
        "id": "1",
        "kod": "CUST001",
        "nazev": "Example Company Ltd.",
        "email": "info@example.com",
        "ico": "12345678"
      }
    ]
  }
}
```

**Python Example - Handling Different Formats:**

```python
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("winstrom", "winstrom")
base_url = "https://demo.flexibee.eu:5434/c/demo"

# Get data as JSON
json_response = requests.get(f"{base_url}/adresar.json", auth=auth)
data = json_response.json()

# Get data as XML
xml_response = requests.get(f"{base_url}/adresar.xml", auth=auth)
xml_data = xml_response.text

# Get data as CSV
csv_response = requests.get(f"{base_url}/adresar.csv", auth=auth)
csv_data = csv_response.text

# Download as Excel file
xls_response = requests.get(f"{base_url}/adresar.xls", auth=auth)
with open("contacts.xls", "wb") as f:
    f.write(xls_response.content)
```

### Demo Server Access

FlexiBee provides a public demo server for testing and learning.

**Demo Server Details:**

- **URL**: `https://demo.flexibee.eu:5434`
- **Company**: `demo`
- **Username**: `winstrom`
- **Password**: `winstrom`
- **Data**: Periodically reset with sample data
- **Permissions**: Full read/write access (data modifications allowed)

**Quick Test - cURL:**

```bash
# List all available evidence types
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu/c/demo/evidence-list"

# Get first 5 contacts
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json?limit=5"

# Get properties of faktura-vydana (issued invoices)
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/properties.json"

# Get overdue invoices with specific fields
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/(stavUhrK%20!=%20'stavUhr.uhrazeno'%20and%20datSplat%20%3C%20now()).xml?detail=custom:sumCelkem,varSym&limit=100" \
  -o overdue-invoices.xml
```

**Python Example - Demo Server Class:**

```python
import requests
from requests.auth import HTTPBasicAuth
from typing import Optional, Dict, List, Any

class FlexiBeeDemo:
    """Simple FlexiBee API client for demo server"""

    def __init__(self):
        self.base_url = "https://demo.flexibee.eu:5434"
        self.company = "demo"
        self.auth = HTTPBasicAuth("winstrom", "winstrom")
        self.session = requests.Session()
        self.session.auth = self.auth

    def get_evidence_list(self) -> List[str]:
        """Get list of all available evidence types"""
        response = self.session.get(
            f"{self.base_url}/c/{self.company}/evidence-list.json"
        )
        response.raise_for_status()
        return response.json()

    def get_records(self, evidence: str, limit: int = 20,
                   detail: str = "summary") -> Dict[str, Any]:
        """Get records from specified evidence"""
        params = {
            "limit": limit,
            "detail": detail
        }
        response = self.session.get(
            f"{self.base_url}/c/{self.company}/{evidence}.json",
            params=params
        )
        response.raise_for_status()
        return response.json()

    def get_properties(self, evidence: str) -> Dict[str, Any]:
        """Get properties/schema for an evidence type"""
        response = self.session.get(
            f"{self.base_url}/c/{self.company}/{evidence}/properties.json"
        )
        response.raise_for_status()
        return response.json()

# Usage example
demo = FlexiBeeDemo()

# List all evidence types
evidence_list = demo.get_evidence_list()
print(f"Available evidence types: {len(evidence_list)}")

# Get contacts
contacts = demo.get_records("adresar", limit=5)
print(f"Retrieved contacts: {contacts}")

# Get invoice properties
invoice_props = demo.get_properties("faktura-vydana")
print(f"Invoice properties: {invoice_props}")
```

### Rate Limits

FlexiBee implements rate limiting to ensure server stability:

**Rate Limit Details:**

- Limits vary by subscription plan and server configuration
- Typical limits: 100-1000 requests per minute
- Exceeded limits return HTTP 429 (Too Many Requests)
- Response headers include rate limit information

**Best Practices:**

1. **Implement exponential backoff** for retries
2. **Batch requests** when possible using filters
3. **Cache frequently accessed data**
4. **Use webhooks** instead of polling for changes
5. **Monitor rate limit headers** in responses

**Python Example - Rate Limit Handling:**

```python
import requests
import time
from requests.auth import HTTPBasicAuth

def make_request_with_retry(url, auth, max_retries=3, backoff_factor=2):
    """Make request with exponential backoff on rate limit"""

    for attempt in range(max_retries):
        response = requests.get(url, auth=auth)

        # Success
        if response.status_code == 200:
            return response

        # Rate limit exceeded
        elif response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', backoff_factor ** attempt))
            print(f"Rate limited. Waiting {retry_after} seconds...")
            time.sleep(retry_after)
            continue

        # Other error
        else:
            response.raise_for_status()

    raise Exception(f"Max retries ({max_retries}) exceeded")

# Usage
auth = HTTPBasicAuth("winstrom", "winstrom")
url = "https://demo.flexibee.eu:5434/c/demo/adresar.json"

try:
    response = make_request_with_retry(url, auth)
    data = response.json()
    print("Success!")
except Exception as e:
    print(f"Failed: {e}")
```

**Python Example - Batch Processing:**

```python
import requests
from requests.auth import HTTPBasicAuth
import time

class FlexiBeeBatchClient:
    """Client with built-in rate limiting and batching"""

    def __init__(self, base_url, company, username, password,
                 requests_per_minute=100):
        self.base_url = base_url
        self.company = company
        self.auth = HTTPBasicAuth(username, password)
        self.requests_per_minute = requests_per_minute
        self.min_interval = 60.0 / requests_per_minute
        self.last_request_time = 0

    def _wait_if_needed(self):
        """Ensure minimum interval between requests"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request_time = time.time()

    def get(self, evidence, params=None):
        """Make GET request with rate limiting"""
        self._wait_if_needed()

        response = requests.get(
            f"{self.base_url}/c/{self.company}/{evidence}.json",
            auth=self.auth,
            params=params
        )

        return response.json()

# Usage - automatically rate limited
client = FlexiBeeBatchClient(
    "https://demo.flexibee.eu:5434",
    "demo",
    "winstrom",
    "winstrom",
    requests_per_minute=50  # Conservative limit
)

# Make multiple requests - automatically throttled
for i in range(10):
    data = client.get("adresar", params={"limit": 10, "start": i * 10})
    print(f"Batch {i}: Retrieved records")
```

---

## Core Concepts

### Evidence Types

In FlexiBee, **evidence** (or "evidence types") refers to the different categories of business data and entities that the system manages. Each evidence type represents a specific domain object like invoices, contacts, products, or bank transactions.

**Common Evidence Types:**

| Evidence Name | Czech Name | Description |
|---------------|------------|-------------|
| `adresar` | Adresář | Address book / Contacts - customers, suppliers, partners |
| `faktura-vydana` | Faktura vydaná | Issued invoices - sales invoices sent to customers |
| `faktura-prijata` | Faktura přijatá | Received invoices - purchase invoices from suppliers |
| `objednavka-vydana` | Objednávka vydaná | Issued orders - sales orders from customers |
| `objednavka-prijata` | Objednávka přijatá | Received orders - purchase orders to suppliers |
| `banka` | Banka | Bank accounts - configured bank account records |
| `pohyb` | Pohyb | Bank movements - individual bank transactions |
| `cenik` | Ceník | Price list - products and services catalog |
| `sklad` | Sklad | Warehouse - inventory and stock items |
| `pohyb-na-sklade` | Pohyb na skladě | Stock movements - warehouse transactions |
| `penezni-pohyb` | Peněžní pohyb | Cash movements - cash register transactions |
| `nabidka-vydana` | Nabídka vydaná | Issued quotes - sales quotations |
| `poptavka-prijata` | Poptávka přijatá | Received requests - purchase inquiries |
| `dodaci-list` | Dodací list | Delivery notes - shipping documents |
| `smlouva` | Smlouva | Contracts - business agreements |
| `udalost` | Událost | Events - calendar events and tasks |

**Discovering Available Evidence:**

```bash
# cURL - List all evidence types
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu/c/demo/evidence-list.json"
```

```python
# Python - Get all evidence types
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("winstrom", "winstrom")
response = requests.get(
    "https://demo.flexibee.eu/c/demo/evidence-list.json",
    auth=auth
)

evidence_list = response.json()
print(f"Total evidence types: {len(evidence_list)}")
for evidence in evidence_list[:10]:  # Show first 10
    print(f"  - {evidence}")
```

**Exploring Evidence Properties:**

Each evidence type has a schema defining its fields, data types, and relationships.

```bash
# cURL - Get properties of issued invoices
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/properties.json"
```

```python
# Python - Explore evidence schema
def get_evidence_schema(evidence_name):
    """Get detailed schema for an evidence type"""
    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/{evidence_name}/properties.json",
        auth=auth
    )
    return response.json()

# Get invoice schema
invoice_schema = get_evidence_schema("faktura-vydana")

# Extract field names and types
if "winstrom" in invoice_schema:
    properties = invoice_schema["winstrom"].get("properties", {})
    print(f"Invoice fields: {len(properties)}")
    for field_name, field_info in list(properties.items())[:5]:
        print(f"  {field_name}: {field_info.get('type', 'N/A')}")
```

### Record Identifiers

FlexiBee supports three types of record identifiers for accessing and referencing records:

#### 1. Numeric ID (Internal ID)

The system's internal unique identifier assigned automatically.

**Format:** Integer number

**Usage:**

```bash
# cURL - Get invoice by ID
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/123.json"
```

```python
# Python - Get record by numeric ID
def get_by_id(evidence, record_id):
    """Fetch record by internal ID"""
    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/{evidence}/{record_id}.json",
        auth=auth
    )
    return response.json()

# Get invoice with ID 123
invoice = get_by_id("faktura-vydana", 123)
```

#### 2. Code Identifier (code:)

User-defined business codes for records.

**Format:** `code:VALUE`

**Usage:**

```bash
# cURL - Get contact by code
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar/code:CUST001.json"
```

```python
# Python - Get record by code
def get_by_code(evidence, code):
    """Fetch record by business code"""
    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/{evidence}/code:{code}.json",
        auth=auth
    )
    return response.json()

# Get customer with code "CUST001"
customer = get_by_code("adresar", "CUST001")
```

#### 3. External Identifier (ext:)

Used for cross-system integration to map external system IDs to FlexiBee records.

**Format:** `ext:SYSTEM:ID`

- `SYSTEM` - External system name (e.g., SHOPIFY, CRM, ERP)
- `ID` - Record ID in the external system

**Usage:**

```bash
# cURL - Get invoice by external ID
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/ext:SHOPIFY:10001.json"
```

```python
# Python - Working with external IDs
class FlexiBeeIntegration:
    """Helper for managing external ID mappings"""

    def __init__(self, base_url, company, auth):
        self.base_url = base_url
        self.company = company
        self.auth = auth

    def get_by_external_id(self, evidence, system, external_id):
        """Fetch record by external system ID"""
        response = requests.get(
            f"{self.base_url}/c/{self.company}/{evidence}/ext:{system}:{external_id}.json",
            auth=self.auth
        )
        return response.json()

    def create_with_external_id(self, evidence, system, external_id, data):
        """Create record with external ID for future reference"""
        data['external-ids'] = [f"{system}:{external_id}"]

        response = requests.put(
            f"{self.base_url}/c/{self.company}/{evidence}.json",
            auth=self.auth,
            json={"winstrom": {evidence: [data]}}
        )
        return response.json()

# Usage example
integration = FlexiBeeIntegration(
    "https://demo.flexibee.eu:5434",
    "demo",
    HTTPBasicAuth("winstrom", "winstrom")
)

# Get order from Shopify system
order = integration.get_by_external_id("faktura-vydana", "SHOPIFY", "10001")

# Create invoice with external reference
new_invoice_data = {
    "typDokl": "code:FAKTURA",
    "firma": "code:CUST001",
    "datVyst": "2025-11-12"
}
result = integration.create_with_external_id(
    "faktura-vydana",
    "SHOPIFY",
    "10002",
    new_invoice_data
)
```

**Best Practices for Identifiers:**

- **Numeric ID**: Use for internal operations and when you already have the FlexiBee ID
- **Code (code:)**: Use for human-readable business identifiers (customer codes, product SKUs)
- **External ID (ext:)**: Use for integration with other systems to maintain bidirectional mapping

### Primary Entities

#### 1. Invoices (Faktury)

The core financial document for recording sales and purchases.

**Issued Invoices (faktura-vydana)** - Sales invoices

```python
# Python - Working with issued invoices
def create_issued_invoice(customer_code, items, due_days=14):
    """Create a new issued invoice"""
    import datetime

    invoice_data = {
        "typDokl": "code:FAKTURA",  # Document type
        "firma": f"code:{customer_code}",  # Customer reference
        "datVyst": datetime.date.today().isoformat(),  # Issue date
        "datSplat": (datetime.date.today() +
                     datetime.timedelta(days=due_days)).isoformat(),  # Due date
        "polozkyFaktury": items  # Invoice line items
    }

    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.put(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        json={"winstrom": {"faktura-vydana": [invoice_data]}}
    )

    return response.json()

# Create invoice with line items
items = [
    {
        "nazev": "Web Development Services",
        "mnozMj": 40,  # Quantity (hours)
        "cenaMj": 50.00,  # Unit price
        "szbDph": "21%"  # VAT rate
    },
    {
        "nazev": "Hosting Fee",
        "mnozMj": 1,
        "cenaMj": 100.00,
        "szbDph": "21%"
    }
]

result = create_issued_invoice("CUST001", items, due_days=30)
```

**Key Invoice Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Internal ID |
| `kod` | String | Invoice code/number |
| `typDokl` | Reference | Document type (e.g., code:FAKTURA) |
| `firma` | Reference | Customer/supplier reference |
| `datVyst` | Date | Issue date |
| `datSplat` | Date | Due date |
| `sumCelkem` | Decimal | Total amount including VAT |
| `sumCelkemMen` | Decimal | Total in foreign currency |
| `stavUhrK` | Enum | Payment status |
| `varSym` | String | Variable symbol (payment reference) |
| `polozkyFaktury` | Array | Invoice line items |
| `external-ids` | Array | External system identifiers |

**Received Invoices (faktura-prijata)** - Purchase invoices

```bash
# cURL - Get received invoices from last 30 days
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-prijata.json?filter[datVyst@from]=2025-10-13&limit=10"
```

```python
# Python - Query received invoices
def get_recent_received_invoices(days=30):
    """Get received invoices from last N days"""
    import datetime

    date_from = (datetime.date.today() -
                 datetime.timedelta(days=days)).isoformat()

    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-prijata.json",
        auth=auth,
        params={
            "filter[datVyst@from]": date_from,
            "detail": "full"
        }
    )

    return response.json()

# Get invoices from last week
invoices = get_recent_received_invoices(days=7)
```

#### 2. Customers & Contacts (Adresar)

The address book containing all business contacts.

```python
# Python - Contact management
def create_contact(name, email=None, phone=None, ico=None, dic=None):
    """Create a new contact in address book"""
    contact_data = {
        "nazev": name,  # Company/person name
        "email": email,
        "telefon": phone,
        "ic": ico,  # Company tax ID (IČO)
        "dic": dic  # VAT ID
    }

    # Remove None values
    contact_data = {k: v for k, v in contact_data.items() if v is not None}

    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.put(
        "https://demo.flexibee.eu:5434/c/demo/adresar.json",
        auth=auth,
        json={"winstrom": {"adresar": [contact_data]}}
    )

    return response.json()

def search_contacts(query):
    """Search contacts by name or email"""
    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/adresar.json",
        auth=auth,
        params={
            "filter[nazev@like]": f"*{query}*",
            "detail": "summary"
        }
    )

    return response.json()

# Create new customer
new_customer = create_contact(
    name="Example Corp Ltd.",
    email="contact@example.com",
    phone="+420123456789",
    ico="12345678",
    dic="CZ12345678"
)

# Search for contacts
results = search_contacts("Example")
```

**Key Contact Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `nazev` | String | Company/person name |
| `email` | String | Email address |
| `telefon` | String | Phone number |
| `ic` | String | Company tax ID (IČO) |
| `dic` | String | VAT ID |
| `ulice` | String | Street address |
| `mesto` | String | City |
| `psc` | String | Postal code |
| `stat` | Reference | Country code |
| `typVztahuK` | Enum | Relationship type (customer, supplier, both) |

#### 3. Bank Accounts & Payments (Banka, Pohyb)

**Bank Accounts (banka):**

```python
# Python - List configured bank accounts
def get_bank_accounts():
    """Get all configured bank accounts"""
    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/banka.json",
        auth=auth,
        params={"detail": "full"}
    )

    return response.json()

accounts = get_bank_accounts()
```

**Bank Movements (pohyb):**

```python
# Python - Get bank transactions
def get_bank_transactions(bank_account_code, date_from=None, date_to=None):
    """Get bank transactions for specific account"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    params = {
        "filter[banka]": f"code:{bank_account_code}",
        "detail": "full"
    }

    if date_from:
        params["filter[datum@from]"] = date_from
    if date_to:
        params["filter[datum@to]"] = date_to

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/pohyb.json",
        auth=auth,
        params=params
    )

    return response.json()

# Get transactions from main account for November 2025
transactions = get_bank_transactions(
    "MAIN",
    date_from="2025-11-01",
    date_to="2025-11-30"
)
```

#### 4. Inventory & Stock (Cenik, Sklad)

**Price List / Products (cenik):**

```python
# Python - Product catalog management
def create_product(name, sku, price, vat_rate="21%", unit="ks"):
    """Create a new product in catalog"""
    product_data = {
        "nazev": name,  # Product name
        "skup": "code:PRODUCTS",  # Product group
        "ean": sku,  # SKU/EAN code
        "cenaNakup": price,  # Purchase price
        "cenaProdej": price * 1.3,  # Sales price (example markup)
        "szbDph": vat_rate,  # VAT rate
        "mj": unit  # Unit of measure (ks=pieces, hod=hours, etc.)
    }

    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.put(
        "https://demo.flexibee.eu:5434/c/demo/cenik.json",
        auth=auth,
        json={"winstrom": {"cenik": [product_data]}}
    )

    return response.json()

def get_products_in_stock():
    """Get products with available stock"""
    auth = HTTPBasicAuth("winstrom", "winstrom")
    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/cenik.json",
        auth=auth,
        params={
            "filter[stavMj@gt]": 0,  # Stock quantity > 0
            "detail": "custom:nazev,ean,stavMj,cenaProdej"
        }
    )

    return response.json()

# Create new product
new_product = create_product(
    name="Wireless Mouse",
    sku="WM-001",
    price=15.00,
    vat_rate="21%",
    unit="ks"
)

# Get in-stock products
in_stock = get_products_in_stock()
```

**Warehouse Movements (pohyb-na-sklade):**

```bash
# cURL - Get recent stock movements
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/pohyb-na-sklade.json?limit=20&order=datVyst@D"
```

```python
# Python - Track stock movements
def get_stock_movements(product_code=None, warehouse_code=None, days=30):
    """Get stock movements with optional filters"""
    import datetime

    auth = HTTPBasicAuth("winstrom", "winstrom")

    params = {
        "filter[datVyst@from]": (datetime.date.today() -
                                  datetime.timedelta(days=days)).isoformat(),
        "order": "datVyst@D",  # Sort by date descending
        "detail": "full"
    }

    if product_code:
        params["filter[cenik]"] = f"code:{product_code}"
    if warehouse_code:
        params["filter[sklad]"] = f"code:{warehouse_code}"

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/pohyb-na-sklade.json",
        auth=auth,
        params=params
    )

    return response.json()

# Get movements for specific product
movements = get_stock_movements(product_code="WM-001", days=7)
```

#### 5. Financial Records

**Key Financial Evidence Types:**

- **Chart of Accounts** - `ucet` - General ledger structure
- **Ledger Entries** - `interni-doklad` - Accounting journal entries
- **Cost Centers** - `stredisko` - Internal cost allocation
- **Tax Records** - `dapovin` - Tax obligation records

---

## Getting Data from FlexiBee

This section focuses on reading and querying data from FlexiBee using the REST API.

### Reading Data (GET)

#### Basic Data Retrieval

**Get All Records from an Evidence:**

```bash
# cURL - Get all contacts (default limit: 20)
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json"
```

```python
# Python - Basic data retrieval
import requests
from requests.auth import HTTPBasicAuth

def get_records(evidence, limit=20, detail="summary"):
    """Get records from any evidence type"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    params = {
        "limit": limit,
        "detail": detail
    }

    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/{evidence}.json",
        auth=auth,
        params=params
    )

    response.raise_for_status()
    return response.json()

# Get first 20 invoices
invoices = get_records("faktura-vydana", limit=20)

# Get all contacts (limit=0 means no limit)
all_contacts = get_records("adresar", limit=0)
```

**Get Specific Record by ID:**

```bash
# cURL - Get invoice by ID
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/123.json"
```

```python
# Python - Get single record
def get_record_by_id(evidence, record_id):
    """Fetch single record by ID"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/{evidence}/{record_id}.json",
        auth=auth
    )

    response.raise_for_status()
    return response.json()

# Get specific invoice
invoice = get_record_by_id("faktura-vydana", 123)
```

#### Detail Levels

FlexiBee supports different detail levels for controlling how much data is returned:

| Detail Level | Description | Use Case |
|--------------|-------------|----------|
| `summary` | Basic fields only (default) | List views, performance-critical queries |
| `full` | All fields including relationships | Detailed record inspection |
| `id` | Only record IDs | Quick existence checks, counting |
| `custom:field1,field2` | Specific fields only | Optimized queries for specific data |

**Examples:**

```bash
# cURL - Different detail levels
# Summary (default)
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json?detail=summary"

# Full details
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json?detail=full"

# Only IDs
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json?detail=id"

# Custom fields
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?detail=custom:kod,firma,sumCelkem,datVyst"
```

```python
# Python - Using detail levels
def get_invoices_summary():
    """Get invoice summary for dashboard"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params={
            "detail": "custom:kod,firma,sumCelkem,datVyst,stavUhrK",
            "limit": 50
        }
    )

    return response.json()

def get_invoice_full_details(invoice_id):
    """Get complete invoice data"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/faktura-vydana/{invoice_id}.json",
        auth=auth,
        params={"detail": "full"}
    )

    return response.json()

# Get summary for list view
summary = get_invoices_summary()

# Get full details for specific invoice
full_invoice = get_invoice_full_details(123)
```

### Filtering and Querying

FlexiBee provides powerful filtering capabilities for querying data.

#### Filter Operators

| Operator | Syntax | Description | Example |
|----------|--------|-------------|---------|
| Equals | `=` or `eq` | Exact match | `id=123` |
| Not equals | `!=` or `ne` | Not equal to | `stavUhrK!=stavUhr.uhrazeno` |
| Greater than | `>` or `gt` | Greater than | `sumCelkem>1000` |
| Less than | `<` or `lt` | Less than | `datVyst<2025-01-01` |
| Greater or equal | `>=` or `gte` | Greater than or equal | `sumCelkem>=500` |
| Less or equal | `<=` or `lte` | Less than or equal | `datSplat<=2025-12-31` |
| Like | `@like` | Pattern matching | `nazev@like=*Ltd*` |
| Between | `@between` | Range query | `datVyst@between=2025-01-01,2025-12-31` |
| In | `@in` | Value in list | `stavUhrK@in=stavUhr.uhrazeno,stavUhr.castUhr` |

#### Basic Filtering

**Date Filters:**

```bash
# cURL - Invoices issued after specific date
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?filter[datVyst@from]=2025-01-01"

# Invoices due before today
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?filter[datSplat@to]=2025-11-12"
```

```python
# Python - Date filtering
import datetime

def get_invoices_by_date_range(date_from=None, date_to=None):
    """Get invoices within date range"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    params = {}
    if date_from:
        params["filter[datVyst@from]"] = date_from
    if date_to:
        params["filter[datVyst@to]"] = date_to

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params=params
    )

    return response.json()

# Get invoices from last 30 days
date_from = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
recent_invoices = get_invoices_by_date_range(date_from=date_from)

# Get invoices for specific month
month_invoices = get_invoices_by_date_range(
    date_from="2025-11-01",
    date_to="2025-11-30"
)
```

**Numeric Filters:**

```bash
# cURL - Invoices over 1000 CZK
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?filter[sumCelkem@gt]=1000"
```

```python
# Python - Numeric filtering
def get_high_value_invoices(min_amount=1000):
    """Get invoices above specified amount"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params={
            "filter[sumCelkem@gt]": min_amount,
            "order": "sumCelkem@D"  # Sort descending
        }
    )

    return response.json()

# Get invoices over 10,000 CZK
high_value = get_high_value_invoices(min_amount=10000)
```

**Text Search:**

```bash
# cURL - Search contacts by name (wildcard)
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json?filter[nazev@like]=*Corp*"
```

```python
# Python - Text search
def search_contacts(search_term):
    """Search contacts by name"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/adresar.json",
        auth=auth,
        params={
            "filter[nazev@like]": f"*{search_term}*",
            "detail": "summary"
        }
    )

    return response.json()

# Search for companies with "Ltd" in name
companies = search_contacts("Ltd")
```

#### Complex Filtering

**Multiple Filters (AND logic):**

```bash
# cURL - Unpaid invoices over 1000 CZK
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?filter[sumCelkem@gt]=1000&filter[stavUhrK]=stavUhr.neuhrazeno"
```

```python
# Python - Multiple filter conditions
def get_overdue_unpaid_invoices(min_amount=0):
    """Get unpaid invoices that are overdue"""
    import datetime

    auth = HTTPBasicAuth("winstrom", "winstrom")

    today = datetime.date.today().isoformat()

    params = {
        "filter[stavUhrK]": "stavUhr.neuhrazeno",  # Unpaid status
        "filter[datSplat@to]": today,  # Due date passed
        "order": "datSplat",  # Sort by due date
        "detail": "custom:kod,firma,sumCelkem,datSplat,varSym"
    }

    if min_amount > 0:
        params["filter[sumCelkem@gt]"] = min_amount

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params=params
    )

    return response.json()

# Get overdue unpaid invoices over 500 CZK
overdue = get_overdue_unpaid_invoices(min_amount=500)
```

**Filter by Related Entity:**

```bash
# cURL - Invoices for specific customer
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?filter[firma]=code:CUST001"
```

```python
# Python - Filter by relationship
def get_customer_invoices(customer_code):
    """Get all invoices for specific customer"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params={
            "filter[firma]": f"code:{customer_code}",
            "order": "datVyst@D",
            "detail": "full"
        }
    )

    return response.json()

# Get all invoices for customer CUST001
customer_invoices = get_customer_invoices("CUST001")
```

#### Advanced Query Syntax

For complex queries, use the inline filter syntax:

```bash
# cURL - Complex query with parentheses
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana/(stavUhrK%20!=%20'stavUhr.uhrazeno'%20and%20datSplat%20%3C%20'2025-11-12').json"
```

```python
# Python - Complex query builder
def build_complex_query(evidence, conditions):
    """Build URL with complex filter conditions"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    # URL encode the condition string
    import urllib.parse
    encoded_conditions = urllib.parse.quote(conditions)

    url = f"https://demo.flexibee.eu:5434/c/demo/{evidence}/({encoded_conditions}).json"

    response = requests.get(url, auth=auth)
    return response.json()

# Example: Unpaid invoices due in the past
query = "stavUhrK != 'stavUhr.uhrazeno' and datSplat < '2025-11-12'"
overdue_invoices = build_complex_query("faktura-vydana", query)

# Example: High-value recent invoices
query = "sumCelkem > 5000 and datVyst >= '2025-10-01'"
high_value_recent = build_complex_query("faktura-vydana", query)
```

### Pagination and Sorting

#### Pagination

**Using limit and start parameters:**

```bash
# cURL - Get records 21-40 (second page, 20 per page)
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/adresar.json?limit=20&start=20"
```

```python
# Python - Pagination helper
def paginate_records(evidence, page_size=20, page_number=1):
    """Get paginated records"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    start = (page_number - 1) * page_size

    params = {
        "limit": page_size,
        "start": start,
        "add-row-count": "true"  # Include total count
    }

    response = requests.get(
        f"https://demo.flexibee.eu:5434/c/demo/{evidence}.json",
        auth=auth,
        params=params
    )

    data = response.json()

    # Extract total count from response
    total_count = 0
    if "winstrom" in data and "@rowCount" in data["winstrom"]:
        total_count = int(data["winstrom"]["@rowCount"])

    return {
        "data": data,
        "page": page_number,
        "page_size": page_size,
        "total_count": total_count,
        "total_pages": (total_count + page_size - 1) // page_size if total_count > 0 else 0
    }

# Get page 3 of contacts (40 per page)
page_3 = paginate_records("adresar", page_size=40, page_number=3)

print(f"Page {page_3['page']} of {page_3['total_pages']}")
print(f"Total records: {page_3['total_count']}")
```

**Iterating Through All Records:**

```python
# Python - Fetch all records in batches
def fetch_all_records(evidence, batch_size=100, filters=None):
    """Fetch all records from evidence in batches"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    all_records = []
    start = 0

    while True:
        params = {
            "limit": batch_size,
            "start": start
        }

        if filters:
            params.update(filters)

        response = requests.get(
            f"https://demo.flexibee.eu:5434/c/demo/{evidence}.json",
            auth=auth,
            params=params
        )

        data = response.json()

        # Extract records from response
        if "winstrom" in data and evidence in data["winstrom"]:
            records = data["winstrom"][evidence]

            if not records:  # No more records
                break

            all_records.extend(records)

            if len(records) < batch_size:  # Last page
                break

            start += batch_size
        else:
            break

    return all_records

# Fetch all invoices in batches of 50
all_invoices = fetch_all_records(
    "faktura-vydana",
    batch_size=50,
    filters={"filter[datVyst@from]": "2025-01-01"}
)

print(f"Total invoices fetched: {len(all_invoices)}")
```

#### Sorting

**Sort by single field:**

```bash
# cURL - Sort by date ascending
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?order=datVyst"

# Sort by date descending
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?order=datVyst@D"
```

```python
# Python - Sorting
def get_sorted_invoices(sort_field="datVyst", descending=False):
    """Get invoices sorted by field"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    # Add @D for descending sort
    order = f"{sort_field}@D" if descending else sort_field

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params={"order": order, "limit": 50}
    )

    return response.json()

# Get newest invoices first
newest_first = get_sorted_invoices("datVyst", descending=True)

# Get highest value invoices first
highest_value = get_sorted_invoices("sumCelkem", descending=True)
```

**Sort by multiple fields:**

```bash
# cURL - Sort by customer, then by date
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?order=firma&order=datVyst@D"
```

```python
# Python - Multi-field sorting
def get_multi_sorted_invoices():
    """Get invoices sorted by multiple fields"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    # Note: Multiple order parameters
    # requests doesn't support duplicate keys well, use tuples
    from urllib.parse import urlencode

    params = [
        ("order", "firma"),
        ("order", "datVyst@D"),
        ("limit", 100)
    ]

    query_string = urlencode(params)
    url = f"https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?{query_string}"

    response = requests.get(url, auth=auth)
    return response.json()

# Get invoices sorted by customer, then by date descending
sorted_invoices = get_multi_sorted_invoices()
```

### Field Selection

Select specific fields to improve query performance and reduce data transfer.

```bash
# cURL - Get only specific fields
curl -u winstrom:winstrom \
  "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json?detail=custom:kod,firma,sumCelkem,datVyst,stavUhrK"
```

```python
# Python - Optimized field selection
def get_invoice_summary_data(date_from=None):
    """Get minimal invoice data for reporting"""
    auth = HTTPBasicAuth("winstrom", "winstrom")

    # Select only needed fields
    fields = "kod,firma,sumCelkem,datVyst,datSplat,stavUhrK,varSym"

    params = {
        "detail": f"custom:{fields}",
        "limit": 0  # All records
    }

    if date_from:
        params["filter[datVyst@from]"] = date_from

    response = requests.get(
        "https://demo.flexibee.eu:5434/c/demo/faktura-vydana.json",
        auth=auth,
        params=params
    )

    return response.json()

# Get summary data for dashboard (only essential fields)
summary = get_invoice_summary_data(date_from="2025-01-01")
```

### Complete Query Example

Here's a comprehensive example combining all techniques:

```python
# Python - Complete query example
class FlexiBeeQueryBuilder:
    """Fluent query builder for FlexiBee API"""

    def __init__(self, base_url, company, auth):
        self.base_url = base_url
        self.company = company
        self.auth = auth
        self.params = {}

    def filter(self, field, operator, value):
        """Add filter condition"""
        param_key = f"filter[{field}{operator}]"
        self.params[param_key] = value
        return self

    def limit(self, count):
        """Set result limit"""
        self.params["limit"] = count
        return self

    def offset(self, start):
        """Set starting offset"""
        self.params["start"] = start
        return self

    def order_by(self, field, descending=False):
        """Set sort order"""
        self.params["order"] = f"{field}@D" if descending else field
        return self

    def fields(self, *field_names):
        """Select specific fields"""
        self.params["detail"] = f"custom:{','.join(field_names)}"
        return self

    def execute(self, evidence):
        """Execute query"""
        response = requests.get(
            f"{self.base_url}/c/{self.company}/{evidence}.json",
            auth=self.auth,
            params=self.params
        )
        response.raise_for_status()
        return response.json()

# Usage example
auth = HTTPBasicAuth("winstrom", "winstrom")
query = FlexiBeeQueryBuilder(
    "https://demo.flexibee.eu:5434",
    "demo",
    auth
)

# Build and execute complex query
results = (query
    .filter("datVyst", "@from", "2025-10-01")
    .filter("sumCelkem", "@gt", 1000)
    .filter("stavUhrK", "", "stavUhr.neuhrazeno")
    .order_by("sumCelkem", descending=True)
    .fields("kod", "firma", "sumCelkem", "datVyst", "datSplat")
    .limit(50)
    .execute("faktura-vydana"))

print(f"Found {len(results.get('winstrom', {}).get('faktura-vydana', []))} invoices")
```

---

## Real-World Examples

This section provides practical integration patterns based on real-world case studies.

### E-Commerce Integration

**Use Case:** Shopify/WooCommerce store integration with automatic invoice generation.

**Key Operations:**
1. Check if customer exists by email, create if needed
2. Verify products in catalog, create missing items
3. Generate invoice with external ID for tracking

```python
# Find or create customer
response = requests.get(
    f"{base_url}/c/{company}/adresar.json",
    auth=auth,
    params={"filter[email]": "customer@example.com"}
)

# Create invoice with external order reference
invoice_payload = {
    "winstrom": {
        "faktura-vydana": [{
            "typDokl": "code:FAKTURA",
            "firma": f"code:{customer_code}",
            "datVyst": "2025-11-12",
            "polozkyFaktury": [
                {"nazev": "Product Name", "mnozMj": 2, "cenaMj": 100.00, "szbDph": "21%"}
            ],
            "external-ids": ["SHOPIFY:10001"]
        }]
    }
}
```

### Invoice Automation

**Use Case:** Recurring monthly subscription billing.

```python
# Generate monthly invoices in batch
import datetime

today = datetime.date.today()

for customer_code, amount in subscriptions:
    payload = {
        "winstrom": {
            "faktura-vydana": [{
                "firma": f"code:{customer_code}",
                "datVyst": today.isoformat(),
                "polozkyFaktury": [{
                    "nazev": f"Subscription - {today.strftime('%B %Y')}",
                    "mnozMj": 1,
                    "cenaMj": amount,
                    "szbDph": "21%"
                }]
            }]
        }
    }
    requests.put(f"{base_url}/c/{company}/faktura-vydana.json", auth=auth, json=payload)
```

### Inventory Synchronization

**Use Case:** Multi-channel stock level synchronization.

```python
# Get current stock levels
response = requests.get(
    f"{base_url}/c/{company}/cenik.json",
    auth=auth,
    params={"detail": "custom:ean,stavMj", "limit": 0}
)

# Extract stock by SKU
stock_levels = {
    product["ean"]: float(product["stavMj"])
    for product in response.json()["winstrom"]["cenik"]
}

# Sync to external system
for sku, quantity in stock_levels.items():
    external_api.update_stock(sku, quantity)
```

### Payment Reconciliation

**Use Case:** Match bank transactions to invoices by variable symbol.

```python
# Get unpaid invoices
unpaid = requests.get(
    f"{base_url}/c/{company}/faktura-vydana.json",
    auth=auth,
    params={"filter[stavUhrK]": "stavUhr.neuhrazeno"}
).json()

# Get recent bank transactions
transactions = requests.get(
    f"{base_url}/c/{company}/pohyb.json",
    auth=auth,
    params={
        "filter[datum@from]": "2025-11-01",
        "filter[typPohybuK]": "typPohybu.prijem"
    }
).json()

# Match by variable symbol and amount
for transaction in transactions["winstrom"]["pohyb"]:
    var_symbol = transaction.get("varSymbol")
    amount = float(transaction.get("sumaMen", 0))

    # Find matching invoice
    for invoice in unpaid["winstrom"]["faktura-vydana"]:
        if invoice["varSym"] == var_symbol and abs(float(invoice["sumCelkem"]) - amount) < 0.01:
            print(f"Matched: {invoice['kod']}")
```

### Multi-System ERP Integration

**Use Case:** Sync customer data from CRM using external IDs.

```python
# Check if customer exists by external CRM ID
response = requests.get(
    f"{base_url}/c/{company}/adresar/ext:CRM:12345.json",
    auth=auth
)

# Create customer with external reference
if response.status_code != 200:
    payload = {
        "winstrom": {
            "adresar": [{
                "nazev": "Tech Solutions Ltd.",
                "email": "info@techsolutions.com",
                "external-ids": ["CRM:12345"]
            }]
        }
    }
    requests.put(f"{base_url}/c/{company}/adresar.json", auth=auth, json=payload)

# Create invoice from project time tracking
invoice_items = [
    {"nazev": f"Project: {task}", "mnozMj": hours, "cenaMj": 50.00, "szbDph": "21%"}
    for task, hours in time_entries
]
```

---

## User Personas & Common Questions

This section maps common business questions from different user personas to specific FlexiBee API queries.

### CFO / Finance Manager

**Primary Concerns:** Financial health, cash flow, reporting, compliance

**Common Questions & API Solutions:**

| Question | API Query |
|----------|-----------|
| "What is our current cash position?" | Get bank account balances: `GET /c/{company}/banka.json?detail=full` |
| "Which customers are paying late?" | Overdue invoices: `GET /c/{company}/faktura-vydana.json?filter[stavUhrK]=stavUhr.neuhrazeno&filter[datSplat@to]={today}` |
| "What are monthly revenue trends?" | Monthly issued invoices: `GET /c/{company}/faktura-vydana.json?filter[datVyst@from]={month_start}&filter[datVyst@to]={month_end}&detail=custom:sumCelkem` |
| "What's our total outstanding receivables?" | Unpaid invoices sum: `GET /c/{company}/faktura-vydana.json?filter[stavUhrK]=stavUhr.neuhrazeno&detail=custom:sumCelkem` |
| "Who are our top customers by revenue?" | Invoices grouped by customer: `GET /c/{company}/faktura-vydana.json?order=sumCelkem@D&detail=custom:firma,sumCelkem` |

**Example Code:**

```python
# Get overdue invoices
import datetime

today = datetime.date.today().isoformat()

response = requests.get(
    f"{base_url}/c/{company}/faktura-vydana.json",
    auth=auth,
    params={
        "filter[stavUhrK]": "stavUhr.neuhrazeno",
        "filter[datSplat@to]": today,
        "order": "datSplat",
        "detail": "custom:kod,firma,sumCelkem,datSplat,varSym"
    }
)

overdue = response.json()["winstrom"]["faktura-vydana"]
total_overdue = sum(float(inv["sumCelkem"]) for inv in overdue)
print(f"Total overdue: {total_overdue} CZK across {len(overdue)} invoices")
```

### Sales Manager

**Primary Concerns:** Customer relationships, revenue, sales pipeline

**Common Questions & API Solutions:**

| Question | API Query |
|----------|-----------|
| "Which customers have unpaid invoices?" | `GET /c/{company}/faktura-vydana.json?filter[stavUhrK]=stavUhr.neuhrazeno&detail=custom:firma,kod,sumCelkem` |
| "What's the average time from invoice to payment?" | Get paid invoices with dates: `GET /c/{company}/faktura-vydana.json?filter[stavUhrK]=stavUhr.uhrazeno&detail=custom:datVyst,datSplat` |
| "Who are our repeat customers?" | Get all customers: `GET /c/{company}/adresar.json` then count invoices per customer |
| "What's this month's sales total?" | Current month invoices: `GET /c/{company}/faktura-vydana.json?filter[datVyst@from]={month_start}&detail=custom:sumCelkem` |
| "Which products are selling best?" | Invoice line items analysis: `GET /c/{company}/faktura-vydana.json?detail=full` |

**Example Code:**

```python
# Get customer sales summary
def get_customer_sales_summary(customer_code):
    """Get total sales and invoice count for customer"""
    response = requests.get(
        f"{base_url}/c/{company}/faktura-vydana.json",
        auth=auth,
        params={
            "filter[firma]": f"code:{customer_code}",
            "detail": "custom:kod,sumCelkem,datVyst",
            "limit": 0
        }
    )

    invoices = response.json()["winstrom"]["faktura-vydana"]

    return {
        "customer": customer_code,
        "total_invoices": len(invoices),
        "total_revenue": sum(float(inv["sumCelkem"]) for inv in invoices),
        "latest_invoice": max(invoices, key=lambda x: x["datVyst"]) if invoices else None
    }
```

### Operations Manager

**Primary Concerns:** Inventory, fulfillment, efficiency

**Common Questions & API Solutions:**

| Question | API Query |
|----------|-----------|
| "What items are out of stock?" | Products with zero stock: `GET /c/{company}/cenik.json?filter[stavMj]=0` |
| "What's our current inventory value?" | All products: `GET /c/{company}/cenik.json?detail=custom:nazev,stavMj,cenaNakup` |
| "Which products are moving slowly?" | Stock movements analysis: `GET /c/{company}/pohyb-na-sklade.json?filter[datVyst@from]={date}&order=datVyst@D` |
| "How many orders are pending?" | Unfulfilled orders: `GET /c/{company}/objednavka-vydana.json?filter[stavK]=stav.nevyrizeny` |
| "What products need reordering?" | Low stock items: `GET /c/{company}/cenik.json?filter[stavMj@lt]=10` |

**Example Code:**

```python
# Get low stock products
def get_low_stock_products(threshold=10):
    """Get products below stock threshold"""
    response = requests.get(
        f"{base_url}/c/{company}/cenik.json",
        auth=auth,
        params={
            "filter[stavMj@lt]": threshold,
            "filter[stavMj@gt]": 0,  # Exclude out of stock
            "detail": "custom:nazev,ean,stavMj,cenaNakup",
            "order": "stavMj"
        }
    )

    products = response.json()["winstrom"]["cenik"]

    return [
        {
            "name": p["nazev"],
            "sku": p["ean"],
            "current_stock": float(p["stavMj"]),
            "unit_cost": float(p.get("cenaNakup", 0))
        }
        for p in products
    ]

low_stock = get_low_stock_products(threshold=20)
print(f"Found {len(low_stock)} products below threshold")
```

### E-Commerce Manager

**Primary Concerns:** Online sales, order processing, customer experience

**Common Questions & API Solutions:**

| Question | API Query |
|----------|-----------|
| "How many orders today?" | Today's invoices: `GET /c/{company}/faktura-vydana.json?filter[datVyst]={today}` |
| "Are inventory levels synced?" | Current stock: `GET /c/{company}/cenik.json?detail=custom:ean,stavMj` |
| "Which products are bestsellers this month?" | Month's invoices with line items: `GET /c/{company}/faktura-vydana.json?filter[datVyst@from]={month_start}&detail=full` |
| "What's our average order value?" | All invoices: `GET /c/{company}/faktura-vydana.json?detail=custom:sumCelkem` |
| "Any failed payment notifications?" | Unpaid recent invoices: `GET /c/{company}/faktura-vydana.json?filter[stavUhrK]=stavUhr.neuhrazeno&filter[datVyst@from]={week_ago}` |

**Example Code:**

```python
# Daily sales dashboard
import datetime

today = datetime.date.today().isoformat()

# Get today's orders
response = requests.get(
    f"{base_url}/c/{company}/faktura-vydana.json",
    auth=auth,
    params={
        "filter[datVyst]": today,
        "detail": "custom:kod,sumCelkem,firma"
    }
)

invoices = response.json()["winstrom"]["faktura-vydana"]

dashboard = {
    "date": today,
    "total_orders": len(invoices),
    "total_revenue": sum(float(inv["sumCelkem"]) for inv in invoices),
    "average_order_value": sum(float(inv["sumCelkem"]) for inv in invoices) / len(invoices) if invoices else 0
}

print(f"Today: {dashboard['total_orders']} orders, {dashboard['total_revenue']:.2f} CZK")
```

### Accountant / Bookkeeper

**Primary Concerns:** Accuracy, reconciliation, compliance

**Common Questions & API Solutions:**

| Question | API Query |
|----------|-----------|
| "Are all invoices recorded?" | All invoices by date: `GET /c/{company}/faktura-vydana.json?filter[datVyst@from]={date}&limit=0` |
| "Do bank accounts reconcile?" | Bank movements vs invoices: `GET /c/{company}/pohyb.json?filter[datum@from]={date}` |
| "Are payments correctly applied?" | Check payment status: `GET /c/{company}/faktura-vydana.json?detail=custom:kod,stavUhrK,sumCelkem` |
| "What documents need review?" | Recent changes: Use Changes API to track modifications |
| "Are VAT calculations correct?" | Invoice VAT details: `GET /c/{company}/faktura-vydana.json?detail=full` |

**Example Code:**

```python
# Bank reconciliation check
def reconciliation_report(date_from):
    """Compare bank transactions to invoice payments"""

    # Get bank transactions
    bank_response = requests.get(
        f"{base_url}/c/{company}/pohyb.json",
        auth=auth,
        params={
            "filter[datum@from]": date_from,
            "filter[typPohybuK]": "typPohybu.prijem",
            "detail": "custom:sumaMen,varSymbol"
        }
    )

    transactions = bank_response.json()["winstrom"]["pohyb"]

    # Get invoices paid in period
    invoice_response = requests.get(
        f"{base_url}/c/{company}/faktura-vydana.json",
        auth=auth,
        params={
            "filter[datVyst@from]": date_from,
            "detail": "custom:kod,varSym,sumCelkem,stavUhrK"
        }
    )

    invoices = invoice_response.json()["winstrom"]["faktura-vydana"]

    bank_total = sum(float(t.get("sumaMen", 0)) for t in transactions)
    paid_invoices = [inv for inv in invoices if "uhrazen" in inv.get("stavUhrK", "")]
    invoice_total = sum(float(inv["sumCelkem"]) for inv in paid_invoices)

    return {
        "bank_transactions": len(transactions),
        "bank_total": bank_total,
        "paid_invoices": len(paid_invoices),
        "invoice_total": invoice_total,
        "difference": bank_total - invoice_total
    }
```

### Business Owner / Entrepreneur

**Primary Concerns:** Overall performance, growth, profitability

**Common Questions & API Solutions:**

| Question | API Query |
|----------|-----------|
| "What's this month's revenue?" | Monthly invoices sum: `GET /c/{company}/faktura-vydana.json?filter[datVyst@from]={month_start}&detail=custom:sumCelkem` |
| "Are we profitable?" | Compare issued vs received invoices for period |
| "Who are our biggest customers?" | Top customers by revenue: `GET /c/{company}/faktura-vydana.json?order=sumCelkem@D` |
| "What's the business growth rate?" | Compare periods: Current vs previous month/quarter/year |
| "What are our key metrics?" | Dashboard combining multiple queries |

**Example Code:**

```python
# Executive dashboard
import datetime

def executive_dashboard(period_days=30):
    """Generate executive summary for specified period"""

    date_from = (datetime.date.today() - datetime.timedelta(days=period_days)).isoformat()

    # Revenue (issued invoices)
    issued = requests.get(
        f"{base_url}/c/{company}/faktura-vydana.json",
        auth=auth,
        params={"filter[datVyst@from]": date_from, "detail": "custom:sumCelkem"}
    ).json()["winstrom"]["faktura-vydana"]

    # Expenses (received invoices)
    received = requests.get(
        f"{base_url}/c/{company}/faktura-prijata.json",
        auth=auth,
        params={"filter[datVyst@from]": date_from, "detail": "custom:sumCelkem"}
    ).json()["winstrom"]["faktura-prijata"]

    # Unpaid invoices
    unpaid = requests.get(
        f"{base_url}/c/{company}/faktura-vydana.json",
        auth=auth,
        params={"filter[stavUhrK]": "stavUhr.neuhrazeno", "detail": "custom:sumCelkem"}
    ).json()["winstrom"]["faktura-vydana"]

    revenue = sum(float(inv["sumCelkem"]) for inv in issued)
    expenses = sum(float(inv["sumCelkem"]) for inv in received)
    outstanding = sum(float(inv["sumCelkem"]) for inv in unpaid)

    return {
        "period_days": period_days,
        "revenue": revenue,
        "expenses": expenses,
        "profit": revenue - expenses,
        "profit_margin": ((revenue - expenses) / revenue * 100) if revenue > 0 else 0,
        "outstanding_receivables": outstanding,
        "total_invoices": len(issued)
    }

dashboard = executive_dashboard(period_days=30)
print(f"30-day Summary:")
print(f"  Revenue: {dashboard['revenue']:.2f} CZK")
print(f"  Profit: {dashboard['profit']:.2f} CZK ({dashboard['profit_margin']:.1f}%)")
print(f"  Outstanding: {dashboard['outstanding_receivables']:.2f} CZK")
```

---

## Integration Patterns

### Webhooks (Event-Driven Integration)

FlexiBee supports webhooks for real-time notifications when data changes.

**Register a webhook:**

```bash
# cURL - Register webhook for invoice changes
curl -u username:password -X PUT \
  "https://flexibee.eu:5434/c/{company}/hooks.json?url=https://your-server.com/webhook&format=JSON"
```

**Python webhook receiver:**

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def flexibee_webhook():
    """Receive FlexiBee webhook notifications"""
    data = request.json

    # Process the change
    if 'winstrom' in data:
        changes = data['winstrom'].get('changes', [])
        for change in changes:
            evidence = change.get('evidence')
            operation = change.get('operation')  # insert, update, delete
            record_id = change.get('id')

            print(f"{operation.upper()} on {evidence}: ID {record_id}")

    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(port=8000)
```

### Changes API (Polling Pattern)

The Changes API enables efficient synchronization by tracking all database modifications with version numbers. Essential for systems that can't receive webhooks or need reliable change tracking.

**Key Concepts:**
- **Global Version Number**: Every change increments a global version counter
- **Since Parameter**: Request only changes after a specific version
- **Change Types**: Insert, update, delete operations
- **Evidence Filtering**: Track changes for specific evidence types only

**Activate Changes API:**

```bash
# Activate Changes API (requires exclusive database access)
curl -u username:password -X PUT \
  "https://flexibee.eu:5434/c/{company}/changes.json?enable=true"
```

**Basic Usage:**

```python
# Initialize tracking
last_version = 0  # Store persistently (database, file, etc.)

response = requests.get(
    f"{base_url}/c/{company}/changes.json",
    auth=auth,
    params={"since": last_version}
)

data = response.json()
new_version = int(data['winstrom']['@version'])

# Process changes
if 'changes' in data['winstrom']:
    for change in data['winstrom']['changes']:
        evidence = change.get('evidence-type')  # e.g., 'faktura-vydana'
        operation = change.get('operation')      # insert, update, delete
        record_id = change.get('id')
        external_id = change.get('external-ids', [])

        print(f"{operation.upper()}: {evidence} ID={record_id}")

# Save new version for next poll
last_version = new_version
```

**Filter by Evidence Type:**

```python
# Track only invoice changes
response = requests.get(
    f"{base_url}/c/{company}/changes.json",
    auth=auth,
    params={
        "since": last_version,
        "evidence-type": "faktura-vydana"  # Only invoices
    }
)
```

**Complete Synchronization Example:**

```python
import requests
from requests.auth import HTTPBasicAuth
import json
import time

class FlexiBeeChangeTracker:
    """Track and process FlexiBee changes"""

    def __init__(self, base_url, company, username, password, version_file='last_version.txt'):
        self.base_url = base_url
        self.company = company
        self.auth = HTTPBasicAuth(username, password)
        self.version_file = version_file
        self.last_version = self._load_version()

    def _load_version(self):
        """Load last processed version from file"""
        try:
            with open(self.version_file, 'r') as f:
                return int(f.read().strip())
        except FileNotFoundError:
            return 0

    def _save_version(self, version):
        """Save processed version to file"""
        with open(self.version_file, 'w') as f:
            f.write(str(version))

    def get_changes(self, evidence_type=None):
        """
        Get all changes since last check

        Args:
            evidence_type: Optional filter (e.g., 'faktura-vydana')

        Returns:
            List of changes and new version number
        """
        params = {"since": self.last_version}

        if evidence_type:
            params["evidence-type"] = evidence_type

        response = requests.get(
            f"{self.base_url}/c/{self.company}/changes.json",
            auth=self.auth,
            params=params
        )

        response.raise_for_status()
        data = response.json()

        new_version = int(data['winstrom']['@version'])
        changes = data['winstrom'].get('changes', [])

        return changes, new_version

    def process_change(self, change):
        """
        Process individual change record

        Args:
            change: Change dict with evidence-type, operation, id, etc.
        """
        evidence = change.get('evidence-type')
        operation = change.get('operation')
        record_id = change.get('id')

        if operation == 'insert':
            self.handle_insert(evidence, record_id)
        elif operation == 'update':
            self.handle_update(evidence, record_id)
        elif operation == 'delete':
            self.handle_delete(evidence, record_id)

    def handle_insert(self, evidence, record_id):
        """Handle new record"""
        # Fetch full record details
        response = requests.get(
            f"{self.base_url}/c/{self.company}/{evidence}/{record_id}.json",
            auth=self.auth
        )

        if response.status_code == 200:
            record = response.json()
            print(f"NEW {evidence}: {record}")
            # Sync to external system here

    def handle_update(self, evidence, record_id):
        """Handle updated record"""
        # Fetch updated record
        response = requests.get(
            f"{self.base_url}/c/{self.company}/{evidence}/{record_id}.json",
            auth=self.auth
        )

        if response.status_code == 200:
            record = response.json()
            print(f"UPDATED {evidence}: {record}")
            # Update external system here

    def handle_delete(self, evidence, record_id):
        """Handle deleted record"""
        print(f"DELETED {evidence} ID={record_id}")
        # Remove from external system here

    def sync(self, evidence_type=None):
        """
        Run synchronization cycle

        Args:
            evidence_type: Optional filter for specific evidence

        Returns:
            Number of changes processed
        """
        changes, new_version = self.get_changes(evidence_type)

        print(f"Found {len(changes)} changes (version {self.last_version} → {new_version})")

        for change in changes:
            try:
                self.process_change(change)
            except Exception as e:
                print(f"Error processing change: {e}")
                # Continue processing other changes

        # Update version after successful processing
        self.last_version = new_version
        self._save_version(new_version)

        return len(changes)

# Usage
tracker = FlexiBeeChangeTracker(
    "https://demo.flexibee.eu:5434",
    "demo",
    "winstrom",
    "winstrom"
)

# One-time sync
changes_count = tracker.sync()
print(f"Processed {changes_count} changes")

# Continuous sync loop
while True:
    try:
        changes_count = tracker.sync(evidence_type="faktura-vydana")
        if changes_count > 0:
            print(f"Synced {changes_count} invoice changes")

        time.sleep(60)  # Poll every minute

    except KeyboardInterrupt:
        print("Stopping sync...")
        break
    except Exception as e:
        print(f"Sync error: {e}")
        time.sleep(60)
```

**Change Record Structure:**

```json
{
  "winstrom": {
    "@version": "12345",
    "changes": [
      {
        "evidence-type": "faktura-vydana",
        "operation": "update",
        "id": "123",
        "external-ids": ["SHOPIFY:10001"],
        "lastUpdate": "2025-11-12T10:30:00"
      }
    ]
  }
}
```

**Best Practices:**

1. **Persist Version Number**: Store `last_version` in database or file to survive restarts
2. **Handle Errors Gracefully**: Don't update version if processing fails
3. **Batch Processing**: Process changes in batches to avoid overwhelming external systems
4. **Incremental Sync**: Only fetch full record data when needed
5. **Use External IDs**: Track records across systems using external-ids
6. **Monitor Version Gaps**: Alert if version number jumps significantly (missed changes)
7. **Regular Full Sync**: Periodically run full sync as backup strategy

**Polling Strategies:**

```python
# Strategy 1: Fixed interval (simple)
def poll_fixed_interval(tracker, interval_seconds=60):
    """Poll every N seconds"""
    while True:
        tracker.sync()
        time.sleep(interval_seconds)

# Strategy 2: Adaptive interval (efficient)
def poll_adaptive(tracker, min_interval=10, max_interval=300):
    """Adjust polling based on change frequency"""
    interval = min_interval

    while True:
        changes_count = tracker.sync()

        if changes_count > 0:
            interval = min_interval  # Changes detected, poll faster
        else:
            interval = min(interval * 1.5, max_interval)  # No changes, slow down

        time.sleep(interval)

# Strategy 3: Business hours only
def poll_business_hours(tracker):
    """Poll only during business hours"""
    import datetime

    while True:
        now = datetime.datetime.now()
        is_business_hours = (
            now.weekday() < 5 and  # Monday-Friday
            9 <= now.hour < 18      # 9 AM - 6 PM
        )

        if is_business_hours:
            tracker.sync()
            time.sleep(60)
        else:
            time.sleep(300)  # Check less frequently outside business hours
```

**Troubleshooting:**

| Issue | Cause | Solution |
|-------|-------|----------|
| Changes API not active | Not enabled | Activate with `enable=true` parameter |
| Version number reset | Database restored | Perform full sync, reset `last_version` |
| Missing changes | Version gap | Check for system downtime, run full reconciliation |
| Duplicate processing | Version not saved | Ensure version persists after successful processing |
| High API usage | Polling too frequently | Implement adaptive polling strategy |

### Batch Operations

Process multiple records in single request.

```python
# Batch create multiple invoices
invoices = [
    {"firma": "code:CUST001", "datVyst": "2025-11-12", "polozkyFaktury": [...]},
    {"firma": "code:CUST002", "datVyst": "2025-11-12", "polozkyFaktury": [...]}
]

payload = {
    "winstrom": {
        "faktura-vydana": invoices
    }
}

response = requests.put(
    f"{base_url}/c/{company}/faktura-vydana.json",
    auth=auth,
    json=payload
)
```

### Error Handling Pattern

```python
def safe_api_call(url, auth, params=None, max_retries=3):
    """API call with retry logic"""
    import time

    for attempt in range(max_retries):
        try:
            response = requests.get(url, auth=auth, params=params, timeout=30)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:  # Rate limit
                time.sleep(2 ** attempt)
                continue
            else:
                response.raise_for_status()

        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise

    raise Exception("Max retries exceeded")
```

---

## Quick Reference

### Common Endpoints

| Evidence | Endpoint | Description |
|----------|----------|-------------|
| Contacts | `/c/{company}/adresar.json` | Customers, suppliers, partners |
| Issued Invoices | `/c/{company}/faktura-vydana.json` | Sales invoices |
| Received Invoices | `/c/{company}/faktura-prijata.json` | Purchase invoices |
| Products | `/c/{company}/cenik.json` | Product catalog |
| Bank Accounts | `/c/{company}/banka.json` | Bank account list |
| Bank Transactions | `/c/{company}/pohyb.json` | Bank movements |
| Stock Movements | `/c/{company}/pohyb-na-sklade.json` | Inventory transactions |
| Orders Issued | `/c/{company}/objednavka-vydana.json` | Sales orders |

### Filter Operators Quick Reference

| Operator | Example | Description |
|----------|---------|-------------|
| `=` or `eq` | `id=123` | Equal to |
| `!=` or `ne` | `stavUhrK!=stavUhr.uhrazeno` | Not equal to |
| `>` or `@gt` | `sumCelkem@gt=1000` | Greater than |
| `<` or `@lt` | `datVyst@lt=2025-01-01` | Less than |
| `@like` | `nazev@like=*Ltd*` | Wildcard search |
| `@from` | `datVyst@from=2025-11-01` | Date from |
| `@to` | `datSplat@to=2025-11-30` | Date to |
| `@in` | `stavK@in=stav.novy,stav.vydany` | Value in list |

### Common URL Parameters

| Parameter | Example | Description |
|-----------|---------|-------------|
| `limit` | `limit=50` | Max records (0 = all) |
| `start` | `start=20` | Pagination offset |
| `order` | `order=datVyst@D` | Sort field (@D = descending) |
| `detail` | `detail=full` | Detail level (summary/full/id/custom) |
| `filter[field]` | `filter[stavUhrK]=stavUhr.neuhrazeno` | Filter condition |
| `add-row-count` | `add-row-count=true` | Include total count |

### Common Field Names

| Field | Czech | Description |
|-------|-------|-------------|
| `nazev` | Název | Name/Title |
| `kod` | Kód | Code |
| `firma` | Firma | Company/Customer reference |
| `datVyst` | Datum vystavení | Issue date |
| `datSplat` | Datum splatnosti | Due date |
| `sumCelkem` | Suma celkem | Total amount |
| `stavUhrK` | Stav úhrady | Payment status |
| `varSym` | Variabilní symbol | Variable symbol |
| `email` | E-mail | Email address |
| `telefon` | Telefon | Phone number |
| `ic` | IČO | Company tax ID |
| `dic` | DIČ | VAT ID |

### Common Status Values

**Invoice Payment Status (stavUhrK):**
- `stavUhr.neuhrazeno` - Unpaid
- `stavUhr.castUhr` - Partially paid
- `stavUhr.uhrazeno` - Paid

**Document Status (stavK):**
- `stav.novy` - New
- `stav.nevyrizeny` - Pending
- `stav.vydany` - Issued

### Quick Examples

**Get unpaid invoices:**
```bash
GET /c/{company}/faktura-vydana.json?filter[stavUhrK]=stavUhr.neuhrazeno
```

**Get this month's revenue:**
```bash
GET /c/{company}/faktura-vydana.json?filter[datVyst@from]=2025-11-01&detail=custom:sumCelkem
```

**Search customer by email:**
```bash
GET /c/{company}/adresar.json?filter[email]=customer@example.com
```

**Get low stock products:**
```bash
GET /c/{company}/cenik.json?filter[stavMj@lt]=10&filter[stavMj@gt]=0
```

### Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| `200` | Success | Request completed successfully |
| `400` | Bad Request | Check request format and parameters |
| `401` | Unauthorized | Verify credentials |
| `403` | Forbidden | Check permissions |
| `404` | Not Found | Record doesn't exist |
| `429` | Rate Limited | Implement exponential backoff |
| `500` | Server Error | Contact support or retry later |

### Implementation Checklist

- [ ] Obtain API credentials (username/password or API key)
- [ ] Test connection on demo server (demo.flexibee.eu)
- [ ] Implement authentication (HTTP Basic Auth)
- [ ] Test basic CRUD operations
- [ ] Implement error handling and retries
- [ ] Add logging for debugging
- [ ] Implement rate limiting
- [ ] Use external IDs for cross-system tracking
- [ ] Test pagination for large datasets
- [ ] Set up webhooks or Changes API for real-time sync
- [ ] Monitor API usage and performance
- [ ] Document integration for your team

---

**Last Updated**: 2025-11-12
