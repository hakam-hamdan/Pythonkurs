# Customer Management System (English Version)

import json
import os

DATA_FILE = "customers.json"

def load_customers():
    """Load customer data from JSON file if exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # JSON keys are strings -> convert to int
                return {int(cid): info for cid, info in data.items()}
            except json.JSONDecodeError:
                print("Error reading JSON file. Starting with empty list.")
                return {}
    return {}

def save_customers(customers):
    """Save customers dict to file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({str(cid): info for cid, info in customers.items()}, f, ensure_ascii=False, indent=2)

def generate_new_id(customers):
    """Return next available ID."""
    if not customers:
        return 1
    return max(customers.keys()) + 1

def add_customer(customers):
    print("\n--- Add New Customer ---")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()

    new_id = generate_new_id(customers)
    customers[new_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }
    save_customers(customers)
    print(f"Customer added successfully. Assigned ID: {new_id}")

def update_customer(customers):
    print("\n--- Update Customer Information ---")
    try:
        cid = int(input("Enter Customer ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    if cid not in customers:
        print("Customer not found.")
        return

    customer = customers[cid]
    print("Press Enter to keep the current value.")
    print("Current First Name:", customer["first_name"])
    first_name = input("New First Name: ").strip() or customer["first_name"]
    print("Current Last Name:", customer["last_name"])
    last_name = input("New Last Name: ").strip() or customer["last_name"]
    print("Current Email:", customer["email"])
    email = input("New Email: ").strip() or customer["email"]
    print("Current Phone:", customer["phone"])
    phone = input("New Phone: ").strip() or customer["phone"]

    customers[cid] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }
    save_customers(customers)
    print("Customer information updated.")

def delete_customer(customers):
    print("\n--- Delete Customer ---")
    try:
        cid = int(input("Enter Customer ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    if cid not in customers:
        print("Customer not found.")
        return

    confirm = input(f"Are you sure you want to delete {customers[cid]['first_name']}? (y/n): ").strip().lower()
    if confirm == "y":
        del customers[cid]
        save_customers(customers)
        print("Customer deleted.")
    else:
        print("Deletion canceled.")

def show_customers(customers):
    print("\n--- Customer List ---")
    if not customers:
        print("No customers found.")
        return
    for cid, info in customers.items():
        print(f"[{cid}] {info['first_name']} {info['last_name']} | Email: {info['email']} | Phone: {info['phone']}")

def main_menu():
    customers = load_customers()
    while True:
        print("\n======== Customer Management System ========")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. List All Customers")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_customer(customers)
        elif choice == "2":
            update_customer(customers)
        elif choice == "3":
            delete_customer(customers)
        elif choice == "4":
            show_customers(customers)
        elif choice == "0":
            print("Saving data and exiting... Goodbye!")
            save_customers(customers)
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()






    

