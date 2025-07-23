# ADQ-Task-Management - User & Task Management Module

This project is a Python-based User and Task Management application that uses Tkinter for a graphical user interface (GUI). The application allows adding users, assigning tasks to users, updating task statuses, viewing all tasks, and deleting a user along with their tasks.

# Features

### Add Users

-> Allows creating users.

-> Displays error if the user already exists or the input is empty.

### Add Tasks

-> Assign tasks to specific users:

-> Tasks start with a default status of "New":

### View All Tasks

-> Displays all users and their tasks in a formatted list:

### Update Task Status

-> Allows changing the status of a specific task for a user.


### Available statuses:

-> New
-> In Progress
-> Hold
-> In Testing
-> Completed

<img width="482" height="235" alt="image" src="https://github.com/user-attachments/assets/408a715d-02f6-4a40-a153-66af0e3fcaa4" />


### Delete User & Tasks

-> Deletes a user and all associated tasks.

# Setup Instructions

Prerequisites:

Python 3.x installed on your system.

Clone the Repository:
```
https://github.com/SaravanaNani/ADQ-Task-Management.git
```

### Run the Application:

task-managemet.py

# Usage Guide

### Add a User

-> Enter a username in the User Name field.

-> Click the "Add User" button.

<img width="547" height="303" alt="Image" src="https://github.com/user-attachments/assets/e83ba647-1563-4710-920b-2dcfeeb97c00" />


### Add a Task

-> Enter a username in the User Name field.

-> Enter a task name in the Task Name field.

-> Click the "Add Task" button.


<img width="651" height="428" alt="image" src="https://github.com/user-attachments/assets/d9a5c66d-a87c-4026-921e-9bf36dc8a6f4" />


-> Tasks start with a default status of "New":


<img width="628" height="339" alt="image" src="https://github.com/user-attachments/assets/da578ca3-6c76-40dd-b2d5-d9f0a14bbd5a" />


### View All Tasks

-> Click the "View All Tasks" button.

-> A new window will display all users and their tasks.


<img width="1026" height="654" alt="image" src="https://github.com/user-attachments/assets/70073b7f-91bb-4006-bc7c-2ba62b03a588" />


### Update Task Status

-> Enter the username in the User Name field.

-> Enter the ticket number in the Task Number field (as displayed in the "View All Tasks" section).

-> Select the new status from the dropdown.

-> Click the "Update Status" button.


<img width="1073" height="643" alt="image" src="https://github.com/user-attachments/assets/48a27bae-fc8e-40b0-a846-c421f82bb4c0" />


### Delete User & Tasks

-> Enter the username in the User Name field.

-> Click the "Delete User & Tasks" button.
