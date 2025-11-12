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

*Section to be populated*

---

## Getting Data from FlexiBee

*Section to be populated*

---

## Real-World Examples

*Section to be populated*

---

## User Personas & Common Questions

*Section to be populated*

---

## Integration Patterns

*Section to be populated*

---

## Quick Reference

*Section to be populated*

---

**Last Updated**: 2025-11-12
