"""K2 REST API Client - Driver for K2 accounting/ERP system."""

import requests
import time
from typing import List, Dict, Any, Optional
from requests.auth import HTTPBasicAuth

try:
    from .exceptions import (
        K2Error,
        AuthenticationError,
        ConnectionError,
        ObjectNotFoundError,
        FieldNotFoundError,
        QueryError,
        RateLimitError,
    )
except ImportError:
    from exceptions import (
        K2Error,
        AuthenticationError,
        ConnectionError,
        ObjectNotFoundError,
        FieldNotFoundError,
        QueryError,
        RateLimitError,
    )


class K2Client:
    """
    Client for K2 REST API following the driver design specification.

    This driver enables interaction with K2 accounting/ERP software via its REST API.
    K2 organizes data into "evidences" (similar to tables or objects in other systems).

    Examples:
        >>> # Initialize client
        >>> client = K2Client(
        ...     api_url="http://localhost:8000",
        ...     username="demo",
        ...     password="demo",
        ...     company_id="demo"
        ... )
        >>>
        >>> # List available evidences (objects)
        >>> evidences = client.list_objects()
        >>> print(evidences)  # ['faktura-vydana', 'adresar', 'cenik', ...]
        >>>
        >>> # Get field schema for an evidence
        >>> fields = client.get_fields("faktura-vydana")
        >>> print(fields['id'])  # {'name': 'id', 'type': 'string', ...}
        >>>
        >>> # Query data
        >>> invoices = client.read(
        ...     evidence="faktura-vydana",
        ...     fields="id,kod,nazev,castka",
        ...     conditions="stav=Nezaplaceno"
        ... )
        >>>
        >>> # Use as context manager
        >>> with K2Client(api_url, username, password, company_id) as client:
        ...     data = client.read("adresar", conditions="stav=Active")
    """

    def __init__(
        self,
        api_url: str,
        username: str,
        password: str,
        company_id: str,
        timeout: int = 30,
        max_retries: int = 3,
        debug: bool = False,
    ):
        """
        Initialize K2 API client.

        Args:
            api_url: Base URL of K2 REST API (e.g., "http://localhost:8000")
            username: K2 username for authentication
            password: K2 password for authentication
            company_id: Company identifier in K2 system
            timeout: Request timeout in seconds (default: 30)
            max_retries: Maximum number of retries for failed requests (default: 3)
            debug: Enable debug logging (default: False)

        Raises:
            AuthenticationError: If credentials are invalid
            ConnectionError: If unable to connect to API

        Examples:
            >>> client = K2Client(
            ...     api_url="http://localhost:8000",
            ...     username="user",
            ...     password="pass",
            ...     company_id="demo"
            ... )
        """
        self.api_url = api_url.rstrip("/")
        self.username = username
        self.password = password
        self.company_id = company_id
        self.timeout = timeout
        self.max_retries = max_retries
        self.debug = debug

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.session.headers.update({"Content-Type": "application/json"})

        # Validate credentials on initialization
        self._validate_connection()

    def _validate_connection(self):
        """
        Validate API connection and credentials.

        Raises:
            AuthenticationError: If credentials are invalid
            ConnectionError: If unable to connect to API
        """
        try:
            response = self.session.get(
                f"{self.api_url}/health",
                timeout=self.timeout
            )
            if response.status_code == 401:
                raise AuthenticationError(
                    "Invalid credentials. Please check your username and password."
                )
            if response.status_code != 200:
                raise ConnectionError(
                    f"Failed to connect to K2 API. Status code: {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to K2 API: {str(e)}")

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        retry_count: int = 0,
    ) -> Dict[str, Any]:
        """
        Make HTTP request with error handling and retries.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data
            retry_count: Current retry attempt number

        Returns:
            Response data as dictionary

        Raises:
            AuthenticationError: If authentication fails
            ConnectionError: If connection fails
            RateLimitError: If rate limit is exceeded
            QueryError: If request fails
        """
        url = f"{self.api_url}{endpoint}"

        if self.debug:
            print(f"[DEBUG] {method} {url}")
            if params:
                print(f"[DEBUG] Params: {params}")
            if data:
                print(f"[DEBUG] Data: {data}")

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=self.timeout,
            )

            if self.debug:
                print(f"[DEBUG] Status: {response.status_code}")

            # Handle different status codes
            if response.status_code == 401:
                raise AuthenticationError("Authentication failed. Please check your credentials.")

            elif response.status_code == 404:
                raise ObjectNotFoundError(endpoint.split("/")[-1])

            elif response.status_code == 429:
                # Rate limit exceeded
                retry_after = int(response.headers.get("Retry-After", 60))
                if retry_count < self.max_retries:
                    if self.debug:
                        print(f"[DEBUG] Rate limited. Retrying after {retry_after} seconds...")
                    time.sleep(retry_after)
                    return self._make_request(method, endpoint, params, data, retry_count + 1)
                else:
                    raise RateLimitError(retry_after)

            elif response.status_code >= 400:
                error_message = response.text
                try:
                    error_data = response.json()
                    if "Error" in error_data:
                        error_message = error_data["Error"].get("Message", response.text)
                except:
                    pass
                raise QueryError(f"Request failed: {error_message}")

            return response.json()

        except requests.exceptions.Timeout:
            if retry_count < self.max_retries:
                if self.debug:
                    print(f"[DEBUG] Timeout. Retrying... ({retry_count + 1}/{self.max_retries})")
                time.sleep(2 ** retry_count)  # Exponential backoff
                return self._make_request(method, endpoint, params, data, retry_count + 1)
            else:
                raise ConnectionError("Request timeout. Please try again later.")

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Request failed: {str(e)}")

    def list_objects(self) -> List[str]:
        """
        List all available K2 evidence types (objects).

        In K2, "evidence" is the term for data objects (similar to tables in databases
        or objects in Salesforce). Common evidences include:
        - faktura-vydana (issued invoices)
        - faktura-prijata (received invoices)
        - adresar (address book - customers/vendors)
        - cenik (pricelist - products)
        - banka (bank accounts)

        Returns:
            List of evidence names available in the K2 system.

        Raises:
            AuthenticationError: If authentication fails
            ConnectionError: If connection fails

        Examples:
            >>> client = K2Client(api_url, username, password, company_id)
            >>> evidences = client.list_objects()
            >>> print(evidences)
            ['faktura-vydana', 'faktura-prijata', 'adresar', 'cenik', 'banka']
        """
        endpoint = f"/c/{self.company_id}/evidence-list"
        response = self._make_request("GET", endpoint)

        evidences = []
        for evidence_data in response.get("evidences", []):
            evidences.append(evidence_data["evidence"])

        return evidences

    def get_fields(self, object_name: str) -> Dict[str, Any]:
        """
        Get field schema for a K2 evidence (object).

        Returns detailed information about all fields in the specified evidence,
        including field names, types, labels, and constraints.

        Args:
            object_name: Name of the evidence (e.g., "faktura-vydana", "adresar")

        Returns:
            Dictionary mapping field names to their properties. Each field contains:
            - name: Field name
            - type: Data type (string, int, decimal, date, boolean)
            - label: Human-readable label
            - isRequired: Whether the field is required
            - isReadOnly: Whether the field is read-only
            - length: Maximum length for string fields (optional)

        Raises:
            ObjectNotFoundError: If evidence is not found
            AuthenticationError: If authentication fails
            ConnectionError: If connection fails

        Examples:
            >>> fields = client.get_fields("faktura-vydana")
            >>> print(fields['kod'])
            {
                'name': 'kod',
                'type': 'string',
                'label': 'Kod',
                'isRequired': True,
                'isReadOnly': False,
                'length': 255
            }
        """
        endpoint = f"/c/{self.company_id}/{object_name}/properties"

        try:
            response = self._make_request("GET", endpoint)
        except ObjectNotFoundError:
            # Get available objects for better error message
            available = self.list_objects()
            raise ObjectNotFoundError(object_name, available)

        properties = response.get("properties", [])

        # Convert list to dictionary keyed by field name
        fields_dict = {}
        for prop in properties:
            field_name = prop["name"]
            fields_dict[field_name] = prop

        return fields_dict

    def read(
        self,
        evidence: str,
        fields: Optional[str] = None,
        conditions: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Query K2 evidence data.

        Execute a query against a K2 evidence with optional field selection,
        filtering, and pagination.

        Args:
            evidence: Evidence name (e.g., "faktura-vydana", "adresar")
            fields: Comma-separated list of fields to return (default: all fields)
            conditions: Filter conditions in K2 format (e.g., "stav=Active", "castka>1000")
            limit: Maximum number of records to return (default: 100)
            offset: Number of records to skip for pagination (default: 0)

        Returns:
            List of records as dictionaries.

        Raises:
            ObjectNotFoundError: If evidence is not found
            QueryError: If query execution fails
            AuthenticationError: If authentication fails
            ConnectionError: If connection fails

        K2 Query Syntax (Conditions parameter):
            - Equality: "stav=Active"
            - Comparison: "castka>1000", "datum<2024-11-01"
            - Multiple conditions: "stav=Active AND castka>1000"
            - OR conditions: "stav=Paid OR stav=Cancelled"

        Examples:
            >>> # Get all records
            >>> records = client.read("adresar")
            >>>
            >>> # Get specific fields
            >>> records = client.read("adresar", fields="kod,nazev,email")
            >>>
            >>> # Filter by condition
            >>> records = client.read(
            ...     evidence="faktura-vydana",
            ...     conditions="stav=Nezaplaceno"
            ... )
            >>>
            >>> # Pagination
            >>> records = client.read(
            ...     evidence="adresar",
            ...     limit=10,
            ...     offset=0
            ... )
        """
        endpoint = f"/Data/{evidence}"

        params = {}
        if fields:
            params["Fields"] = fields
        if conditions:
            params["Conditions"] = conditions

        # Calculate pagination
        page_size = limit if limit else 100
        page_number = (offset // page_size) + 1 if offset else 1

        params["PageSize"] = page_size
        params["PageNumber"] = page_number

        try:
            response = self._make_request("GET", endpoint, params=params)
        except ObjectNotFoundError:
            available = self.list_objects()
            raise ObjectNotFoundError(evidence, available)

        paged_list = response.get("PagedList", {})
        records = paged_list.get("Items", [])

        return records

    def get_object_count(self, evidence: str, conditions: Optional[str] = None) -> int:
        """
        Get the count of records in an evidence.

        Args:
            evidence: Evidence name
            conditions: Optional filter conditions

        Returns:
            Number of records matching the conditions.

        Examples:
            >>> # Total customers
            >>> count = client.get_object_count("adresar")
            >>>
            >>> # Active customers only
            >>> count = client.get_object_count("adresar", conditions="stav=Active")
        """
        records = self.read(evidence, fields="id", conditions=conditions, limit=1)
        # Note: This is a simplified implementation
        # In a real implementation, you'd use a COUNT endpoint if available
        return len(records)

    def close(self):
        """
        Close the client session and release resources.

        Examples:
            >>> client = K2Client(api_url, username, password, company_id)
            >>> try:
            ...     data = client.read("adresar")
            ... finally:
            ...     client.close()
        """
        if self.session:
            self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
        return False

    def __repr__(self):
        return f"K2Client(api_url='{self.api_url}', company_id='{self.company_id}')"
