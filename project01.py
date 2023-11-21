import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # Entry for task description
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for actions
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.display_button = tk.Button(self.master, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=1, column=0, padx=5, pady=10)

        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=1, column=1, padx=5, pady=10)

        self.complete_button = tk.Button(self.master, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=10)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=5, pady=10)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append({"description": task_description, "completed": False})
            messagebox.showinfo("Task Added", f"Task '{task_description}' added successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task description.")

    def display_tasks(self):
        if self.tasks:
            task_list = "\n".join([f"{i + 1}. {task['description']} - {'Completed' if task['completed'] else 'Not Completed'}"
                                  for i, task in enumerate(self.tasks)])
            messagebox.showinfo("To-Do List", task_list)
        else:
            messagebox.showinfo("To-Do List", "No tasks in the list.")

    def remove_task(self):
        if self.tasks:
            task_index = self.get_selected_task_index()
            if task_index is not None:
                removed_task = self.tasks.pop(task_index)
                messagebox.showinfo("Task Removed", f"Task '{removed_task['description']}' removed successfully.")
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to remove.")
        else:
            messagebox.showinfo("To-Do List", "No tasks in the list.")

    def mark_as_completed(self):
        if self.tasks:
            task_index = self.get_selected_task_index()
            if task_index is not None:
                self.tasks[task_index]["completed"] = True
                messagebox.showinfo("Task Completed", "Task marked as completed.")
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")
        else:
            messagebox.showinfo("To-Do List", "No tasks in the list.")

    def update_task(self):
        if self.tasks:
            task_index = self.get_selected_task_index()
            if task_index is not None:
                new_description = simpledialog.askstring("Update Task", "Enter new description:")
                if new_description is not None:
                    self.tasks[task_index]["description"] = new_description
                    messagebox.showinfo("Task Updated", "Task description updated successfully.")
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to update.")
        else:
            messagebox.showinfo("To-Do List", "No tasks in the list.")

    def get_selected_task_index(self):
        selected_task = simpledialog.askinteger("Select Task", "Enter the task number:")
        if selected_task is not None and 1 <= selected_task <= len(self.tasks):
            return selected_task - 1
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
