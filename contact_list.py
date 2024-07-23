def add_contact(contacts, c_name, c_number, c_email):
    contact = {"name": c_name, "number": c_number, "email": c_email, "favorite": False}
    contacts.append(contact)
    print(f"You've created a new contact: {c_name}")
    return

def show_contacts(contacts):
    print(f"Contact list:\n")
    for i, contact in enumerate(contacts, start=1):
        status = "☆" if contact['favorite'] else ""
        contact_name = contact['name']
        print(f"{i}. [{status}] {contact_name}")
    return

def update_contats(contacts, index, new_c_name, new_c_number, new_c_email):
    real_index = int(index) - 1
    if real_index >= 0 and real_index < len(contacts):
        contacts[real_index]['name'] = new_c_name
        contacts[real_index]['number'] = new_c_number
        contacts[real_index]['email'] = new_c_email
        print(f'Contact was updated to {contacts[real_index]["name"]}')
    else:
        print('Invalid index. Try again!')
    return

def favorite_contact(contacts, index):
    real_index = int(index) - 1
    if real_index >= 0 and real_index < len(contacts):
        contacts[real_index]["favorite"] = True
    print(f'The contact {contacts[real_index]["name"]} becomes a favorite contact.')

def remove_contact(contacts, index):
    real_index = int(index) - 1
    if real_index >= 0 and real_index < len(contacts):
        del contacts[real_index]
    print('The contact has been deleted.')
    return

contacts = []

while True:
    print("\nContact menu selection:")
    print("1 - Add new contact")
    print("2 - Show contacts")
    print("3 - Update a contact")
    print("4 - Favorite a contact")
    print("5 - Delete contact")
    print("6 - Exit")

    choice = input('Choose an option: ')

    if choice == "1":
        c_name = input('Type contact name: ')
        c_number = input('Type contact number: ')
        c_email = input('Type contact email: ')
        add_contact(contacts, c_name, c_number, c_email)
    elif choice == "2":
        show_contacts(contacts)
    elif choice == "3":
        show_contacts(contacts)
        index = input('Enter the index number of the contact you want to update: ')
        new_c_name = input('Enter new contact name: ')
        new_c_number = input('Enter new contact number: ')
        new_c_email = input('Enter new contact email: ')
        update_contats(contacts, index, new_c_name, new_c_number, new_c_email)
    elif choice == "4":
        show_contacts(contacts)
        index = input('Enter the index number of the contact you want to change: ')
        favorite_contact(contacts, index)
    elif choice == "5":
        show_contacts(contacts)
        index = input('Enter the index of contact you want to delete: ')
        if input(f"You've shoure that want to delete this contact? (y or n) ") == 'y':
            remove_contact(contacts, index)
        else:
            True
    elif choice == "6":
        break
print("Exit succefully!")