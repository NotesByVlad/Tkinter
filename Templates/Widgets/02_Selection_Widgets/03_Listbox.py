### Listbox (Multiple Selectable Items) ###

import tkinter as tk  # Import the Tkinter library

# Function to display the selected item
def get_selected():
    selected_indices = listbox.curselection()  # Get the index of the selected item(s)
    if selected_indices:  # Check if something is selected
        selected_item = listbox.get(selected_indices[0])  # Get the text of the first selected item
        print(f"Selected item: {selected_item}")  # Print the selected item

# Create the main application window
root = tk.Tk()
root.title("Listbox Example")  # Set the window title

# Create a Listbox widget
listbox = tk.Listbox(root, height=5)  # Define the listbox with a height of 5 items

# Add items to the listbox
items = ["Python", "Java", "C++", "JavaScript"]
for item in items:
    listbox.insert(tk.END, item)  # Insert each item into the listbox

listbox.pack(pady=10)  # Pack the listbox into the window

# Create a button to get the selected item
button = tk.Button(root, text="Get Selection", command=get_selected)

button.pack(pady=5)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop