import csv

# Initialize an empty list to store family history records
family_history = []

# Function to add a new family history record


def add_record():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    middle_name = input("Enter middle name: ")
    if not middle_name:
        middle_name = None

    birthday = input("Enter birthday: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    medical_history = input("Enter medical history: ")

    relatives = []  # Initialize a list to store relatives with their relationships

    # Ask for relative's name and relationship separately
    print("Enter relatives. For each one, provide the name followed by the relationship.")
    while True:
        relative_name = input(
            "Enter the relative's name (or leave blank to finish): ")
        if not relative_name:
            break
        relationship = input(
            "Enter your relationship to this relative (e.g., mother, father, cousin): ")

        # Combine the name and relationship as "Name (Relationship)"
        relative_entry = f"{relative_name} ({relationship})"
        relatives.append(relative_entry)

    # Join all relative entries with a comma
    relatives_string = ", ".join(relatives)

    record = {
        'First Name': first_name,
        'Last Name': last_name,
        'Middle Name': middle_name,
        'Birthday': birthday,
        'Address': address,
        'City': city,
        'State': state,
        'Medical History': medical_history,
        'Relatives': relatives_string,  # String of all relatives with their roles
    }

    family_history.append(record)
    print("\nRecord added successfully!")


# Function to search for family history records based on user input


def search_records():
    search_term = input(
        "Enter a search term (first name, last name, address, allergy, or relative): ")
    results = []

    for record in family_history:
        for key, value in record.items():
            if search_term.lower() in str(value).lower():
                results.append(record)
                break  # No need to add the same record multiple times

    if results:
        print("\nSearch results:")
        for result in results:
            for key, value in result.items():
                print(f"{key}: {value}")
            print()
    else:
        print("\nNo matching records found.")

# Function to save family history records to a CSV file


def save_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name', 'Middle Name', 'Birthday',
                      'Address', 'City', 'State', 'Medical History', 'Relatives']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in family_history:
            writer.writerow(record)

    print(f"\nRecords saved to {filename}")

# Function to display all family history records


def display_records():
    for record in family_history:
        print("\n")
        for key, value in record.items():
            print(f"{key}: {value}")


# Main program
print("Welcome to Family History Management System")
while True:
    print("\nOptions:")
    print("1. Add a new record")
    print("2. Search for records")
    print("3. Save records to a file")
    print("4. Display all records")
    print("5. Load records from a file")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_record()
    elif choice == '2':
        search_records()
    elif choice == '3':
        filename = input("Enter the file name to save the records: ")
        save_to_csv(filename)
    elif choice == '4':
        display_records()
    elif choice == '5':
        filename = input("Enter the file name to load records from: ")
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                family_history = list(reader)
            print(f"\nRecords loaded from {filename}")
        except FileNotFoundError:
            print(f"\nFile not found: {filename}")
    elif choice == '6':
        # Ask the user if they want to save before exiting
        save_on_exit = input(
            "Would you like to save the current records before exiting? (Y/N): ").strip().upper()
        if save_on_exit == 'Y':
            filename = input("Enter the file name to save the records: ")
            save_to_csv(filename)
        break
    else:
        print("\nInvalid choice. Please try again.")

print("\nGoodbye!")
