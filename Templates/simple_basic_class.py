import tkinter as tk                            # Import the Tkinter library for GUI development

class SimpleApp:                                # Define a class for the application
    def __init__(self, root):                   # Constructor method, initializes the app
        self.root = root                        # Store the root window in an instance variable
        self.root.title("Simple Tkinter App")   # Set the window title
        self.root.geometry("300x200")           # Set the window size (width x height)

# Run the app
if __name__ == "__main__":                      # Ensures the script runs only when executed directly
    root = tk.Tk()                              # Create the main Tkinter window
    app = SimpleApp(root)                       # Create an instance of the SimpleApp class
    root.mainloop()                             # Start the Tkinter event loop (keeps the window open)