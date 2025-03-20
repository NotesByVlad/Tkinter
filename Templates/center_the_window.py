# -------------------------------------------------------------------------- #
# Procedural Approach ## Procedural Approach  ### Procedural Approach ####   #
# -------------------------------------------------------------------------- #
# -(Whitout Class)- #

import tkinter as tk            # Import the Tkinter library

# Create the main window
root = tk.Tk()
root.title("Centered Window")   # Set the window title
root.geometry("300x200")        # Set an initial size (width x height)

# Update the window to get the actual width and height (important for centering)
root.update()

# Get the window dimensions
window_width = root.winfo_width()       # Get the width of the window
window_height = root.winfo_height()     # Get the height of the window

# Get the screen dimensions
screen_width = root.winfo_screenwidth()    # Get the screen width
screen_height = root.winfo_screenheight()  # Get the screen height

# Calculate x and y coordinates to center the window
window_x = int((screen_width / 2) - (window_width / 2))    # X position
window_y = int((screen_height / 2) - (window_height / 2))  # Y position

# Set the new geometry (position) of the window
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Run the Tkinter event loop
root.mainloop()

# -------------------------------------------------------------------------- #
# Class-Based Approach ## Class-Based Approach ### Class-Based Approach #### #
# -------------------------------------------------------------------------- #

import tkinter as tk  # Import the Tkinter library

class CenteredApp:
    def __init__(self, root):              # Constructor to initialize the app
        self.root = root                   # Store the main window instance
        self.root.title("Centered Window") # Set the window title
        self.root.geometry("300x200")      # Set an initial size (width x height)

        self.center_window()               # Call method to center the window

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

# Run the application
if __name__ == "__main__":
    root = tk.Tk()           # Create the Tkinter window
    app = CenteredApp(root)  # Create an instance of the app
    root.mainloop()          # Run the Tkinter event loop