"""Example: Full evidence discovery workflow."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import K2Client
from dotenv import load_dotenv

load_dotenv()


def main():
    """Demonstrate full evidence discovery workflow."""
    # Get credentials from environment
    api_url = os.getenv("K2_API_URL", "http://localhost:8000")
    username = os.getenv("K2_USERNAME", "demo")
    password = os.getenv("K2_PASSWORD", "demo")
    company_id = os.getenv("K2_COMPANY_ID", "demo")

    print("K2 Driver Example: Evidence Discovery Workflow")
    print("=" * 60)

    # Create client
    with K2Client(api_url, username, password, company_id) as client:
        # Step 1: List all evidences
        print("\nStep 1: Discovering available evidences...")
        evidences = client.list_objects()
        print(f"Found {len(evidences)} evidences: {', '.join(evidences)}")

        # Step 2: Get fields for first evidence
        if evidences:
            evidence_name = evidences[0]
            print(f"\nStep 2: Getting fields for '{evidence_name}'...")
            fields = client.get_fields(evidence_name)
            print(f"Found {len(fields)} fields:")
            for field_name in list(fields.keys())[:5]:
                field = fields[field_name]
                print(f"  • {field_name} ({field['type']})")
            if len(fields) > 5:
                print(f"  ... and {len(fields) - 5} more fields")

            # Step 3: Query sample data
            print(f"\nStep 3: Querying sample data from '{evidence_name}'...")
            records = client.read(evidence_name, limit=3)
            print(f"Retrieved {len(records)} records")

            if records:
                print("\nSample record:")
                for key, value in list(records[0].items())[:5]:
                    print(f"  {key}: {value}")
                if len(records[0]) > 5:
                    print(f"  ... and {len(records[0]) - 5} more fields")

            # Step 4: Get record count
            print(f"\nStep 4: Getting total record count...")
            # Note: This is simplified - real implementation would use COUNT
            print(f"Sample count: {len(records)} (limited to 3)")

    print("\n" + "=" * 60)
    print("Discovery complete!")


if __name__ == "__main__":
    main()
