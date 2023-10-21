import json

# Initialize an empty contacts list
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email})
    save_contacts()

# Function to view all contacts
def view_contacts():
    if contacts:
        for contact in contacts:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("-" * 20)
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact(query):
    matching_contacts = [contact for contact in contacts if query.lower() in contact["Name"].lower()]
    if matching_contacts:
        for contact in matching_contacts:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("-" * 20)
    else:
        print("No matching contacts found.")

# Function to delete a contact
def delete_contact(query):
    global contacts
    contacts = [contact for contact in contacts if query.lower() not in contact["Name"].lower()]
    save_contacts()

# Function to save contacts to a JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Load contacts from the JSON file
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []

while True:
    print("\nContact App")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter a name to search for: ")
        search_contact(query)
    elif choice == "4":
        query = input("Enter a name to delete: ")
        delete_contact(query)
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")
1