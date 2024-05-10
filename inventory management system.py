class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            print("Item already exists in inventory. Updating quantity...")
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
            print("Item added to inventory.")

    def update_item(self, item_name, quantity=None, price=None):
        if item_name in self.inventory:
            if quantity is not None:
                self.inventory[item_name]['quantity'] = quantity
            if price is not None:
                self.inventory[item_name]['price'] = price
            print("Item updated successfully.")
        else:
            print("Item not found in inventory.")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print("Item removed from inventory.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory Status:")
            print("Item Name\tQuantity\tPrice")
            for item_name, details in self.inventory.items():
                print(f"{item_name}\t\t{details['quantity']}\t\t{details['price']}")


def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add New Item")
        print("2. Update Existing Item")
        print("3. Remove Item")
        print("4. Display Inventory Status")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.add_item(item_name, quantity, price)

        elif choice == '2':
            item_name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity (or leave blank to skip): ") or '0')
            price = float(input("Enter new price (or leave blank to skip): ") or '0')
            inventory.update_item(item_name, quantity, price)

        elif choice == '3':
            item_name = input("Enter item name to remove: ")
            inventory.remove_item(item_name)

        elif choice == '4':
            inventory.display_inventory()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

 