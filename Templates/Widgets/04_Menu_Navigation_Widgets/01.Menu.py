### Menu (Dropdown Menu) ###

import tkinter as tk  # Import Tkinter

# Function for menu actions
def menu_action():
    print("Menu item clicked")

# Create the main application window
root = tk.Tk()
root.title("Menu Example")  # Set the window title

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=menu_action)  # Add "Open" option
file_menu.add_command(label="Save", command=menu_action)  # Add "Save" option
file_menu.add_separator()  # Add a separator
file_menu.add_command(label="Exit", command=root.quit)  # Add "Exit" option

# Add "File" menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the window to use this menu bar
root.config(menu=menu_bar)

root.mainloop()  # Start the Tkinter event loop