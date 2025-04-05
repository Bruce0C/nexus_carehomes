from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('nexuscare')

care_homes = SHEET.worksheet('home')
medication = SHEET.worksheet('medication')
schedule = SHEET.worksheet('schedule')
daily_notes = SHEET.worksheet('notes')
now = datetime.now
colour = colorama.Fore

# Log user login


def log_user_login():
    """
    Log user name in spreadsheet.
    """
    print('Please enter your name to begin')

    name_str = input("Enter your name here: ")
    print(
        f"Hello {name_str}. Please select a the care home")


def update_user_worksheet(name_str):
    """
    Update user name in spreadsheet.
    """
    print('Updating user name...\n')
    user_worksheet = SHEET.worksheet('user')
    user_worksheet.append_row(name_str)
    print('Name logged succesefully.\n')


def get_care_homes():
    """
    Collects column of data from home worksheet,
    """
    home = SHEET.worksheet("home")

    columns = []
    for ind in range(1, 7):
        column = home.col_values(ind)
        columns.append(column[-5:])

    return columns


def select_home():
    """
    This function displays care home options using data from the 'home'
     worksheet and returns the selected home name
    """
    care_home_columns = get_care_homes()
    # Take names from first row of each of the first 3 columns
    care_home_names = [col[0] for col in care_home_columns[:3]]

    print("Select a care home:")
    for i, name in enumerate(care_home_names, start=1):
        print(f"{i}. {name}")

    while True:
        choice = input("Enter option (1, 2, or 3): ").strip()
        if choice in {"1", "2", "3"}:
            selected_home = care_home_names[int(choice) - 1]
            print(f"You selected: {selected_home}")
            return selected_home
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def access_home_sheet(home_name):
    """
    This function accesses and displays column-based service user data
    from the selected care home worksheet
    """
    worksheet = SHEET.worksheet(home_name)

    columns = []
    for i in range(1, worksheet.col_count + 1):
        column = worksheet.col_values(i)
        if column:  # Ignore empty columns
            columns.append(column)

    print(Fore.GREEN + "Access granted")
    print("The service users in this care home are...")

    for col in columns:
        print(", ".join(col))

    return worksheet


def main():
    """
    Run all program functions
    """
    log_user_login()
    update_user_worksheet(log_user_login)
    get_care_homes()
    select_home()
    access_home_sheet(home_name)


print("Welcome to nexus care homes work care assistant")
main()
