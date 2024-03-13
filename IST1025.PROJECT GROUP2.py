"""IST1025 PROJECT"""
"""GROUP 2 """

#importing python libraries for the program
import json
from tkinter import *
from tkinter import messagebox

tasks = []  # Initialize an empty list to store 

# Function to add task
#Get the name and task due date user input fields in the GUI
def add_task():
    name = task_name.get()
    due_date = task_due_date.get()
        # Check whether task name and due date are provided 
    if name and due_date:
        task = {"name": name, "due_date": due_date, "completed": False} #if True, a dictionary is created to represent the task
        tasks.append(task)
        update_task_list()
        task_name.delete(0, END) #clears input fields after updating
        task_due_date.delete(0, END)
        #If either task name or due date is empty, throw a warning message
    else:
        messagebox.showwarning("Warning", "Task name and due date cannot be empty.")


#A function for removing task from tasks after saving
def remove_task():
    #Gets the index of selected task from the task listbox
    try:
        selected_task = task_listbox.curselection()[0]
        #Remove selected task from listbox using its index
        tasks.pop(selected_task)
        update_task_list()#Updates the GUI to reflect the changes made
        #Throws a warning when there is no selection of either task name or due date
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove.")

#Function to mark task already done as completed
def mark_completed():
    try:
        #Gets index of selected task from listbox
        selected_task = task_listbox.curselection()[0]
        tasks[selected_task]["completed"] = True   #Mark the selected task as completed by updating its "completed" status to True
        update_task_list()  #Updates the GUI to reflect changes made
    except IndexError:      # Gives a warning message when neither task name nor due date is selected
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

# A function to edit task alreeady saved
def edit_task():
    try:  #for handling potential errors
        #Gets index of selected task from listbox
        selected_task = task_listbox.curselection()[0]
        edit_window = Toplevel(root) #creates new window for editing selected task
        edit_window.title("Edit Task")# Sets the edit window's title to "Edit Task"
        task_to_edit = tasks[selected_task]# Retrieves selected task details from the list
        
        task_name = task_to_edit["name"]  # Accessing task name from the dictionary
        due_date = task_to_edit["due_date"]  # Accessing due date from the dictionary
        
        #Creating entry widgets to editing window for task name and due date 
        Label(edit_window, text="Task Name:").grid(row=0, column=0, padx=10, pady=5) 
        #Creates entry field for editing task name
        edited_name = Entry(edit_window)
        edited_name.grid(row=0, column=1, padx=10, pady=5) 
        #Inserts the existing task name into the entry field 
        edited_name.insert("end", task_to_edit)
        
        #Creating entry widgets to editing window for task name and due date 
        # Adds a label for due date
        Label(edit_window, text="Due Date:").grid(row=1, column=0, padx=10, pady=5)
        #Creates entry field for editing due date
        edited_due_date = Entry(edit_window)
        edited_due_date.grid(row=1, column=1, padx=10, pady=5)
        #Inserts the existing due date into the entry field 
        edited_due_date.insert("end", task_to_edit)
        
        #A function to save edited task
        def save_edit():
            #Retrieve edited task name and due date from entry widgets
            new_task = f"Task: {edited_name.get()} - Due Date: {edited_due_date.get()}"
            #Updates the newly edited task name and due date by replacing the previous task string
            tasks[selected_task] = new_task
            #Deletes the previous task edited from listbox and inserts the edited string
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, new_task)
            # Collapses/closes the edit window after updating and saving the edited task
            edit_window.destroy()
        #Creates a button widget for saving edited task 
        save_button = Button(edit_window, text="Save", command=save_edit)
        save_button.grid(row=2, column=0, columnspan=2, pady=10)
        #Indicates a warning when user clicks on save_edit without selecting task
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit.")

#function to sort tasks by due date
def sort_by_due_date():
    tasks.sort(key=lambda x: x["due_date"])#sorts the tasks list based on the values of the "due_date" key within each dictionary item in the list
    update_task_list() #Updates GUI with changes made

#function to update task status
def update_task_list():
    task_listbox.delete(0, END) #clears the content of the task_listbox from index 0 to the END.
    for idx, task in enumerate(tasks):
        """checks the "completed" key within each task dictionary. If the task is marked as completed (True),
          it assigns a checkmark ("✔️") to the status variable; otherwise, it assigns a cross mark ("❌")."""
        status = "✔️" if task["completed"] else "❌"
        task_listbox.insert(END, f"{idx + 1}. {status} {task['name']} - Due Date: {task['due_date']}")# inserts a formatted string into the task_listbox for each task


#Program to create a basic to-do list GUI using Tkinter
#Sets up main window
root = Tk()
#Creates the main window's title as To-do-list
root.title("To-Do List")

#Creating a widget label for task name in the main window with grid geometry
Label(root, text="Task Name:").grid(row=0, column=0, sticky=W, padx=10, pady=5)
task_name = Entry(root)
task_name.grid(row=0, column=1, padx=10, pady=5)

#Creating a widget label for task due date in the main window with grid geometry
Label(root, text="Due Date:").grid(row=1, column=0, sticky=W, padx=10, pady=5)
task_due_date = Entry(root)
task_due_date.grid(row=1, column=1, padx=10, pady=5)

#Creating button widgets for other functionalities
add_button = Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

#Creating a listbox for tasks
task_listbox = Listbox(root, width=50)
task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

#Button widget for removing task from listbox
remove_button = Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=4, column=0, pady=5)

#Button widget for marking task as complete in listbox
complete_button = Button(root, text="Mark Completed", command=mark_completed)
complete_button.grid(row=4, column=1, pady=5)


#Button widget for editing task selected from listbox
edit_button = Button(root, text="Edit Task", command=edit_task)
edit_button.grid(row=5, column=0, pady=5)

#Button widget for sorting tasks in listbox
sort_button = Button(root, text="Sort by Due Date", command=sort_by_due_date)
sort_button.grid(row=5, column=1, pady=5)

#for creating a new window
edit_window = Toplevel(root)
edit_window.withdraw()

#Starts the main event loop and keep the GUI running
root.mainloop()