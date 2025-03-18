### Entry (User Input Field) ###

import tkinter as tk  # Import the Tkinter library

# Function to retrieve text from entry field
def get_text():
    user_input = entry.get()  # Get the text entered
    print(f"User entered: {user_input}")  # Print the text

# Create the main application window
root = tk.Tk()
root.title("Entry Example")  # Set the window title

# Create an Entry widget for user input
entry = tk.Entry(root, font=("Arial", 12))

entry.pack(pady=10)  # Pack the entry field into the window

# Create a button to get input when clicked
button = tk.Button(root, text="Get Text", command=get_text)

button.pack(pady=5)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop
