# Supply Chain Intelligence System
# Electronics Store Inventory

inventory = {
    "Resistor": {
        "stock": 500,
        "price": 2.00,
        "minimum_stock": 100
    },
    "Capacitor": {
        "stock": 35,
        "price": 5.00,
        "minimum_stock": 50
    },
    "LED": {
        "stock": 12,
        "price": 3.00,
        "minimum_stock": 50
    },
    "Arduino": {
        "stock": 80,
        "price": 750.00,
        "minimum_stock": 20
    }
}


def display_inventory():
    print("\n========== INVENTORY ==========")

    for item, details in inventory.items():
        stock = details["stock"]
        price = details["price"]
        minimum = details["minimum_stock"]

        if stock <= minimum:
            status = "⚠ LOW STOCK"
        else:
            status = "OK"

        print(
            f"{item:12} | "
            f"Stock: {stock:4} | "
            f"Price: ₹{price:7.2f} | "
            f"{status}"
        )


def check_low_stock():
    print("\n========== LOW STOCK ALERTS ==========")

    low_stock_found = False

    for item, details in inventory.items():
        if details["stock"] <= details["minimum_stock"]:
            print(
                f"⚠ {item} is low in stock "
                f"({details['stock']} remaining)."
            )
            low_stock_found = True

    if not low_stock_found:
        print("All items have sufficient stock.")


def add_stock():
    item = input("\nEnter the component name: ")

    if item not in inventory:
        print("Item not found.")
        return

    amount = int(input("Enter quantity to add: "))

    inventory[item]["stock"] += amount

    print(
        f"{amount} {item}(s) added. "
        f"New stock: {inventory[item]['stock']}"
    )


def remove_stock():
    item = input("\nEnter the component name: ")

    if item not in inventory:
        print("Item not found.")
        return

    amount = int(input("Enter quantity removed/sold: "))

    if amount > inventory[item]["stock"]:
        print("Not enough stock available.")
    else:
        inventory[item]["stock"] -= amount

        print(
            f"{amount} {item}(s) removed. "
            f"Remaining stock: {inventory[item]['stock']}"
        )


def search_item():
    item = input("\nEnter the component you want to search for: ")

    if item in inventory:
        details = inventory[item]

        print("\n========== ITEM INFORMATION ==========")
        print(f"Component: {item}")
        print(f"Stock: {details['stock']}")
        print(f"Price: ₹{details['price']:.2f}")
        print(f"Minimum Stock: {details['minimum_stock']}")

        if details["stock"] <= details["minimum_stock"]:
            print("Status: ⚠ LOW STOCK")
        else:
            print("Status: OK")

    else:
        print("Item not found.")


def reorder_recommendations():
    print("\n========== REORDER RECOMMENDATIONS ==========")

    found = False

    for item, details in inventory.items():

        if details["stock"] <= details["minimum_stock"]:

            # Suggest ordering enough to reach 2 × minimum stock
            recommended_order = (
                details["minimum_stock"] * 2
                - details["stock"]
            )

            estimated_cost = (
                recommended_order * details["price"]
            )

            print(f"\n{item}")
            print(f"Current stock: {details['stock']}")
            print(f"Recommended order: {recommended_order}")
            print(f"Estimated cost: ₹{estimated_cost:.2f}")

            found = True

    if not found:
        print("No items currently need to be reordered.")


def main():

    while True:

        print("\n======================================")
        print("   SUPPLY CHAIN INTELLIGENCE SYSTEM")
        print("======================================")

        print("1. View inventory")
        print("2. Check low-stock alerts")
        print("3. Add stock")
        print("4. Remove/sell stock")
        print("5. Search for an item")
        print("6. Reorder recommendations")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            display_inventory()

        elif choice == "2":
            check_low_stock()

        elif choice == "3":
            add_stock()

        elif choice == "4":
            remove_stock()

        elif choice == "5":
            search_item()

        elif choice == "6":
            reorder_recommendations()

        elif choice == "7":
            print("\nExiting system...")
            break

        else:
            print("Invalid choice. Please try again.")


main()