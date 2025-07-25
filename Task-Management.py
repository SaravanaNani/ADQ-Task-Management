import tkinter as tk
from tkinter import messagebox

# Initialize users and tasks
users = {}
statuses = ["New", "In Progress", "Hold", "In Testing", "Completed"]

def add_user():
    username = user_entry.get().strip()
    if username:
        if username in users:
            messagebox.showerror("Error", "User already exists!")
        else:
            users[username] = []
            user_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"User '{username}' added successfully!")
    else:
        messagebox.showerror("Error", "User name cannot be empty!")

def add_task():
    username = user_entry.get().strip()
    if username not in users:
        messagebox.showerror("Error", "User does not exist!")
        return

    task_name = task_entry.get().strip()

    if task_name:
        task = {"task": task_name, "status": "New"}
        users[username].append(task)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
    else:
        messagebox.showerror("Error", "Task name cannot be empty!")

def view_all_tasks():
    if not users:
        messagebox.showinfo("Info", "No users or tasks available.")
        return

    task_window = tk.Toplevel(app)
    task_window.title("All Users and Tasks")
    task_list = tk.Text(task_window, width=80, height=20)
    task_list.pack()

    for username, tasks in users.items():
        task_list.insert(tk.END, f"User: {username}\n")
        for idx, task in enumerate(tasks, start=1):
            task_list.insert(tk.END, f"  {idx}. Task: {task['task']}, Status: {task['status']}\n")
        task_list.insert(tk.END, "-" * 50 + "\n")

def update_status():
    username = user_entry.get().strip()
    if username not in users:
        messagebox.showerror("Error", "User does not exist!")
        return

    task_index = int(task_index_entry.get().strip()) - 1

    if 0 <= task_index < len(users[username]):
        new_status = status_var.get()
        users[username][task_index]["status"] = new_status
        messagebox.showinfo("Success", "Task status updated successfully!")
    else:
        messagebox.showerror("Error", "Invalid Ticket number!")

def delete_user_tasks():
    username = user_entry.get().strip()
    if username not in users:
        messagebox.showerror("Error", "User does not exist!")
        return

    users.pop(username)
    messagebox.showinfo("Success", f"User '{username}' and their tasks have been deleted!")

# Main application window
app = tk.Tk()
app.title("User & Task Management")

# Add user section
tk.Label(app, text="User Name:").grid(row=0, column=0, padx=10, pady=5)
user_entry = tk.Entry(app, width=30)
user_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Button(app, text="Add User", command=add_user).grid(row=0, column=2, padx=10, pady=5)

# Add task section
tk.Label(app, text="Task Name:").grid(row=1, column=0, padx=10, pady=5)
task_entry = tk.Entry(app, width=30)
task_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(app, text="Add Task", command=add_task).grid(row=1, column=2, padx=10, pady=5)

# View tasks
tk.Button(app, text="View All Tasks", command=view_all_tasks).grid(row=2, column=0, columnspan=3, pady=10)

# Update task status
tk.Label(app, text="Ticket Number:").grid(row=3, column=0, padx=10, pady=5)
task_index_entry = tk.Entry(app, width=10)
task_index_entry.grid(row=3, column=1, padx=10, pady=5)

status_var = tk.StringVar(app)
status_var.set(statuses[0])  # Default value
tk.OptionMenu(app, status_var, *statuses).grid(row=3, column=2, padx=10, pady=5)

tk.Button(app, text="Update Status", command=update_status).grid(row=4, column=0, columnspan=3, pady=10)

# Delete user and tasks
tk.Button(app, text="Delete User & Tasks", command=delete_user_tasks).grid(row=5, column=0, columnspan=3, pady=10)

# Run the application
app.mainloop()
 
