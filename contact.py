contacts = {}

def add_contact():
    print("Add a new contact:")
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact {name} added successfully!")

def view_contact_list():
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"{name}: {details['Phone']}")

def search_contact():
    query = input("Enter the name or phone number to search: ")
    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details['Phone']:
            print("\nContact Details:")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            return
    print(f"No contact found for '{query}'.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact: {name}")
        phone = input("Enter the new phone number (press Enter to keep existing): ")
        email = input("Enter the new email address (press Enter to keep existing): ")
        address = input("Enter the new address (press Enter to keep existing): ")
        
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        
        print(f"Contact {name} updated successfully!")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}.")

def main():
    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
