### Text Widget (Multi-line Input) ###

import tkinter as tk  # Import Tkinter

# Create the main application window
root = tk.Tk()
root.title("Text Widget Example")  # Set the window title

# Create a Text widget for multi-line input
text_widget = tk.Text(root, height=5, width=40)  # Define height and width
text_widget.pack(pady=10)  # Pack the text widget into the window

# Function to retrieve text content
def get_text():
    user_text = text_widget.get("1.0", tk.END)  # Get text from line 1, char 0 to end
    print(f"User typed:\n{user_text}")  # Print the text

# Create a button to get the text input
button = tk.Button(root, text="Get Text", command=get_text)
button.pack(pady=5)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop