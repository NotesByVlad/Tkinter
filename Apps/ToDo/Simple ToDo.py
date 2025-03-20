import tkinter as tk                            # Import the Tkinter library for GUI development
from tkinter import simpledialog, messagebox
import json, os
import os

class SimpleToDoApp:                                # Define a class for the application
    def __init__(self, root):                   # Constructor method, initializes the app
        self.root = root                        # Store the root window in an instance variable
        self.root.title("Simple Tkinter App")   # Set the window title
        self.root.geometry("1001x660")           # Set the window size (width x height)
        
        # Styles
        self.font = ("Helvetica", 16)
        self.bg = '#333'
        self.bg_red = '#e00000'
        self.fg = '#fff'

        # App Background color
        self.root.config(bg=self.bg)

        # Creation
        self.center_window()
        self.create_widgets()

        # Load file
        self.load_tasks()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def create_widgets(self):
        self.create_labels()
        self.create_listboxes()
        self.create_buttons()

    def create_labels(self):
        self.progress_label = tk.Label(self.root, text="In Progress", 
                                        width=12,height=2,
                                        font=self.font, bg=self.bg, fg=self.fg)
        self.progress_label.grid(row=0,column=0, columnspan=2)

        self.done_tasks_label = tk.Label(self.root, text="Done Tasks", 
                                        width=12,height=2,
                                        font=self.font, bg=self.bg, fg=self.fg)
        self.done_tasks_label.grid(row=0,column=3, columnspan=2)

    def create_listboxes(self):
        self.task_list = tk.Listbox(self.root, font=self.font,
                                    width=40,height=15,
                                    bg=self.bg,fg=self.fg)
        self.task_list.grid(row=1,column=0, columnspan=2)
        # Scroll bar
        self.create_scrollbars(self.task_list,1,2,2,0)
       

        self.done_task_list = tk.Listbox(self.root, font=self.font,
                                         width=40,height=15,
                                         bg=self.bg,fg=self.fg)
        self.done_task_list.grid(row=1,column=3,columnspan=2)

        self.create_scrollbars(self.done_task_list,1,5,2,3)

    def create_scrollbars(self, widget, v_row, v_col, h_row, h_col):
        self.vertical_scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.horizontal_scrollbar = tk.Scrollbar(self.root, orient="horizontal")

        widget.config(yscrollcommand=self.vertical_scrollbar.set,
                    xscrollcommand=self.horizontal_scrollbar.set)

        self.vertical_scrollbar.grid(row=v_row,column=v_col,sticky='ns')
        self.horizontal_scrollbar.grid(row=h_row,column=h_col,sticky="ew",columnspan=2)

        self.vertical_scrollbar.config(command=widget.yview)
        self.horizontal_scrollbar.config(command=widget.xview)

    def create_buttons(self):
        add_button = tk.Button(self.root, text="Add task", 
                               width=15,height=2, 
                               font=self.font, bg=self.bg, fg=self.fg,
                               command=self.add_task)
        add_button.grid(row=3,column=0,sticky='e')

        mark_button = tk.Button(self.root, text="Mark as Done", 
                                width=15,height=2, 
                                font=self.font, bg=self.bg, fg=self.fg,
                                command=self.mark_as_done)
        mark_button.grid(row=3,column=1,sticky='w')

        edit_button = tk.Button(self.root, text="Edit task", 
                                width=15,height=2, 
                                font=self.font, bg=self.bg, fg=self.fg,
                                command=self.edit_task)
        edit_button.grid(row=4,column=0,sticky='e')

        remove_button = tk.Button(self.root, text="Remove Task", 
                                  width=15,height=2, 
                                  font=self.font, bg=self.bg, fg=self.fg,
                                  command=self.remove_task)
        remove_button.grid(row=4,column=1,sticky='w')

        clear_tasks_button = tk.Button(self.root, text="Clear Tasks", 
                                       width=15,height=2, 
                                       font=self.font, bg=self.bg_red, fg=self.fg,
                                    command=self.clear_tasks)
        clear_tasks_button.grid(row=5,column=1,sticky='w')

        save_button = tk.Button(self.root, text="Save",
                                width=15,height=2,
                                font=self.font,bg=self.bg,fg=self.fg,
                                command=self.save_tasks)
        save_button.grid(row=5,column=0,sticky='e')

        clear_history_button = tk.Button(self.root, text="Clear History", 
                                         width=20,height=2, 
                                         font=self.font, bg=self.bg_red, fg=self.fg,
                                  command=self.clear_task_history)
        clear_history_button.grid(row=3,column=3,sticky='we',columnspan=2)      
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def add_task(self):
        task = simpledialog.askstring("Add","Add a task")
        task = task.strip()
        if task:
            self.task_list.insert(tk.END,task)

    def mark_as_done(self):
        index = self.task_list.curselection()
        if not index:
            self.show_warning('Please select task to mark as done!')
        else:
            task = self.task_list.get(index[0])
            self.done_task_list.insert(tk.END,task)
            self.task_list.delete(index)

    def edit_task(self):
        index = self.task_list.curselection()
        if not index:
            self.show_warning('Please select task to edit!')
            return
        
        task = self.task_list.get(index[0])
        new_task = simpledialog.askstring('Edit task', f'Task: {task}')

        new_task = new_task.strip()
        if not new_task:
            self.show_warning('Task can\'t be empty!')
        else:
            self.task_list.delete(index)
            self.task_list.insert(index, new_task)

    def remove_task(self):
        index = self.task_list.curselection()
        if not index:
            self.show_warning('Please select task to delete!')
        else:
            self.task_list.delete(index)

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)

    def clear_task_history(self):
        self.done_task_list.delete(0, tk.END)

    def save_tasks(self):
    # Get the directory where the current script is located
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Create the full path for the JSON file
        json_file_path = os.path.join(script_directory, "tasks.json")

        # Get all items from the task list and done task list
        task_items = [self.task_list.get(i) for i in range(self.task_list.size())]
        done_task_items = [self.done_task_list.get(i) for i in range(self.done_task_list.size())]

        # Create a dictionary to store both lists
        tasks_data = {
            "tasks": task_items,
            "done_tasks": done_task_items
        }

        # Save the dictionary to a JSON file in the same directory as the .py file
        try:
            with open(json_file_path, "w") as json_file:
                json.dump(tasks_data, json_file, indent=4)
            (f"Tasks successfully saved to {json_file_path}")  # You can replace this with a tkinter messagebox if needed
        except Exception as e:
            self.show_error(f"An error occurred while saving tasks: {e}")

    def load_tasks(self):
                # Get the directory where the current script is located
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Create the full path for the JSON file
        json_file_path = os.path.join(script_directory, "tasks.json")

        # Load the tasks from the file if it exists
        if os.path.exists(json_file_path):
            try:
                with open(json_file_path, "r") as json_file:
                    tasks_data = json.load(json_file)
                    
                    # Load the tasks into the Listboxes
                    for task in tasks_data.get("tasks", []):
                        self.task_list.insert(tk.END, task)
                    
                    for done_task in tasks_data.get("done_tasks", []):
                        self.done_task_list.insert(tk.END, done_task)

                print(f"Tasks successfully loaded from {json_file_path}")
            except Exception as e:
                self.show_error(f"An error occurred while loading tasks: {e}")
        else:
            self.show_warning("No saved tasks found.")

    def show_warning(self,message):
        messagebox.showwarning('Warning', message)

    def show_error(self,message):
        messagebox.showerror('Error', message)

    def show_succes(self,message):
        messagebox.showinfo('Succes!', message)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def center_window(self):
        """ Centers the window on the screen """
        self.root.update()                          # Update the window to get correct width & height

        # Get the window dimensions
        window_width = self.root.winfo_width()      # Get the width of the window
        window_height = self.root.winfo_height()    # Get the height of the window

        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()    # Get the screen width
        screen_height = self.root.winfo_screenheight()  # Get the screen height

        # Calculate x and y coordinates to center the window
        window_x = int((screen_width / 2) - (window_width / 2))    # X position
        window_y = int((screen_height / 2) - (window_height / 2))  # Y position

        # Set the new position of the window
        self.root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Run the app
if __name__ == "__main__":                      # Ensures the script runs only when executed directly
    root = tk.Tk()                              # Create the main Tkinter window
    app = SimpleToDoApp(root)                       # Create an instance of the SimpleApp class
    root.mainloop()                             # Start the Tkinter event loop (keeps the window open)