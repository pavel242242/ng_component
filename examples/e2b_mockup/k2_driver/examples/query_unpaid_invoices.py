"""Example: Query unpaid invoices from K2."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import K2Client
from dotenv import load_dotenv

load_dotenv()


def main():
    """Query and display unpaid invoices."""
    # Get credentials from environment
    api_url = os.getenv("K2_API_URL", "http://localhost:8000")
    username = os.getenv("K2_USERNAME", "demo")
    password = os.getenv("K2_PASSWORD", "demo")
    company_id = os.getenv("K2_COMPANY_ID", "demo")

    print("K2 Driver Example: Query Unpaid Invoices")
    print("=" * 50)

    # Create client
    with K2Client(api_url, username, password, company_id) as client:
        # Query unpaid invoices
        invoices = client.read(
            evidence="faktura-vydana",
            fields="id,kod,nazev,datum,castka,firma,splatnost",
            conditions="stav=Nezaplaceno"
        )

        print(f"\nFound {len(invoices)} unpaid invoices:\n")

        if invoices:
            # Display header
            print(f"{'Code':<12} {'Amount':<12} {'Due Date':<12} {'Customer':<15}")
            print("-" * 55)

            # Display invoices
            total = 0
            for invoice in invoices:
                print(
                    f"{invoice.get('kod', 'N/A'):<12} "
                    f"{invoice.get('castka', 0):>10.2f}  "
                    f"{invoice.get('splatnost', 'N/A'):<12} "
                    f"{invoice.get('firma', 'N/A'):<15}"
                )
                total += float(invoice.get('castka', 0))

            print("-" * 55)
            print(f"{'Total:':<12} {total:>10.2f}")
        else:
            print("No unpaid invoices found.")

    print("\n" + "=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
