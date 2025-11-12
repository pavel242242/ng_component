"""Exception classes for K2 driver."""


class K2Error(Exception):
    """Base exception for all K2 driver errors."""
    pass


class AuthenticationError(K2Error):
    """Raised when authentication fails."""
    def __init__(self, message="Authentication failed. Please check your username and password."):
        self.message = message
        super().__init__(self.message)


class ConnectionError(K2Error):
    """Raised when unable to connect to K2 API."""
    def __init__(self, message="Failed to connect to K2 API. Please check the API URL and network connectivity."):
        self.message = message
        super().__init__(self.message)


class ObjectNotFoundError(K2Error):
    """Raised when a K2 evidence (object) is not found."""
    def __init__(self, object_name: str, available_objects: list = None):
        self.object_name = object_name
        self.available_objects = available_objects or []

        message = f"Evidence '{object_name}' not found."
        if self.available_objects:
            suggestions = [obj for obj in self.available_objects if object_name.lower() in obj.lower()]
            if suggestions:
                message += f" Did you mean: {', '.join(suggestions)}?"
            else:
                message += f" Available evidences: {', '.join(self.available_objects[:5])}..."

        super().__init__(message)


class FieldNotFoundError(K2Error):
    """Raised when a field is not found in an evidence."""
    def __init__(self, field_name: str, evidence: str, available_fields: list = None):
        self.field_name = field_name
        self.evidence = evidence
        self.available_fields = available_fields or []

        message = f"Field '{field_name}' not found in evidence '{evidence}'."
        if self.available_fields:
            suggestions = [field for field in self.available_fields if field_name.lower() in field.lower()]
            if suggestions:
                message += f" Did you mean: {', '.join(suggestions)}?"
            else:
                message += f" Available fields: {', '.join(self.available_fields[:5])}..."

        super().__init__(message)


class QueryError(K2Error):
    """Raised when a query fails to execute."""
    def __init__(self, message="Query execution failed."):
        self.message = message
        super().__init__(self.message)


class RateLimitError(K2Error):
    """Raised when API rate limit is exceeded."""
    def __init__(self, retry_after: int = None):
        self.retry_after = retry_after
        message = "API rate limit exceeded."
        if retry_after:
            message += f" Please retry after {retry_after} seconds."
        super().__init__(message)


class ValidationError(K2Error):
    """Raised when data validation fails."""
    def __init__(self, message="Data validation failed."):
        self.message = message
        super().__init__(self.message)
