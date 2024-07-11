from tkinter import *
from tkinter import messagebox
import time
from firebase import firebase
from cryptography.fernet import Fernet
import base64

# Initialize Fernet cipher suite with a securely managed key
key = b'12345678901234567890123456789012'
cipher_suite = Fernet(base64.urlsafe_b64encode(key))

# Initialize Firebase
firebase = firebase.FirebaseApplication(
    "https://mystudyapp-46eae-default-rtdb.firebaseio.com/", None)

# Function to toggle password visibility
def change1():
    if password_entry['show'] == "*":
        password_entry['show'] = ""
    else:
        password_entry['show'] = "*"

# Function to switch to login window
def login_window():
    import Login_Window

# Function to register user
def register():
    global username
    global password
    username = username_entry.get()
    password = password_entry.get()
    
    if len(username) != 0 and len(password) != 0:
        try:
            # Encrypt password before storing in Firebase
            encoded_text = cipher_suite.encrypt(password.encode())
            
            # Store username and encrypted password in Firebase
            firebase.put('/', username, encoded_text.decode())  # Store as string
            
            # Clear input fields after successful registration
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            
            # Provide feedback to user
            messagebox.showinfo('Success', 'Successfully Registered, you may now Log In')
            
            # Delay and switch to login window (replace with actual logic)
            time.sleep(1)
            login_window()
        except Exception as e:
            messagebox.showinfo('Error', f'Error: {str(e)}')
    else:
        messagebox.showinfo('Error', 'Please enter username and password')

# Create the registration window
registration_window = Tk()
registration_window.minsize(400, 400)
registration_window.maxsize(400, 400)

label0 = Label(registration_window,text="My Study App",font=(
    "Sans Comic MS", 20, "bold"), bg="#f0f0f0", fg="black")
label0.place(relx=0.5,rely=0.1,anchor=CENTER)    

heading_label = Label(
    registration_window, text="Register", font='arial 18 bold')
heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

username_label = Label(
    registration_window, text="Username : ", font='arial 13')
username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

password_label = Label(
    registration_window, text="Password :  ", font='arial 13')
password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window, show="*")
password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up",
                 font='arial 13 bold', command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5, rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In",
                          font='arial 10 bold',  command=login_window, relief=FLAT)
btn_login_window.place(relx=0.9, rely=0.06, anchor=CENTER)

b = Checkbutton(registration_window, command=change1)
b.place(relx=0.8, rely=0.5, anchor=CENTER)

registration_window.mainloop()
