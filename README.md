# [Nexus Carehomes](https://nexus-care-e0ddbf0b6681.herokuapp.com)

Developer: Bruce Chibisa ([Bruce0C](https://www.github.com/Bruce0C))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Bruce0C/nexus_carehomes)](https://www.github.com/Bruce0C/nexus_carehomes/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Bruce0C/nexus_carehomes)](https://www.github.com/Bruce0C/nexus_carehomes/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Bruce0C/nexus_carehomes)](https://www.github.com/Bruce0C/nexus_carehomes)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://nexus-care-e0ddbf0b6681.herokuapp.com)

![screenshot](documentation/mockup.png)

source: [nexus_carehomes amiresponsive](https://ui.dev/amiresponsive?url=https://nexus-care-e0ddbf0b6681.herokuapp.com)


## UX

**The 5 Planes of UX**



**1. Strategy**

**Purpose**
- Provide care givers simple and effective way to log service user activities and help with documentation.
- Help users optimize working day by reducing the amount of physical paperwork by using their devices to quiclkly take notes.
- Display information a care giver may find helpful about their working day.
- Add any input to a spreadsheet, this would aid manager and users of the google sheet to gain insite on the care givers and service users. 


**Primary User Needs**
- Log in/out.
- Choose assigned care home.
- View notes regarding service user.
- Input notes regarding service user
- Store notes in a worksheetsheet.
- Exit programme gracefully.

**Business Goals**
- Offer a reliable tool for care givers to optmise their knowladge of their service users.
- Help businesses reduce amount time needed to carry out a handover process.
- Reduce the amount of time it takes to write notes.
- Improve the legibility of notes.  
- Centralized data management
- Enhabce record keeping
- Simplify decision making
- Scalability by supporting multiple care homes and using goolge sheets as backend. 

**2. Scope**

**Features**
- User Login: Allow caregivers to log in and track their activities.
- Care Home Management:
  - View a list of care homes and their addresses.
  - Select a care home to view its service users.
- Service User Management:
  - View a list of service users in a selected care home.
  - Select a service user to view their details.
  - Add notes for a service user.
  - Administer medication to a service user with daily limits.
  - View the daily schedule for a service user.
- Error Handling:
  - Handle invalid inputs gracefully.
  - Provide clear error messages for missing or incorrect data.
- Data Storage:
  - Use Google Sheets for centralized data storage and retrieval.

**Content Requirements**

- Clear and concise instructions for users.
- Informative messages for each action (e.g., successful login, invalid input).
- Tabular data display for care homes, service users, and schedules.
- Color-coded messages for better readability (e.g., green for success, red for errors, yellow for warnings).

**3. Structure**

**Interaction Design**

- The application follows a linear flow:
  - User logs in.
  - User selects a care home.
  - User selects a service user.
  - User performs actions (e.g., input notes, administer medication, view schedule).
  - User exits the program.

**Information Architecture**

- The application is structured around the following key components:
  - Care Homes: Displays a list of care homes and allows the user to select one.
  - Service Users: Displays a list of service users for the selected care home.
  - Service User Information: Displays detailed information about the selected service user and provides options for further actions.
  - Notes and Medication: Allows users to input notes and administer medication.
  - Schedules: Displays the daily schedule for the selected service user.

4. Skeleton
Wireframe The application is a command-line interface (CLI), so the wireframe is represented by the flow of text-based menus and tables. Below is an example of the structure:...

Login Screen:
Care Home Selection:
Service User Selection:
Service User Information:
Daily Schedule:

**5. Surface**
**Visual Design**

- Color Scheme:
  - Green: Success messages (e.g., successful login, successful note addition).
  - Yellow: Warnings or prompts (e.g., menu options, input prompts).
  - Red: Error messages (e.g., invalid input, worksheet not found).
- Typography:
  - The application uses the default terminal font.
  - Text is formatted with Colorama for color and Tabulate for table formatting.
- User Feedback
 - The application provides immediate feedback for every action:
  - Success messages for completed actions.
- Error messages for invalid inputs or issues.
- Clear instructions for navigating menus and performing actions.
- Interaction Flow

- The user interacts with the application by entering numeric inputs to navigate menus and perform actions.
- The application uses a loop to ensure the user can retry if they make an invalid input.

## Features
- User Login: Users can log in by entering their name, which is stored in the user worksheet.
- Care Home Management:
- View a list of care homes and their addresses.
- Select a care home to view its service users.
- Service User Management:
- View a list of service users in a selected care home.
- Select a service user to view their information.
- Add notes for a service user.
- Administer medication to a service user with daily limits.
- View the daily schedule for a service user.
- Interactive Menus: Navigate through the application using numbered options.
- Error Handling: Handles invalid inputs and provides user-friendly error messages.
- Data Storage: Uses Google Sheets as the backend for storing and retrieving data.

## Technologies Used**
- Python: The programming language used to build the application.
- Google Sheets API: Used for data storage and retrieval.
- Colorama: For adding colors to the terminal output.
- Tabulate: For displaying data in a tabular format in the terminal.

**Possible Future Plans**
- Add authentication.
- Time stamps for each note added to the workesheet.
- Search and filter functionality.
- Generate daily summary reports for each home, including service user updates, notes and schedules.
- Intergration with other tools, such as task manager of calenders to sync schedules.
- Intergration with other tools to enable notifications and reminders for important tasks.
- Data validation, highliting missing or incomplete data in the worksheet. 
- Analytics and insights,displaying trends or patterns (e.g., frequent medication updates, recurring issues).
- Mobile-friendly interface, adapting the program for mobile devices or create a web-based version for easier access on the go.
- User activity logs to track and log user actions (e.g., logins, data updates) for accountability and auditing.

