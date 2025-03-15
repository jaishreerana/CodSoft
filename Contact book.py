# Simple Contact Management System
contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print(f"Contact {name} added!")

    elif choice == "2":
        if not contacts:
            print("No contacts saved.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"{search}: {contacts[search]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print(f"Contact {delete} deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
