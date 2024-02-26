import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # List to store tasks
        self.TaskList = []

        # user interface
        # Creating a listbox for current tasks
        self.TaskListBox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.TaskListBox.pack(pady=10)

        # Entry to add tasks 
        self.EnterTask = ttk.Entry(root, width=30)
        self.EnterTask.pack(pady=10)

        # Button to add the task marked in the entry
        self.AddTask = ttk.Button(root, text="Add Task +", command=self.Add_Task)
        self.AddTask.pack()

        # Button to remove the selected task from the list
        self.DeleteTask = ttk.Button(root, text="Delete Task -", command=self.Delete_Task)
        self.DeleteTask.pack()

        # Button to mark as completed the selected tasks in the list
        self.CompleteTask = ttk.Button(root, text="Marked as complete *", command=self.Marked_Completed)
        self.CompleteTask.pack()

    # function to add a task
    def Add_Task(self):
        nouvelle_tache = self.EnterTask.get()
        if nouvelle_tache:
            self.TaskList.append(nouvelle_tache)
            self.Update_Task_List()
            self.EnterTask.delete(0, tk.END)  # Clear the field after adding

    # Function to remove the selected task from the list
    def Delete_Task(self):
        selections = self.TaskListBox.curselection()
        if selections:
            for index in reversed(selections):
                del self.TaskList[index]
            self.Update_Task_List()

    # Function to mark a task as complete the list
    def Marked_Completed(self):
        selection = self.TaskListBox.curselection()
        if selection:
            index = selection[0]
            Task = self.TaskList[index]
            messagebox.showinfo("Marked Complete", f"Task '{Task}' marked as completed!" )
            self.TaskListBox.delete(index)
            self.TaskListBox.insert(tk.END, f'\u2713 {Task}')
            self.TaskListBox.itemconfig(tk.END-1, {'fg': 'gray'})
            self.Update_Task_List()

    # Function to dynamically update the list
    def Update_Task_List(self):
        self.TaskListBox.delete(0, tk.END)
        for task in self.TaskList:
            self.TaskListBox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()