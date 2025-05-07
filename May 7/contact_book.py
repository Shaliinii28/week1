def load_contacts(filename):
    # Load contacts from file or create empty dictionary if file doesn't exist
    try:
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                name, phone = line.strip().split(',')
                contacts[name] = phone
            return contacts
    except FileNotFoundError:
        # Create new file if it doesn't exist
        with open(filename, 'w') as file:
            pass  # Create empty file
        return {}
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return {}

def save_contacts(filename, contacts):
    # Save contacts to file
    try:
        with open(filename, 'w') as file:
            for name, phone in contacts.items():
                file.write(f"{name},{phone}\n")
        print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")

def main():
    filename = "contacts.txt"
    contacts = load_contacts(filename)
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        
        choice = input("Choose (1-3): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            if name and phone:
                contacts[name] = phone
                save_contacts(filename, contacts)  # Save after adding
                print("Contact added and saved")
            else:
                print("Name and phone required")
                
        elif choice == '2':
            contacts = load_contacts(filename)  # Reload from file
            if contacts:
                print("\nContacts:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts found")
                
        elif choice == '3':
            save_contacts(filename, contacts)
            print("Contacts saved. Goodbye!")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()