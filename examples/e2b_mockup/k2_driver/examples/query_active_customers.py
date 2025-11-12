"""Example: Query active customers from K2 address book."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import K2Client
from dotenv import load_dotenv

load_dotenv()


def main():
    """Query and display active customers."""
    # Get credentials from environment
    api_url = os.getenv("K2_API_URL", "http://localhost:8000")
    username = os.getenv("K2_USERNAME", "demo")
    password = os.getenv("K2_PASSWORD", "demo")
    company_id = os.getenv("K2_COMPANY_ID", "demo")

    print("K2 Driver Example: Query Active Customers")
    print("=" * 50)

    # Create client
    with K2Client(api_url, username, password, company_id) as client:
        # Query active customers from address book
        customers = client.read(
            evidence="adresar",
            fields="kod,nazev,email,telefon,mesto",
            conditions="stav=Active"
        )

        print(f"\nFound {len(customers)} active customers:\n")

        if customers:
            # Display header
            print(f"{'Code':<12} {'Name':<25} {'Email':<30} {'City':<15}")
            print("-" * 85)

            # Display customers
            for customer in customers:
                print(
                    f"{customer.get('kod', 'N/A'):<12} "
                    f"{customer.get('nazev', 'N/A'):<25} "
                    f"{customer.get('email', 'N/A'):<30} "
                    f"{customer.get('mesto', 'N/A'):<15}"
                )
        else:
            print("No active customers found.")

    print("\n" + "=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
