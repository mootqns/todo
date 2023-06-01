from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        login_label.config(text="Login successful!", fg="green")
    else:
        login_label.config(text="Login failed. Please try again.", fg="red")
        
# Create the main window
window = Tk()
window.title("Login Screen")

# Set the initial size of the window
window.geometry("400x200")

# Create username label and entry field
username_label = Label(window, text="Username:")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

# Create password label and entry field
password_label = Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

# Create login button
login_button = Button(window, text="Login", command=login)
login_button.pack()

# Create label for login status
login_label = Label(window, text="")
login_label.pack()

# Start the main loop
window.mainloop()
