### Menubutton (Button with Menu) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("Menubutton Example")  # Set the window title

# Create a Menubutton widget
menu_button = tk.Menubutton(root, text="Options", relief="raised")
menu_button.menu = tk.Menu(menu_button, tearoff=0)

# Add items to the Menubutton menu
menu_button.menu.add_command(label="Option 1")
menu_button.menu.add_command(label="Option 2")

menu_button["menu"] = menu_button.menu  # Assign menu to Menubutton
menu_button.pack(pady=10)  # Pack the Menubutton into the window

root.mainloop()  # Start the Tkinter event loop