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

user_list = SHEET.worksheet('user')
care_homes = SHEET.worksheet('care_home')
medication = SHEET.worksheet('medication')
schedule = SHEET.worksheet('schedule')
daily_notes = SHEET.worksheet('notes')

names = user_list.get_all_values()
home = care_homes.get_all_values()
dosage = medication.get_all_values()
activities = schedule.get_all_values()
notes = daily_notes.get_all_values()

# Log user login


def log_user_login(SHEET, user):
    """
    ...
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    SHEET.append_row([timestamp, user, "LOGIN"])

# LOG USER
# CARE HOMES
# Select service user
# Daily schedule
# Track medication
# Record medication administration
# Main Application loop
