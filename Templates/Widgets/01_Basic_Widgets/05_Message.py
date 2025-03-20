### Message Widget (Auto-Wrapping Text) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("Message Widget Example")  # Set the window title

# Create a Message widget to display long text with auto-wrap
message_text = "This is a Message widget. It automatically wraps long text."
message = tk.Message(root, text=message_text, width=200, font=("Arial", 12))

message.pack(pady=10)  # Pack the message widget into the window

root.mainloop()  # Start the Tkinter event loop