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

care_homes = SHEET.worksheet('care_home')
medication = SHEET.worksheet('medication')
schedule = SHEET.worksheet('schedule')
daily_notes = SHEET.worksheet('notes')
now = datetime.now()


# Log user login
def log_user_login():
    """
    Log user name in spreadsheet
    """
    print('Welcome to Nexus care homes, please enter your name to begin')

    name_str = input("Enter your name here: ")
    print(
        f"Hello {name_str}. Please select a the care home")


def update_user_worksheet(name_str):
    """
    Update user name in spreadsheet
    """
    print('Updating user name...\n')
    user_worksheet = SHEET.worksheet('user')
    user_worksheet.append_row(name_str)
    print('Name logged succesefully.\n')


log_user_login()
update_user_worksheet(log_user_login)
