'''
This script serves as a digital assistant for managing care home operations.
It provides caregivers and managers with an efficient way to log activities,
access service user information, and manage data stored in Google Sheets.
'''

from datetime import datetime
import sys
from google.oauth2.service_account import Credentials
import gspread
from colorama import Fore, Style
from tabulate import tabulate

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

# daily_notes = SHEET.worksheet('notes')
f_names = SHEET.worksheet('farhaven')
t_names = SHEET.worksheet('tenville')
b_names = SHEET.worksheet('brookway')
now = datetime.now
colour = Fore

# Dictionary to track the number of pills administered per user
medication_log = {
    "red_pill": 0,
    "blue_pill": 0,
}

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

    print(f"{Fore.GREEN}{greeting}{Style.RESET_ALL}!"
          "Please enter your name to begin.")

    name_str = input(f"\n{Fore.YELLOW}Enter your name here:{Style.RESET_ALL} ")
    print(f'\n{Fore.GREEN}Name logged succesefully.{Style.RESET_ALL}')
    print(
        f"\nWelcome {Fore.GREEN}{name_str}{Style.RESET_ALL}.")
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
    Collects column of data from home worksheet and prints it in
    a simple_grid table format.
    """
    homes = care_homes.get_all_values()  # Fetches all rows as a list of lists

    # Prepare data for tabulate
    table_data = [[index + 1, row[0], row[1]]
                  for index, row in enumerate(homes) if len(row) >= 2]
    headers = [f"{Fore.CYAN}No.{Style.RESET_ALL}", f"{Fore.LIGHTYELLOW_EX}Care"
               "Home{Style.RESET_ALL}",
               f"{Fore.LIGHTYELLOW_EX}Address{Style.RESET_ALL}"]

    # Print the table in simple_grid format
    print("\nCare Homes Available:\n")
    print(tabulate(table_data, headers=headers, tablefmt="simple_grid"))

    return homes

# Select care home


def select_home():
    """
    This function displays care home options using data from the 'home'
    worksheet and returns the selected home name or ends the program.
    """
    print(f"{Fore.YELLOW}Select a care home:{Style.RESET_ALL}")
    print("0. Exit")
    print("1. Farhaven")
    print("2. Tenville")
    print("3. Brookway\n")

    while True:
        try:
            choice = int(input(
                f"{Fore.YELLOW}Enter your choice (1, 2, 3, or 0 to exit):"
                f"{Style.RESET_ALL} "))
            if choice == 1:
                print(f"{Fore.GREEN}\nFarhaven selected.{Style.RESET_ALL}")
                data = f_names.get_all_values()
                print("\nService users living in Farhaven:")
                # Extract the first row as headers
                headers = data[0]
                # Exclude the first row (headers) from the data
                data = data[1:]
                # Filter out empty rows
                data = [row for row in data if any(row)]
                # Prepare data for tabulate
                table_data = [[index + 1] +
                              row for index, row in enumerate(data)]
                # Print the table in simple_grid format
                print(tabulate(table_data, headers=headers, tablefmt="simple_"
                               "grid"))
                return f_names
            elif choice == 2:
                print(f"{Fore.GREEN}\nTenville selected.{Style.RESET_ALL}")
                data = t_names.get_all_values()
                print("\nService users living in Tenville:")
                # Extract the first row as headers
                headers = data[0]
                # Exclude the first row (headers) from the data
                data = data[1:]
                # Filter out empty rows
                data = [row for row in data if any(row)]
                # Prepare data for tabulate
                table_data = [[index + 1] +
                              row for index, row in enumerate(data)]
                # Print the table in simple_grid format
                print(tabulate(table_data, headers=headers, tablefmt="simple_"
                               "grid"))
                return t_names
            elif choice == 3:
                print(f"{Fore.GREEN}\nBrookway selected.{Style.RESET_ALL}")
                data = b_names.get_all_values()
                print("\nService users living in Brookway:")
                # Extract the first row as headers
                headers = data[0]
                # Exclude the first row (headers) from the data
                data = data[1:]
                # Filter out empty rows
                data = [row for row in data if any(row)]
                # Prepare data for tabulate
                table_data = [[index + 1] +
                              row for index, row in enumerate(data)]
                # Print the table in simple_grid format
                print(tabulate(table_data, headers=headers, tablefmt="simple_"
                               "grid"))
                return b_names
            elif choice == 0:
                print(f"{Fore.YELLOW}Exiting the program"
                      f"Goodbye!{Style.RESET_ALL}")
                sys.exit()  # Use sys.exit instead of exit
            else:
                print(f"\n{Fore.RED}Invalid choice."
                      f" Please enter 1, 2, 3, or 0.")
        except ValueError:
            print(
                f"\n{Fore.RED}Invalid input."
                f" Please enter a number (1, 2, 3, or 0).{Style.RESET_ALL}")

# Select service user


def select_service_user(selected_home):
    """
    Displays service users based on the selected home and allows the user
    to choose a service user or return to the care homes menu.
    """
    print("0. Return to care homes")
    if selected_home == f_names:
        print(
            f"\n{Fore.YELLOW}Select a service user"
            f"from Farhaven:{Style.RESET_ALL}")
        service_users = ["Mike", "Donald", "Tom"]
    elif selected_home == t_names:
        print(
            f"\n{Fore.YELLOW}Select a service user"
            f"from Tenville:{Style.RESET_ALL}")
        service_users = ["Ed", "Alice", "Kyle"]
    elif selected_home == b_names:
        print(
            f"\n{Fore.YELLOW}Select a service user"
            f"from Brookway:{Style.RESET_ALL}")
        service_users = ["Lica", "Gen", "Alice"]
    else:
        print(f"\n{Fore.RED}Invalid home selected.{Style.RESET_ALL}")
        return
    for idx, user in enumerate(service_users, start=1):
        print(f"{idx}. {user}")

    while True:
        try:
            choice = int(
                input(f"{Fore.YELLOW}Enter your choice"
                      f"(1, 2, 3, or 0 to return):{Style.RESET_ALL} "))
            if 1 <= choice <= len(service_users):
                print(
                    f"{Fore.YELLOW}\nYou selected "
                    f"{service_users[choice - 1]}.{Style.RESET_ALL}")
                # Return the selected service user or navigate back to
                # care homes menu
                return service_users[choice - 1]
            elif choice == 0:
                print(f"{Fore.YELLOW}\nReturning to "
                      f"care homes...{Style.RESET_ALL}")
                return select_home()  # Call the select_home function
            else:
                print(
                    f"{Fore.RED}\nInvalid choice."
                    f" Please select a valid option.\n{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\nInvalid input."
                  f"Please enter a number.\n{Style.RESET_ALL}")

# Service user information options


def service_user_information(selected_user):
    """
    Fetches and displays data from the worksheet corresponding to the selected
    service user and provides options to input notes, administer medication,
    view the daily schedule, or exit the program.
    """
    print(f"{Fore.GREEN}Fetching information "
          F"for {selected_user}...\n{Style.RESET_ALL}")

    try:
        # Open the worksheet corresponding to the selected user
        user_worksheet = SHEET.worksheet(selected_user.lower())
        # Fetch all data as a list of dictionaries
        data = user_worksheet.get_all_records()

        if not data:
            print(
                f"{Fore.GREEN}No data found in the worksheet "
                f"for {selected_user}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Information for"
                  f" {selected_user}:{Style.RESET_ALL}\n")
            for record in data:
                for key, value in record.items():
                    print(f"{key}: {value}")
                print("\n")  # Adds a blank line between records

    except gspread.exceptions.WorksheetNotFound:
        print(
            f"{Fore.GREEN}Worksheet for {selected_user} not found."
            f"Please check the contact admin for "
            f"further information.{Style.RESET_ALL}")

    while True:
        print("Options:")
        print("0. Exit the program")
        print("1. Input notes")
        print("2. Administer medication")
        print("3. View daily schedule\n")

        try:
            choice = int(input("Enter your choice (0, 1, 2, or 3): \n"))
            if choice == 0:
                print("Exiting the program. Goodbye!\n")
                sys.exit()  # Use sys.exit instead of exit
            elif choice == 1:
                print("Input notes selected.\n")
                note = input("Enter your note: ")
                # Append the note to the worksheet
                user_worksheet.append_row([note])
                print("Note added successfully.\n")
            elif choice == 2:
                print("Administer medication selected.")
                administer_medication(selected_user)
            elif choice == 3:
                print("View daily schedule selected.\n")
                # Open the "schedule" worksheet for the selected user
                schedule_worksheet = SHEET.worksheet(
                    f"{selected_user.lower()}_schedule")
                return view_daily_schedule(schedule_worksheet, selected_user)
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# View daily schedule


def view_daily_schedule(schedule_worksheet, selected_user):
    """
    Fetches and displays the daily schedule for the selected service user.
    """
    print("Fetching daily schedule...\n")
    try:
        # Fetch all data from the schedule worksheet
        schedule_data = schedule_worksheet.get_all_records()
        if not schedule_data:
            print("No schedule data found.\n")
        else:
            print("Daily Schedule:")
            for index, record in enumerate(schedule_data, start=1):
                print(f"Record {index}:")
                for key, value in record.items():
                    print(f"  {key}: {value}")
                print("\n")  # Add a blank line between records
    except gspread.exceptions.WorksheetNotFound:
        print("Schedule worksheet not found. Please check the worksheet"
              "name.\n")
    except gspread.exceptions.APIError as e:
        print(f"An API error occurred while fetching the schedule: {e}\n")
    except gspread.exceptions.GSpreadException as e:
        print(f"A GSpread error occurred while fetching the schedule: {e}\n")
    except (KeyError, ValueError) as e:
        print(f"A specific error occurred: {e}\n")

    # Return to the service user information menu
    service_user_information(selected_user)

# Administer medication


def administer_medication(selected_user):
    """
    Administers medication to the selected service user.
    The medications are a choice between the red pill and blue pill.
    Each pill can be administered a maximum of 2 times per day.
    """
    print(f"Administering medication for {selected_user}...\n")

    while True:
        print("Available medications:")
        print("1. Red Pill")
        print("2. Blue Pill")
        print("0. Exit\n")

        try:
            choice = int(
                input("Enter the number of the pill to administer: \n"))
            if choice == 0:
                print("Returning to service user information menu.\n")
                return  # Exit the function and return to the calling function
            elif choice == 1:
                if medication_log["red_pill"] < 2:
                    medication_log["red_pill"] += 1
                    print("1 Red pill administered successfully.\n")
                else:
                    print(
                        "You have already administered the maximum of "
                        "2 red pills today.")
            elif choice == 2:
                if medication_log["blue_pill"] < 2:
                    medication_log["blue_pill"] += 1
                    print("1 Blue pill administered successfully.\n")
                else:
                    print(
                        "You have already administered the maximum of"
                        " 2 blue pills today.\n")
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    # After the loop ends, return to the service_user_information function
    service_user_information(selected_user)


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
    service_user_information(selected_user)


# Greetings message
print(f"Welcome to {Fore.GREEN}Nexus Carehome{Style.RESET_ALL}!")
print("Your digital assistant to help inform your working day!\n")

# Run the program
main()
