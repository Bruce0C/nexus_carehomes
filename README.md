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

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a caregiver | I want to log in to the system | so that my activities can be tracked and recorded.. |
| As a caregiver  | I want to view a list of care homes | so that I can select the care home I am assigned to. |
| As a caregiver  | I want to select my assigned care home | so that I can view the service users in that care home. |
| As a caregiver  | I want to view a list of service users in my assigned care home | So that I can choose the service user I am responsible for.|
| As a caregiver  |I want to select a specific service user | so that I can view their details and manage their information. |
| As a caregiver  | I want to view detailed information about a service user | so that I can better understand their needs and provide appropriate care.|
| As a caregiver  | I want to input notes about a service user | so that I can document important information about their care. |
| As a caregiver | I want to log the medication I administer to a service user | so that I can track the medication history and ensure compliance with dosage limits. 
| As a caregiver| I want to view the daily schedule for a service user | so that I can plan my day and ensure all activities are completed on time. 
| As a caregiver | I want to exit the program gracefully | so that I can end my session without losing any data. 
| As a caregiver | I want the program to handle invalid inputs | so that I can correct my mistakes without the program crashing. 
| As a manager | I want all data to be stored in a centralized Google Sheet | so that I can monitor and analyze the activities of caregivers and service users. 
| As a business owner | I want the system to support multiple care homes and service users | so that it can scale as my business grows. 
| As a caregiver | I want the application to be simple and easy to use | so that I can quickly navigate and perform my tasks without confusion. |


## Features

| Features | Notes| Screenshots |
| --- | --- | --- |
|User Login| Users can log in by entering their name, which is stored in the user worksheet. | [screenshot](documentation/features/data-validation.png)|
|Care Home Management| View a list of care homes and their addresses. | [screenshot](documentation/features/data-validation.png)|
| |Select a care home to view its service users. | [screenshot](documentation/features/data-validation.png)|
|Service User Management: | View a list of service users in a selected care home. | [screenshot](documentation/features/data-validation.png) |
| | Select a service user to view their information. | [screenshot](documentation/features/data-validation.png)|
| | Add notes for a service user. | [screenshot](documentation/features/data-validation.png) |
| | Administer medication to a service user with daily limits. | [screenshot](documentation/features/data-validation.png)|
| | View the daily schedule for a service user. | [screenshot](documentation/features/data-validation.png)|
|Interactive Menus: | Navigate through the application using numbered options. | [screenshot](documentation/features/data-validation.png)|
|Error Handling: | Handles invalid inputs and provides user-friendly error messages. | [screenshot](documentation/features/data-validation.png)|
|Data Storage: | Uses Google Sheets as the backend for storing and retrieving data. | [screenshot](documentation/features/data-validation.png) |

**Future Features**
- **User Authentication**: Add a login system with usernames and passwords for caregivers to ensure secure access to the application.
- **Role-Based Access Control**: Implement different user roles (e.g., caregiver, manager, admin) with varying levels of access.
- **Reporting and Analytics**: Generate reports and analytics for managers, such as:
   - Total notes added per caregiver.
   - Medication logs for each service user.
   - Summary of daily activities.
- **Notifications and Reminders**: Add notifications and reminders for caregivers about upcoming tasks, medication schedules, or important notes.
- **Search and Filter Functionality**: Allow users to search for specific service users, notes, or care homes and filter data based on criteria (e.g., age, room number, or activity type).
- **Export Data**: Allow users to export data (e.g., notes, schedules, or reports) to CSV or PDF files for offline use or sharing.
- **Customizable Schedules**: Allow caregivers or managers to customize the daily schedules for service users.
- **Service User Alerts**:
Description: Add alerts for critical service user conditions (e.g., missed medication, overdue tasks).


## Technologies Used
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

