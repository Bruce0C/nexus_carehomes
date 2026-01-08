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


def service_user_information():
    """
    This function lets the user to select
     one of three options notes, medication, or schedule
     for the service user.
    """


def main():
    """
    Run all program functions
    """
    name_str = log_user_login()  # Capture the returned name
    update_user_worksheet(name_str)  # Pass it to the next function
    get_care_homes()
    select_home()


print("Welcome to nexus care homes work care assistant\n")
main()
