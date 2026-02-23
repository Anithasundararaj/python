

contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available.")
        return
    
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    search_value = input("Enter Name or Phone Number to search: ").lower()
    
    found = False
    for contact in contacts:
        if search_value in contact["name"].lower() or search_value in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True
    
    if not found:
        print("Contact not found.")


def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").lower()
    
    for contact in contacts:
        if contact["name"].lower() == name:
            contact["phone"] = input("Enter new Phone Number: ")
            contact["email"] = input("Enter new Email: ")
            contact["address"] = input("Enter new Address: ")
            print("Contact updated successfully!")
            return
    
    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").lower()
    
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    
    print("Contact not found.")


def main():
    while True:
        print("\n==============================")
        print("   📒 Contact Management System")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please select from 1 to 6.")

main()