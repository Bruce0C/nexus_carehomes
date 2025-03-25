import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, init
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('nexuscare')

user = SHEET.worksheet('user')


def log_user_login(sheet, user_name):
    """
    User log in 
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, user_name, "LOGIN"])


def get_care_homes(sheet):
    """
    Get care home from sheet
    """
    return ["Farehaven", "Tenville", "Brookway"]


def get_service_users(care_home):
    """
    Select a service use
    """
    return {"Farehaven": ["Mike", "Tom", "Donald"], "Tenville": ["Ed", "Alice", "Kyle"], "Brookway": ["Lisa", "Gen", "Allen"]}.get(care_home, [])


def get_schedule(service_user):
    """
    Fetch the service user schedule
    """
    return ["Breakfast", "Dr Appointment", "Medication", "Going for a walk", "Expecting visitor"]


def reset_daily_medication_log():
    """
    Track medication dosage
    """
    return {"red": {}, "blue": {}, "green": {}}


daily_medication_log = reset_daily_medication_log()
allowed_medications = {
    "red": ["Alice", "Ed", "Donald"],
    "blue": ["Gen", "Allen", "Tom"],
    "green": ["Mike", "Ed", "Kyle"]
}
