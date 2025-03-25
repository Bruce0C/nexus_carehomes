import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
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


# Log user login
def log_user_login(SHEET, user):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    SHEET.append_row([timestamp, user, "LOGIN"])


# Get care homes
def get_care_homes():
    return ["Farehaven", "Tenville", "Brookway"]


# Select a service user
def get_service_users(care_home):
    return {"Farehaven": ["Mike", "Tom", "Donald"], "Tenville": ["Ed", "Alice", "Kyle"], "Brookway": ["Lisa", "Gen", "Allen"]}.get(care_home, [])


# Fetch schedule for a use
def get_schedule(service_user):
    return ["Breakfast", "Dr Appointment", "Medication", "Going for a walk", "Expecting visitor"]

# Track medication doses


def reset_daily_medication_log():
    return {"red": {}, "blue": {}, "green": {}}


daily_medication_log = reset_daily_medication_log()
allowed_medications = {
    "red": ["Alice", "Ed", "Donald"],
    "blue": ["Gen", "Allen", "Tom"],
    "green": ["Mike", "Ed", "Kyle"]
}

# Record medication administration


def administer_medication(SHEET, user_name, service_user, pill_color):
    if service_user not in allowed_medications[pill_color]:
        print(Fore.RED + f"{service_user} is not allowed to receive {pill_color} pills.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    max_doses_per_time = 2
    max_doses_per_day = 4

    if service_user not in daily_medication_log[pill_color]:
        daily_medication_log[pill_color][service_user] = 0

    if daily_medication_log[pill_color][service_user] >= max_doses_per_day:
        """
        Colorama used to change text colour
        """
        print(Fore.RED + "You have reached the daily maximum for this medication. Please do not give the service user anymore!")
        return

    dose = int(input(f"How many {pill_color} pills are being given? (Max {max_doses_per_time} at a time): "))

    if dose > max_doses_per_time:
        print(Fore.RED + "You cannot give more than 2 pills at a time!")
        return

    daily_medication_log[pill_color][service_user] += dose
    batch_data = [[timestamp, user_name, service_user, f"{dose} {pill_color} pill(s)", "Given"]]
    SHEET.append_rows(batch_data)

    print(Fore.GREEN + f"Recorded: {dose} {pill_color} pill(s) given to {service_user}.")


# Main application loop
def main():
    global daily_medication_log
    daily_medication_log = reset_daily_medication_log()
    Sheet = SHEET.user
    user_name = input("Enter your name: ")
    log_user_login(SHEET, user)
    care_homes = get_care_homes()
    print("Select a care home:")
    for idx, home in enumerate(care_homes, 1):
        print(f"{idx}. {home}")
    while True:
        try:
            care_home_choice = int(input("Enter choice: ")) - 1
            if care_home_choice < 0 or care_home_choice >= len(care_homes):
                print(Fore.RED + "Invalid selection. Please try again.")
                continue
            care_home = care_homes[care_home_choice]
            print(Fore.GREEN + f"You selected: {care_home}")
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
    
    service_users = get_service_users(care_home)
    print("Select a service user:")
    for idx, user in enumerate(service_users, 1):
        print(f"{idx}. {user}")
    while True:
        try:
            user_choice = int(input("Enter choice: ")) - 1
            if user_choice < 0 or user_choice >= len(service_users):
                print(Fore.RED + "Invalid selection. Please try again.")
                continue
            service_user = service_users[user_choice]
            print(Fore.GREEN + f"You selected: {service_user}")
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
    while True:
        print("\nOptions:")
        print("1. View Schedule")
        print("2. Complete a Task")
        print("3. Administer Medication")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice not in ["1", "2", "3", "4"]:
            print(Fore.RED + "Invalid choice. Try again.")
            continue
        if choice == "4":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
