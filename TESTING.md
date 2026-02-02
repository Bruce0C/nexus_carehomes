# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation

| Directory | File | URL | Screenshot | 
| --- | --- | --- | --- | 
|  | [run.py](https://github.com/Bruce0C/nexus_carehomes/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Bruce0C/nexus_carehomes/main/run.py) | ![screenshot](assets/images/python_linter.jpeg) | 

## Defensive Programming
| Test Case | Feature | Expected Behaviour | Test Steps | Result | Fix | Screenshot
|----------|--------|-------------------|-----------|--------|-----|----|
| 1 | Validate user input for menu options in `select_home()` | Valid inputs (1, 2, 3, 0) navigate correctly. Invalid or non-numeric inputs show an error and re-prompt the user. | • Entered valid inputs (1, 2, 3, 0) <br> • Entered invalid inputs (4, -1, 100) <br> • Entered non-numeric inputs ("abc", "!@#", blank) | • Valid inputs navigated correctly or exited <br> • Invalid and non-numeric inputs displayed an error and re-prompted | No fixes required | ![screenshot](assets/images/invalid_and_valid_inputs.jpeg) |
| 2 | Handle missing or incorrect worksheet names in `service_user_information()` | If the worksheet does not exist, an error message is shown and the user can return to the previous menu. | • Tested with valid worksheet name ("farhaven") <br> • Tested with invalid worksheet name ("invalid_user") <br> • Tested with deleted worksheet | • Valid worksheet fetched and displayed correctly <br> • Invalid/missing worksheet displayed appropriate error message | No fixes required | ![screenshot](assets/images/worksheet_error_message.jpeg) |
| 3 | Enforce daily medication limits in `administer_medication()` | Maximum of 2 pills per type per day. Exceeding the limit shows a warning and prevents logging. | • Administered 1 red and 1 blue pill <br> • Attempted third red pill <br> • Attempted third blue pill | • First two pills administered successfully <br> • Third pill attempts blocked with warning message | No fixes required | ![screenshot](assets/images/medication_limit_message.jpeg) |
| 4 | Handle API errors in `view_daily_schedule()` | API errors display an error message and allow retry or return to the previous menu. | • Disconnected internet to simulate API error <br> • Used invalid worksheet name | • Error message displayed with details <br> • User allowed to retry or return | No fixes required |
| 5 | Graceful program exit in `select_home()` and `service_user_information()` | Selecting "Exit" displays a goodbye message and terminates the program gracefully. | • Selected Exit from care home menu <br> • Selected Exit from service user menu | Program displayed exit message and terminated without errors | No fixes required | ![screenshot](assets/images/exit_program.jpeg) |
| 6 | Handle invalid menu choices in `select_home()` and `select_service_user()` | Invalid or non-numeric menu choices display an error message and re-prompt the user. | • Entered valid inputs (1, 2, 3, 0) <br> • Entered invalid inputs (4, -1, 100) <br> • Entered non-numeric inputs ("abc", "!@#", blank) | • Valid inputs navigated correctly <br> • Invalid inputs showed appropriate error messages and re-prompted | No fixes required |

 ### Invalid User Inputs

- Feature: Validate user input for menu options in select_home()

**Expected:**
When the user enters a valid number (1, 2, 3, or 0), the program should proceed to the corresponding care home or exit the program.
If the user enters an invalid number or a non-numeric value, the program should display an error message and prompt the user again.

**Testing:** 
- Entered valid inputs (1, 2, 3, 0).
- Entered invalid inputs (e.g., 4, -1, 100).
- Entered non-numeric inputs (e.g., "abc", "!@#", or left the input blank).

**Result:**
- Valid inputs: The program correctly navigated to the selected care home or exited the program.
- Invalid inputs: The program displayed an error message and prompted the user again.
- Non-numeric inputs: The program displayed an error message and prompted the user again.
- Fix: No fixes were required as the feature behaved as expected.

 ### Missing or Incorrect Worksheet Names

**Feature:**
- Handle missing or incorrect worksheet names in service_user_information()

**Expected:**
If the worksheet for the selected service user does not exist, the program should display an error message and allow the user to return to the previous menu.

**Testing:**
- Tested with a valid worksheet name (e.g., "farhaven").
- Tested with an invalid worksheet name (e.g., "invalid_user").
- Tested with a missing worksheet (e.g., deleted the worksheet from Google Sheets).

**Result:**
- Valid worksheet name: The program successfully fetched and displayed the data.
Invalid or missing worksheet name: The program displayed the error message:
"Worksheet for [selected_user] not found. Please contact admin for further information."

**Fix:**
- No fixes were required as the feature behaved as expected.

 ### Handling Empty or Missing Data
**Feature:** 
-Handle empty or missing data in get_care_homes()

**Expected:**
- If the home worksheet is empty, the program should display a message indicating no care homes are available and return an empty list.

**Testing:**
- Tested with a populated home worksheet.
- Tested with an empty home worksheet (manually cleared all rows in the worksheet).

**Result:**
- Populated worksheet: The program displayed the care homes in a table format.
- Empty worksheet: The program displayed the message:
"No care homes found in the database." and returned an empty list.

**Fix:**
- No fixes were required as the feature behaved as expected.

### Handling Medication Limits

**Feature:** 
- Enforce daily medication limits in administer_medication()

**Expected:**
- The program should allow a maximum of 2 pills per type (e.g., red pill, blue pill) to be administered to a service user per day.
- If the daily limit is reached, the program should display a warning message and prevent further administration.

**Testing:**
- Administered 1 red pill and 1 blue pill to a service user.
- Attempted to administer a third red pill after reaching the daily limit.
- Attempted to administer a third blue pill after reaching the daily limit.

**Result:**
- First and second pills: The program successfully administered the pills and displayed a success message.
-Third pill: The program displayed the message:
"You have already administered the maximum of 2 red pills today." and did not update the medication log.

**Fix:**
- No fixes were required as the feature behaved as expected.

### Handling API Errors

**Feature:**
 - Handle API errors in view_daily_schedule()
 
**Expected:**
- If the Google Sheets API encounters an error (e.g., network issue, API limit), the program should display an error message and allow the user to retry or return to the previous menu.

**Testing:**
- Simulated an API error by disconnecting from the internet.
- Simulated an invalid worksheet name to trigger an API error.

**Result:**
- API error: The program displayed the message:
"An API error occurred while fetching the schedule: [error details]"
and allowed the user to retry or return to the previous menu.

**Fix:**
- No fixes were required as the feature behaved as expected.
 
### Handling Program Exit
**Feature:**
 - Graceful program exit in select_home() and service_user_information()

**Expected:**
- When the user selects the "Exit" option, the program should display a goodbye message and terminate gracefully.

**Testing:**
- Selected the "Exit" option from the care home menu.
- Selected the "Exit" option from the service user options menu.

**Result:**
- The program displayed the message:
"Exiting the program. Goodbye!"
and terminated without errors.

**Fix:**
- No fixes were required as the feature behaved as expected.

### Handling Invalid Menu Choices

**Feature:**

 - Handle invalid menu choices in `select_home()` and `select_service_user()`

**Expected:**
- If the user enters an invalid menu option, the program should display an error message and prompt the user again.

**Testing:**

- Entered valid menu options (e.g., 1, 2, 3, 0).
- Entered invalid menu options (e.g., 4, -1, 100).
- Entered non-numeric inputs (e.g., "abc", "!@#", or left the input blank).

**Result:**

- Valid inputs: The program navigated to the correct menu or exited as expected.
Invalid inputs: The program displayed the message:
"Invalid choice. Please enter 1, 2, 3, or 0."
and prompted the user again.
- Non-numeric inputs: The program displayed the message:
"Invalid input. Please enter a number (1, 2, 3, or 0)."
and prompted the user again.
Fix:

No fixes were required as the feature behaved as expected.



## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a caregiver | I want to log my username to the system | so that my activities can be tracked and recorded. |  ![screenshot](assets/images/log_username.jpeg) |
| As a caregiver  | I want to view a list of care homes | so that I can select the care home I am assigned to. |  ![screenshot](assets/images/care_home_list.jpeg) |
| As a caregiver  | I want to select my assigned care home | so that I can view the service users in that care home. |  ![screenshot](assets/images/care_home_select.jpeg) |
| As a caregiver  | I want to view a list of service users in my assigned care home | So that I can choose the service user I am responsible for.|  ![screenshot](assets/images/service_user_list.jpeg) |
| As a caregiver  | I want to select a specific service user | so that I can view their details and manage their information. |  ![screenshot](assets/images/service_user_select.jpeg) |
| As a caregiver  | I want to view detailed information about a service user | so that I can better understand their needs and provide appropriate care.|  ![screenshot](assets/images/service_user_info.jpeg) |
| As a caregiver  | I want to input notes about a service user | so that I can document important information about their care. |  ![screenshot](assets/images/input_notes.jpeg) |
| As a caregiver | I want to log the medication I administer to a service user | so that I can track the medication history and ensure compliance with dosage limits. |  ![screenshot](assets/images/administer_medication.jpeg) |
| As a caregiver| I want to view the daily schedule for a service user | so that I can plan my day and ensure all activities are completed on time. |  ![screenshot](assets/images/service_user_schedule.jpeg) |
| As a caregiver | I want to exit the program gracefully | so that I can end my session without losing any data. |  ![screenshot](assets/images/exit_program.jpeg) |
| As a caregiver | I want the program to handle invalid inputs | so that I can correct my mistakes without the program crashing. |  ![screenshot](assets/images/invalid_menu_choice.jpeg) |
| As a manager | I want all data to be stored in a centralized Google Sheet | so that I can monitor and analyze the activities of caregivers and service users. |  ![screenshot](assets/images/google_sheet.jpeg) |
| As a business owner | I want the system to support multiple care homes and service users | so that it can scale as my business grows. |  ![screenshot](assets/images/google_sheet.jpeg) |
| As a caregiver | I want the application to be simple and easy to use | so that I can quickly navigate and perform my tasks without confusion. | ![screenshot](assets/images/service_user_list.jpeg) |


## Bugs


### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Bruce0C/nexus_carehomes?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/Bruce0C/nexus_carehomes/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/Bruce0C/nexus_carehomes/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/Bruce0C/nexus_carehomes/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)


### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When using a helper `clear()` function, any text above the height of the terminal (24 lines) does not clear, and remains when scrolling up. | ![screenshot](documentation/issues/clear-scrolling.png) |
| The `colorama` terminal colors are fainter on Heroku when compared to the IDE locally. | ![screenshot](documentation/issues/colorama.png) |
| Emojis are cut-off when viewing the application from Firefox. | ![screenshot](documentation/issues/emojis.png) |
| The Python terminal doesn't work well with Safari, and sometimes uses cannot type in the application. | ![screenshot](documentation/issues/safari.png) |
| If a user types `CTRL`+`C` in the terminal on the live site, they can manually stop the application and receive and error. | ![screenshot](documentation/issues/ctrl-c.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

