### Checkbutton Widget (Checkbox) ###

import tkinter as tk  # Import Tkinter

# Function to print checkbox state
def show_state():
    print(f"Checkbox is {'checked' if var.get() else 'unchecked'}")

# Create the main application window
root = tk.Tk()
root.title("Checkbutton Example")  # Set the window title

# Create an IntVar to track the state (0 = off, 1 = on)
var = tk.IntVar()

# Create a Checkbutton widget
checkbutton = tk.Checkbutton(root, text="Check me!", variable=var, command=show_state)

checkbutton.pack(pady=10)  # Pack the checkbox into the window

root.mainloop()  # Start the Tkinter event loop