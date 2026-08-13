import csv
import random
from datetime import date, timedelta

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

NUMBER_OF_SALES = 50000

OUTPUT_FILE = "data/sales.csv"

START_DATE = date(2026, 1, 1)
END_DATE = date(2026, 6, 30)

# -------------------------------------------------------
# Load customers
# -------------------------------------------------------

with open("data/customers.csv", "r", encoding="utf-8") as file:
    customers = list(csv.DictReader(file))

# -------------------------------------------------------
# Load products
# -------------------------------------------------------

with open("data/products.csv", "r", encoding="utf-8") as file:
    products = list(csv.DictReader(file))

# -------------------------------------------------------
# Load stores
# -------------------------------------------------------

with open("data/stores.csv", "r", encoding="utf-8") as file:
    stores = list(csv.DictReader(file))

# -------------------------------------------------------
# Generate sales data
# -------------------------------------------------------

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow([
        "sales_id",
        "order_date",
        "customer_id",
        "product_id",
        "store_id",
        "quantity",
        "unit_price",
        "discount"
    ])

    for sales_id in range(10001, 10001 + NUMBER_OF_SALES):

        # Random date
        days_difference = (END_DATE - START_DATE).days

        random_days = random.randint(
            0,
            days_difference
        )

        order_date = START_DATE + timedelta(
            days=random_days
        )

        # Random customer
        customer = random.choice(customers)

        # Random product
        product = random.choice(products)

        # Random store
        store = random.choice(stores)

        # Random quantity
        quantity = random.randint(1, 10)

        # Product price
        unit_price = float(product["unit_price"])

        # Random discount
        discount = random.choice([
            0,
            0,
            0,
            0.05,
            0.10,
            0.15
        ])

        writer.writerow([
            sales_id,
            order_date.isoformat(),
            customer["customer_id"],
            product["product_id"],
            store["store_id"],
            quantity,
            unit_price,
            discount
        ])

print(f"Generated {NUMBER_OF_SALES:,} sales records.")
print(f"Output file: {OUTPUT_FILE}")
