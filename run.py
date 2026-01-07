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
colour = colorama.Fore

# print to test API function
# print(care_homes)
# print(medication)
# print(schedule)
# print(daily_notes)

# Log user


def log_user_login():
    """
    Log user name in spreadsheet.
    """
    # Determine the current hour
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f'{greeting}! Please enter your name to begin\n')

    name_str = input("Enter your name here: ")
    print('Name logged succesefully.\n')
    print(
        f"Welcome {name_str}. Please select a care home\n")
    return name_str  # Returns user name

# Update users worksheet to log user


def update_user_worksheet(name_str):
    """
    Update user name in spreadsheet.
    """
    user_worksheet = SHEET.worksheet('user')
    user_worksheet.append_row([name_str])


def get_care_homes():
    """
    Collects column of data from home worksheet,
    """
    homes = care_homes.col_values(1)
    return homes


def select_home():
    """
    This function displays care home options using data from the 'home'
     worksheet and returns the selected home name
    """


def access_home_sheet():
    """
    This function accesses and displays column-based service user data
    from the selected care home worksheet
    """


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


print("Welcome to nexus care homes work care assistant\n")
main()
