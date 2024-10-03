# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ").strip().title()
    if name in contacts:
        print(f"Contact with name {name} already exists.")
    else:
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        contacts[name] = {'Phone': phone, 'Email': email}
        print(f"Contact {name} added successfully.")

# Function to edit a contact
def edit_contact():
    name = input("Enter the name of the contact you want to edit: ").strip().title()
    if name in contacts:
        print(f"Editing contact: {name}")
        print(f"Current details: Phone: {contacts[name]['Phone']}, Email: {contacts[name]['Email']}")
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()

        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ").strip().title()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Delete operation cancelled.")
    else:
        print(f"Contact {name} not found.")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print("No contacts available.")

# Main menu
def contact_book():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            view_contacts()
        elif choice == '5':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the contact book
contact_book()
