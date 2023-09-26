import datetime

# Arrays to store contact and meeting information
contacts = []
meetings = []

# Function to display the main menu
def display_main_menu():
    print("UZ University Projects Diary")
    print("1. Contact Details")
    print("2. Meetings/Appointments")
    print("3. Exit")

# Function to display the contact submenu
def display_contact_submenu():
    print("Contact Details")
    print("1. Add New Contact")
    print("2. Delete Contact")
    print("3. Edit Contact")
    print("4. Search Contact")
    print("5. Go Back")

# Function to display the meetings/appointments submenu
def display_meetings_submenu():
    print("Meetings/Appointments")
    print("1. Add New Meeting")
    print("2. Delete Meeting")
    print("3. Edit Meeting")
    print("4. Search Meeting")
    print("5. Go Back")

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = {
        "name": name,
        "address": address,
        "phone_number": phone_number,
        "email": email
    }
    contacts.append(contact)
    print("Contact added successfully!")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter the name or email of the contact you want to delete: ")
    found_contacts = search_contacts(search_term)
    if len(found_contacts) > 0:
        print("Multiple contacts found. Please select the contact to delete:")
        display_contacts(found_contacts)
        choice = int(input("Enter the index of the contact to delete: "))
        if choice >= 0 and choice < len(found_contacts):
            contacts.remove(found_contacts[choice])
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")
    else:
        print("No contacts found.")

# Function to edit a contact
def edit_contact():
    search_term = input("Enter the name or email of the contact you want to edit: ")
    found_contacts = search_contacts(search_term)
    if len(found_contacts) > 0:
        print("Multiple contacts found. Please select the contact to edit:")
        display_contacts(found_contacts)
        choice = int(input("Enter the index of the contact to edit: "))
        if choice >= 0 and choice < len(found_contacts):
            contact = found_contacts[choice]
            name = input("Enter the updated name: ")
            address = input("Enter the updated address: ")
            phone_number = input("Enter the updated phone number: ")
            email = input("Enter the updated email address: ")
            contact["name"] = name
            contact["address"] = address
            contact["phone_number"] = phone_number
            contact["email"] = email
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contacts(search_term):
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term.lower() in contact["email"].lower():
            found_contacts.append(contact)
    return found_contacts

# Function to display contacts
def display_contacts(contacts_list):
    for i, contact in enumerate(contacts_list):
        print(f"{i}. {contact['name']}, {contact['email']}")

# Function to add a new meeting
def add_meeting():
    date = input("Enter the date (YYYY-MM-DD): ")
    time = input("Enter the time: ")
    location = input("Enter the location: ")
    meeting = {
        "date": date,
        "time": time,
        "location": location
    }
    meetings.append(meeting)
    print("Meeting added successfully!")

# Function to delete a meeting
def delete_meeting():
    search_term = input("Enter the date or location of the meeting you want to delete: ")
    found_meetings = search_meetings(search_term)
    if len(found_meetings) > 0:
        print("Multiple meetings found. Please select the meeting to delete:")
        display_meetings(found_meetings)
        choice = int(input("Enter the index of the meeting to delete: "))
        if choice >= 0 and choice < len(found_meetings):
            meetings.remove(found_meetings[choice])
            print("Meeting deleted successfully!")
        else:
            print("Invalid meeting index.")
    else:
        print("No meetings found.")

# Function to edit a meeting
def edit_meeting():
    search_term = input("Enter the date or location of the meeting you want to edit: ")
    found_meetings = search_meetings(search_term)
    if len(found_meetings) > 0:
        print("Multiple meetings found. Please select the meeting to edit:")
        display_meetings(found_meetings)
        choice = int(input("Enter the index of the meeting to edit: "))
        if choice >= 0 and choice < len(found_meetings):
            meeting = found_meetings[choice]
            date = input("Enter the updated date (YYYY-MM-DD): ")
            time = input("Enter the updated time: ")
            location = input("Enter the updated location: ")
            meeting["date"] = date
            meeting["time"] = time
            meeting["location"] = location
            print("Meeting updated successfully!")
        else:
            print("Invalid meeting index.")
    else:
        print("No meetings found.")

# Function to search for a meeting
def search_meetings(search_term):
    found_meetings = []
    for meeting in meetings:
        if search_term.lower() in meeting["date"].lower() or search_term.lower() in meeting["location"].lower():
            found_meetings.append(meeting)
    return found_meetings

# Function to display meetings
def display_meetings(meetings_list):
    for i, meeting in enumerate(meetings_list):
        print(f"{i}. {meeting['date']}, {meeting['location']}")

# Function to display reminders for meetings/appointments
def display_reminders():
    current_date = datetime.date.today()
    for meeting in meetings:
        meeting_date = datetime.datetime.strptime(meeting["date"], "%Y-%m-%d").date()
        if meeting_date == current_date:
            print(f"Reminder: Meeting on {meeting['date']} at {meeting['time']} in {meeting['location']}")

# Main program flow
while True:
    display_main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            display_contact_submenu()
            contact_choice = input("Enter your choice: ")

            if contact_choice == "1":
                add_contact()
            elif contact_choice == "2":
                delete_contact()
            elif contact_choice == "3":
                edit_contact()
            elif contact_choice == "4":
                search_term = input("Enter the name or email of the contact you want to search: ")
                found_contacts = search_contacts(search_term)
                if len(found_contacts) > 0:
                    print("Search Results:")
                    display_contacts(found_contacts)
                else:
                    print("No contacts found.")
            elif contact_choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            display_meetings_submenu()
            meetings_choice = input("Enter your choice: ")

            if meetings_choice == "1":
                add_meeting()
            elif meetings_choice == "2":
                delete_meeting()
            elif meetings_choice == "3":
                edit_meeting()
            elif meetings_choice == "4":
                search_term = input("Enter the date or location of the meeting you want to search: ")
                found_meetings = search_meetings(search_term)
                if len(found_meetings) > 0:
                    print("Search Results:")
                    display_meetings(found_meetings)
                else:
                    print("No meetings found.")
            elif meetings_choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")

    print("\n")

# Display reminders for meetings/appointments
display_reminders()