"""Example: List all available K2 evidences (objects)."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import K2Client
from dotenv import load_dotenv

load_dotenv()


def main():
    """List all available K2 evidence types."""
    # Get credentials from environment
    api_url = os.getenv("K2_API_URL", "http://localhost:8000")
    username = os.getenv("K2_USERNAME", "demo")
    password = os.getenv("K2_PASSWORD", "demo")
    company_id = os.getenv("K2_COMPANY_ID", "demo")

    print("K2 Driver Example: List Evidences")
    print("=" * 50)

    # Create client
    with K2Client(api_url, username, password, company_id) as client:
        # Get all evidences
        evidences = client.list_objects()

        print(f"\nFound {len(evidences)} available evidences:\n")
        for evidence in evidences:
            print(f"  • {evidence}")

    print("\n" + "=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
