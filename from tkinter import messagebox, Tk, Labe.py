from tkinter import messagebox, Tk, Label, Entry, Button, Listbox, Scrollbar

tasks = []

def add_task():
    name = task_name.get()
    due_date = task_due_date.get()
    if name and due_date:
        task = f"Task: {name} - Due Date: {due_date}"
        task_list.insert("end", task)
        tasks.append(task)
        task_name.delete(0, "end")
        task_due_date.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Task name and due date cannot be empty.")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        tasks.pop(selected_task)
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove.")

root = Tk()
root.title("Simple To-Do List")

Label(root, text="Task Name:").grid(row=0, column=0, padx=10, pady=5)
task_name = Entry(root)
task_name.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Due Date:").grid(row=1, column=0, padx=10, pady=5)
task_due_date = Entry(root)
task_due_date.grid(row=1, column=1, padx=10, pady=5)

add_button = Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

scrollbar = Scrollbar(root)
scrollbar.grid(row=3, column=2, sticky="ns")

task_list = Listbox(root, width=40, yscrollcommand=scrollbar.set)
task_list.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

scrollbar.config(command=task_list.yview)

remove_button = Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()