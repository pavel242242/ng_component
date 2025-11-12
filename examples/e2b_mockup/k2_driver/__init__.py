"""K2 REST API Driver.

A Python driver for K2 accounting/ERP software REST API.
"""

from .client import K2Client
from .exceptions import (
    K2Error,
    AuthenticationError,
    ConnectionError,
    ObjectNotFoundError,
    FieldNotFoundError,
    QueryError,
    RateLimitError,
    ValidationError,
)

__version__ = "1.0.0"
__all__ = [
    "K2Client",
    "K2Error",
    "AuthenticationError",
    "ConnectionError",
    "ObjectNotFoundError",
    "FieldNotFoundError",
    "QueryError",
    "RateLimitError",
    "ValidationError",
]
