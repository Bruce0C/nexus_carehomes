'''
This script serves as a digital assistant for managing care home operations.
It provides caregivers and managers with an efficient way to log activities,
access service user information, and manage data stored in Google Sheets.
'''
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# const to hold the untracked credentials file
CREDS = Credentials.from_service_account_file('creds.json')
# const to give scopes to the credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# const to authorize the gspread client with these scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# const to hold the full spreadsheet
SHEET = GSPREAD_CLIENT.open('nexuscare')

# vars to reference the individual worksheets of the full spreadsheet
care_homes = SHEET.worksheet('home')
medication = SHEET.worksheet('medication')
schedule = SHEET.worksheet('schedule')
daily_notes = SHEET.worksheet('notes')
f_names = SHEET.worksheet('farhaven')
t_names = SHEET.worksheet('tenville')
b_names = SHEET.worksheet('brookway')
now = datetime.now
colour = Fore

# print to test API function
# print(care_homes)
# print(medication)
# print(schedule)
# print(daily_notes)

# Log user


def log_user_login():
    """
    Log user name in user worksheet.
    """
    # Determine the current hour
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f'{Fore.GREEN}{greeting}{Style.RESET_ALL}! Please enter your name to'
          ' begin.\n')

    name_str = input("Enter your name here: ")
    print('\nName logged succesefully.\n')
    print(
        f"Welcome {Fore.GREEN}{name_str}{Style.RESET_ALL}. Please select a"
        " care home\n")
    return name_str  # Returns user name

# Update users worksheet to log user


def update_user_worksheet(name_str):
    """
    Update user name in spreadsheet.
    """
    user_worksheet = SHEET.worksheet('user')
    user_worksheet.append_row([name_str])

# Get care home names


def get_care_homes():
    """
    Collects column of data from home worksheet and prints it.
    """
    homes = care_homes.col_values(1)  # Fetches all values in the first column
    print("Care homes available:")
    for home in homes:
        # Print each care home name
        print(f"{Fore.LIGHTYELLOW_EX}{home}{Style.RESET_ALL}\n")
    return homes

# Select care home


def select_home():
    """
    This function displays care home options using data from the 'home'
    worksheet and returns the selected home name or ends the program.
    """
    print("Select a care home:\n")
    print("1. Farhaven")
    print("2. Tenville")
    print("3. Brookway")
    print("0. Exit\n")

    while True:
        try:
            choice = int(input("Enter your choice (1, 2, 3, or 0 to exit): "))
            if choice == 1:
                print("Farhaven selected.")
                # Fetch all values from Farhaven worksheet
                data = f_names.get_all_values()
                print("Service users living in Farhaven:")
                for row in data:
                    print(row)
                return f_names
            elif choice == 2:
                print("Tenville selected.")
                # Fetch all values from Tenville worksheet
                data = t_names.get_all_values()
                print("Service users living in Tenville :")
                for row in data:
                    print(row)
                return t_names
            elif choice == 3:
                print("Brookway selected.")
                # Fetch all values from Brookway worksheet
                data = b_names.get_all_values()
                print("Service users living in Brookway :")
                for row in data:
                    print(row)
                return b_names
            elif choice == 0:
                print("Exiting the program. Goodbye!")
                exit()  # Exit the program
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 0.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3, or 0).")

# Select service user


def select_service_user(selected_home):
    """
    Displays service users based on the selected home and allows the user
    to choose a service user or return to the care homes menu.
    """
    if selected_home == f_names:
        print("Select a service user from Farhaven:")
        service_users = ["Mike", "Donald", "Tom"]
    elif selected_home == t_names:
        print("Select a service user from Tenville:")
        service_users = ["Ed", "Alice", "Kyle"]
    elif selected_home == b_names:
        print("Select a service user from Brookway:")
        service_users = ["Lica", "Gen", "Alice"]
    else:
        print("Invalid home selected.")
        return

    print("Service users:")
    for idx, user in enumerate(service_users, start=1):
        print(f"{idx}. {user}")
    print("0. Return to care homes")

    while True:
        try:
            choice = int(
                input("Enter your choice (1, 2, 3, or 0 to return): "))
            if 1 <= choice <= len(service_users):
                print(f"You selected {service_users[choice - 1]}.")
                # You can add further functionality for the selected user here
                return service_users[choice - 1]
            elif choice == 0:
                print("Returning to care homes...")
                return select_home()  # Call the select_home function
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Service user information options


def service_user_information(selected_user, selected_home):
    """
    Fetches and displays data from the worksheet corresponding to the selected
    service user and allows the user to return to the
    service user selection menu.
    """
    print(f"Fetching information for {selected_user}...\n")

    try:
        # Open the worksheet corresponding to the selected user
        user_worksheet = SHEET.worksheet(selected_user.lower())
        # Fetch all data as a list of dictionaries
        data = user_worksheet.get_all_records()

        if not data:
            print(f"No data found in the worksheet for {selected_user}.")
        else:
            print(f"Information for {selected_user}:")
            for record in data:
                for key, value in record.items():
                    print(f"{key}: {value}")
                print("\n")  # Add a blank line between records

    except gspread.exceptions.WorksheetNotFound:
        print(
            f"Worksheet for {selected_user} not found. Please check the"
            " worksheet name.")

    while True:
        print("Options:")
        print("0. Exit the program")
        print("1. Input notes")
        print("2. Administer medication")
        print("3. View daily schedule")

        try:
            choice = int(input("Enter your choice (0, 1, 2, or 3): "))
            if choice == 0:
                print("Exiting the program. Goodbye!")
                sys.exit()  # Use sys.exit instead of exit
            elif choice == 1:
                print("Input notes selected.")
                note = input("Enter your note: ")
                # Append the note to the worksheet
                user_worksheet.append_row([note])
                print("Note added successfully.")
            elif choice == 2:
                print("Administer medication selected.")
                # Call the medication function
                print(
                    f"Administering medication for {selected_user} is not"
                    "implemented yet.")
                return
            elif choice == 3:
                print("View daily schedule selected.")
                # Open the "schedule" worksheet for the selected user
                schedule_worksheet = SHEET.worksheet(
                    f"{selected_user.lower()}_schedule")
                return view_daily_schedule(schedule_worksheet)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run all program functions


def main():
    """
    Run all program functions
    """
    name_str = log_user_login()  # Capture the returned name
    update_user_worksheet(name_str)  # Pass it to the next function
    get_care_homes()
    selected_home = select_home()
    selected_user = select_service_user(selected_home)
    service_user_information(selected_user, selected_home)


print(f"Welcome to {Fore.GREEN}Nexus Carehome{Style.RESET_ALL}, your digital"
      " assistant to help inform your working day!\n")
main()
