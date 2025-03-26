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
def log_user_login():
    """
    Log user name in spreadsheet
    """
    print('Welcome to Nexus care homes, please enter your name to log in: ')


# Get care home
def get_care_homes():

    # Select care home


def get_care_homes(care_home):
    """
    ...
    """

# Select service user


def get_service_users(care_home):
    """
    ...
    """

# Daily schedule


def get_schedule(user):
    """
    ...
    """

# Track medication


def reset_daily_medication_log():
    """
    ...
    """

# Record medication administration


def administer_medication():
    """
    ...
    """


# Main Application loop
def main():
    """
    ...
    """
