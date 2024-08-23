import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Task List
        self.tasks = []

        # Frame for the task list
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.task_frame, font=('Arial', 12), selectmode=tk.SINGLE, height=12, width=40)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry widget to add tasks
        self.task_entry = tk.Entry(self.root, font=('Arial', 14))
        self.task_entry.pack(pady=10)

        # Button to add tasks
        self.add_task_btn = tk.Button(self.root, text="Add Task", font=('Arial', 12), width=15, command=self.add_task)
        self.add_task_btn.pack(pady=5)

        # Button to delete tasks
        self.delete_task_btn = tk.Button(self.root, text="Delete Task", font=('Arial', 12), width=15, command=self.delete_task)
        self.delete_task_btn.pack(pady=5)

        # Button to update tasks
        self.update_task_btn = tk.Button(self.root, text="Update Task", font=('Arial', 12), width=15, command=self.update_task)
        self.update_task_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.task_entry.get()
            if updated_task != "":
                self.tasks[selected_task_index[0]] = updated_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
