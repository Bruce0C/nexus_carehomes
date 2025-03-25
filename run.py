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


def administer_medication(sheet, user_name, service_user, pill_color):
    """
    Record medication administration 
    """
    if service_user not in allowed_medications[pill_color]:
        print(Fore.RED + f"{service_user} is not allowed to receive {pill_color} pills.")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    max_doses_per_time = 2
    max_doses_per_day = 4
    
    if service_user not in daily_medication_log[pill_color]:
        daily_medication_log[pill_color][service_user] = 0
    
    if daily_medication_log[pill_color][service_user] >= max_doses_per_day:
        print(Fore.RED + "You have reached the daily maximum for this medication. Please do not give the service user anymore!")
        return

    dose = int(input(f"How many {pill_color} pills are being given? (Max {max_doses_per_time} at a time): "))
    if dose > max_doses_per_time:
        print(Fore.RED + "You cannot give more than 2 pills at a time!")
        return
    daily_medication_log[pill_color][service_user] += dose
    batch_data = [[timestamp, user_name, service_user, f"{dose} {pill_color} pill(s)", "Given"]]
    sheet.append_rows(batch_data) 
    print(Fore.GREEN + f"Recorded: {dose} {pill_color} pill(s) given to {service_user}.")
