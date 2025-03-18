from tkinter import *  # Import all components from the tkinter library for GUI creation.

# Initialize the root window for the calculator GUI
root = Tk()
root.resizable(False, False)  # Prevent the window from being resized
root.title('My Simple Calculator')  # Set the window title
root.config(bg='#343434')  # Set the background color of the window

# Define colors used in the calculator
color_orange = '#fc7703'
color_gray = '#343434'
color_red = '#fc0303'

# Global variables to store the first number and the current operation
first_number = 0
operation = ''

# Create Entry widget for the display area of the calculator
entry = Entry(root, width=8, borderwidth=1, font=('Terminal', 30),
              fg='white', bg=color_gray)
entry.grid(column=0, row=0, columnspan=4)  # Position the Entry widget on the grid

# Functions to handle the button actions:

# Insert a number into the entry field
def insert_number(number):
    current_text = entry.get()  # Get the current text in the entry field
    entry.delete(0, END)  # Clear the entry field
    entry.insert(END, current_text + str(number))  # Add the number to the current text

# Clear the entry field and reset first number and operation
def clear():
    global first_number, operation
    entry.delete(0, END)  # Clear the entry field
    first_number = 0  # Reset the first number
    operation = ''  # Reset the operation

# Functions for each arithmetic operation
def add():
    global first_number, operation
    if entry.get():  # If there's a number in the entry field
        first_number = float(entry.get())  # Store the number as the first number
    operation = 'add'  # Set the operation to addition
    entry.delete(0, END)  # Clear the entry field

def subtract():
    global first_number, operation
    if entry.get():  # If there's a number in the entry field
        first_number = float(entry.get())  # Store the number as the first number
    operation = 'subtract'  # Set the operation to subtraction
    entry.delete(0, END)  # Clear the entry field

def multiply():
    global first_number, operation
    if entry.get():  # If there's a number in the entry field
        first_number = float(entry.get())  # Store the number as the first number
    operation = 'multiply'  # Set the operation to multiplication
    entry.delete(0, END)  # Clear the entry field

def divide():
    global first_number, operation
    if entry.get():  # If there's a number in the entry field
        first_number = float(entry.get())  # Store the number as the first number
    operation = 'divide'  # Set the operation to division
    entry.delete(0, END)  # Clear the entry field

# Equal function to calculate and show the result
def equal():
    global first_number, operation
    if not entry.get() or operation == '':  # If the entry field is empty or no operation is selected
        entry.delete(0, END)  # Clear the entry field
        entry.insert(END, str(first_number))  # Just display the first number
        return

    second_number = float(entry.get())  # Get the second number
    if operation == 'add':
        result = first_number + second_number  # Perform addition
    elif operation == 'subtract':
        result = first_number - second_number  # Perform subtraction
    elif operation == 'multiply':
        result = first_number * second_number  # Perform multiplication
    elif operation == 'divide':
        if second_number == 0:  # Prevent division by zero
            entry.delete(0, END)  # Clear the entry field
            entry.insert(END, "Error")  # Show error message
            return
        result = first_number / second_number  # Perform division

    entry.delete(0, END)  # Clear the entry field
    entry.insert(END, str(result))  # Display the result

    first_number = result  # Set the result as the new first number
    operation = ''  # Reset the operation

# Insert a decimal point if there isn't already one
def insert_dot():
    current_text = entry.get()
    if '.' not in current_text:  # Only add a dot if there isn't already one
        entry.delete(0, END)  # Clear the entry field
        entry.insert(END, current_text + '.')  # Add the dot

# Bind keyboard input to operator functions
root.bind('+', lambda event: add())  # Bind the '+' key to addition
root.bind('-', lambda event: subtract())  # Bind the '-' key to subtraction
root.bind('*', lambda event: multiply())  # Bind the '*' key to multiplication
root.bind('/', lambda event: divide())  # Bind the '/' key to division
root.bind('<Return>', lambda event: equal())  # Bind the Enter key to equal
root.bind('<BackSpace>', lambda event: clear())  # Bind Backspace to clear

# Number Buttons
button_7 = Button(root, text='7', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(7))
button_7.grid(column=0, row=1)  # Position button 7 in the grid
button_8 = Button(root, text='8', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(8))
button_8.grid(column=1, row=1)  # Position button 8 in the grid
button_9 = Button(root, text='9', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(9))
button_9.grid(column=2, row=1)  # Position button 9 in the grid

button_4 = Button(root, text='4', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(4))
button_4.grid(column=0, row=2)  # Position button 4 in the grid
button_5 = Button(root, text='5', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(5))
button_5.grid(column=1, row=2)  # Position button 5 in the grid
button_6 = Button(root, text='6', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(6))
button_6.grid(column=2, row=2)  # Position button 6 in the grid

button_1 = Button(root, text='1', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(1))
button_1.grid(column=0, row=3)  # Position button 1 in the grid
button_2 = Button(root, text='2', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(2))
button_2.grid(column=1, row=3)  # Position button 2 in the grid
button_3 = Button(root, text='3', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(3))
button_3.grid(column=2, row=3)  # Position button 3 in the grid

button_0 = Button(root, text='0', padx=25, pady=10, fg='white', bg=color_gray,
                  command=lambda: insert_number(0))
button_0.grid(column=0, row=4)  # Position button 0 in the grid

dot_button = Button(root, text=' .', padx=25, pady=10, fg='white', bg=color_gray,
                  command=insert_dot)
dot_button.grid(column=1, row=4)  # Position the dot button

# Operator Buttons
button_plus = Button(root, text='+', padx=25, pady=10, fg='white', bg=color_orange,
                     command=add)
button_plus.grid(column=3, row=1)  # Position the plus button

subtract_button = Button(root, text='- ', padx=25, pady=10, fg='white', bg=color_orange,
                         command=subtract)
subtract_button.grid(column=3, row=2)  # Position the minus button

multiply_button = Button(root, text='* ', padx=25, pady=10, fg='white', bg=color_orange,
                         command=multiply)
multiply_button.grid(column=3, row=3)  # Position the multiply button

division_button = Button(root, text='/ ', padx=25, pady=10, fg='white', bg=color_orange,
                         command=divide)
division_button.grid(column=3, row=4)  # Position the divide button

# Clear and equal buttons
clear_button = Button(root, text='C', padx=24, pady=10, fg='white', bg=color_red,
                      command=clear)
clear_button.grid(column=2, row=4)  # Position the clear button

equal_button = Button(root, text='=', padx=123, pady=10, borderwidth=1, fg='white', bg=color_orange,
                      command=equal)
equal_button.grid(column=0, row=5, columnspan=4)  # Position the equal button

# Start the Tkinter event loop to keep the window open
root.mainloop()
