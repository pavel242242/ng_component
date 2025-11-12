"""Test K2 API connection and credentials."""

import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from client import K2Client
from exceptions import K2Error, AuthenticationError, ConnectionError


def test_connection(api_url: str, username: str, password: str, company_id: str) -> bool:
    """
    Test connection to K2 API.

    Args:
        api_url: K2 API base URL
        username: K2 username
        password: K2 password
        company_id: Company identifier

    Returns:
        True if connection successful, False otherwise
    """
    print(f"Testing connection to K2 API...")
    print(f"API URL: {api_url}")
    print(f"Company ID: {company_id}")
    print(f"Username: {username}")
    print("-" * 50)

    try:
        # Initialize client (validates connection)
        client = K2Client(
            api_url=api_url,
            username=username,
            password=password,
            company_id=company_id,
            debug=True,
        )

        print("\n✓ Connection successful!")
        print("\nTesting API functionality...")

        # Test list_objects
        print("\n1. Listing available evidences...")
        evidences = client.list_objects()
        print(f"   Found {len(evidences)} evidences:")
        for evidence in evidences:
            print(f"   - {evidence}")

        # Test get_fields with first evidence
        if evidences:
            first_evidence = evidences[0]
            print(f"\n2. Getting fields for '{first_evidence}'...")
            fields = client.get_fields(first_evidence)
            print(f"   Found {len(fields)} fields:")
            for field_name, field_props in list(fields.items())[:5]:
                print(f"   - {field_name}: {field_props['type']}")
            if len(fields) > 5:
                print(f"   ... and {len(fields) - 5} more fields")

            # Test read
            print(f"\n3. Reading data from '{first_evidence}'...")
            records = client.read(first_evidence, limit=3)
            print(f"   Retrieved {len(records)} records")
            if records:
                print(f"   Sample record keys: {list(records[0].keys())[:5]}")

        print("\n" + "=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)

        client.close()
        return True

    except AuthenticationError as e:
        print(f"\n✗ Authentication failed: {e}")
        print("   Please check your username and password.")
        return False

    except ConnectionError as e:
        print(f"\n✗ Connection failed: {e}")
        print("   Please check:")
        print("   - API URL is correct")
        print("   - Network connectivity")
        print("   - K2 server is running")
        return False

    except K2Error as e:
        print(f"\n✗ K2 API error: {e}")
        return False

    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run connection test with command line arguments or defaults."""
    import os
    from dotenv import load_dotenv

    load_dotenv()

    # Get credentials from environment or command line
    api_url = os.getenv("K2_API_URL", "http://localhost:8000")
    username = os.getenv("K2_USERNAME", "demo")
    password = os.getenv("K2_PASSWORD", "demo")
    company_id = os.getenv("K2_COMPANY_ID", "demo")

    # Allow command line override
    if len(sys.argv) > 1:
        api_url = sys.argv[1]
    if len(sys.argv) > 2:
        username = sys.argv[2]
    if len(sys.argv) > 3:
        password = sys.argv[3]
    if len(sys.argv) > 4:
        company_id = sys.argv[4]

    success = test_connection(api_url, username, password, company_id)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
