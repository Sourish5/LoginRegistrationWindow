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

def signup_window():
    import Registration_Window
    login_window.destroy()

def change1():
    if login_password_entry['show'] == "*":
        login_password_entry['show'] = ""
    else:
        login_password_entry['show'] = "*"

def login():
    username = login_username_entry.get()
    password_entered = login_password_entry.get()

    if len(username) != 0 and len(password_entered) != 0:
        try:
            # Retrieve encrypted password from Firebase
            encoded_text = firebase.get('/', username)
            if encoded_text:
                # Decrypt the password and compare with entered password
                decoded_text = cipher_suite.decrypt(encoded_text.encode()).decode()
                if decoded_text == password_entered:
                    messagebox.showinfo('Success', 'Successfully Logged In')
                    login_username_entry.delete(0, END)
                    login_password_entry.delete(0, END)
                    time.sleep(1)
                    login_window.destroy()

                    # Open main application window (example)
                    root = Tk()
                    root.minsize(600, 400)
                    root.maxsize(600, 400)

                    labelx = Label(root,text="My Study App", font=("Comic Sans MS", 18, 'bold'), fg="black")
                    labelx.place(relx=0.5,rely=0.1,anchor=CENTER)

                    label_a = Label(root, text="Welcome " + username + "!",
                                    font=("Comic Sans MS", 18, 'bold'), fg="black")
                    label_a.place(relx=0.5, rely=0.5, anchor=CENTER)

                    root.mainloop()
                else:
                    messagebox.showinfo('Error', 'Incorrect username or password')
            else:
                messagebox.showinfo('Error', 'No username found')
        except Exception as e:
            messagebox.showinfo('Error', f'Error: {str(e)}')
    else:
        messagebox.showinfo('Error', 'Please enter username and password')

# Create the login window
login_window = Tk()
login_window.geometry("400x400")

label0 = Label(login_window,text="My Study App",font=(
    "Sans Comic MS", 20, "bold"), bg="#f0f0f0", fg="black")
label0.place(relx=0.5,rely=0.1,anchor=CENTER)    

log_heading_label = Label(
    login_window, text="Log In", font='arial 18 bold')
log_heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

login_username_label = Label(
    login_window, text="Username : ", font='arial 13')
login_username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

login_username_entry = Entry(login_window)
login_username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

login_password_label = Label(
    login_window, text="Password : ", font='arial 13')
login_password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

login_password_entry = Entry(login_window, show="*")
login_password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_login = Button(login_window, text="Log In",
                   font='arial 13 bold', relief=FLAT, command=login)
btn_login.place(relx=0.5, rely=0.7, anchor=CENTER)

btn_signup_window = Button(login_window, text="Sign Up",
                           font='arial 10 bold',  command=signup_window, relief=FLAT)
btn_signup_window.place(relx=0.9, rely=0.06, anchor=CENTER)

b = Checkbutton(login_window, command=change1)
b.place(relx=0.8, rely=0.5, anchor=CENTER)

login_window.mainloop()
