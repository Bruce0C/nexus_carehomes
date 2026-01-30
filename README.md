# [Nexus Carehomes](https://nexus-care-e0ddbf0b6681.herokuapp.com)

Developer: Bruce Chibisa ([Bruce0C](https://www.github.com/Bruce0C))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Bruce0C/nexus_carehomes)](https://www.github.com/Bruce0C/nexus_carehomes/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Bruce0C/nexus_carehomes)](https://www.github.com/Bruce0C/nexus_carehomes/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Bruce0C/nexus_carehomes)](https://www.github.com/Bruce0C/nexus_carehomes)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://nexus-care-e0ddbf0b6681.herokuapp.com)

![screenshot](documentation/mockup.png)

source: [nexus_carehomes amiresponsive](https://ui.dev/amiresponsive?url=https://nexus-care-e0ddbf0b6681.herokuapp.com)


## UX

## The 5 Planes of UX



#### 1. Strategy

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