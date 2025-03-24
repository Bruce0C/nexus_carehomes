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
home = SHEET.worksheet('home')
medication = SHEET.worksheet('medication')
schedule = SHEET.worksheet('schedule')