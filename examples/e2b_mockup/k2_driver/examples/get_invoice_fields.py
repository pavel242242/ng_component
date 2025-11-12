"""Example: Get field schema for issued invoices."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import K2Client
from dotenv import load_dotenv

load_dotenv()


def main():
    """Get and display field information for faktura-vydana (issued invoices)."""
    # Get credentials from environment
    api_url = os.getenv("K2_API_URL", "http://localhost:8000")
    username = os.getenv("K2_USERNAME", "demo")
    password = os.getenv("K2_PASSWORD", "demo")
    company_id = os.getenv("K2_COMPANY_ID", "demo")

    print("K2 Driver Example: Get Invoice Fields")
    print("=" * 50)

    # Create client
    with K2Client(api_url, username, password, company_id) as client:
        # Get fields for issued invoices
        fields = client.get_fields("faktura-vydana")

        print(f"\nFields in 'faktura-vydana' (Issued Invoices):\n")
        print(f"{'Field Name':<20} {'Type':<12} {'Required':<10} {'Read-Only':<10}")
        print("-" * 55)

        for field_name, field_props in fields.items():
            required = "Yes" if field_props.get("isRequired") else "No"
            readonly = "Yes" if field_props.get("isReadOnly") else "No"
            print(
                f"{field_name:<20} "
                f"{field_props['type']:<12} "
                f"{required:<10} "
                f"{readonly:<10}"
            )

    print("\n" + "=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
