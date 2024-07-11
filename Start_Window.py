from tkinter import *
import time

root = Tk()
root.minsize(600, 400)
root.maxsize(600, 400)
root.title('Welcome')
root.configure(background="#f0f0f0")

x = 0
y = 0

# For creating delay


def destroy1():
    global x
    if(x <= 2):
        x = x + 1
    else:
        root.destroy()
        import Login_Window
    delay1()


def delay1():
    root.after(500, destroy1)


def destroy2():
    global y
    if(y <= 2):
        y = y + 1
    else:
        root.destroy()
        import Registration_Window
    delay2()


def delay2():
    root.after(500, destroy2)
# For estroying the window to changing window


def login():
    root.after(500, destroy1)


def signup():
    root.after(500, destroy2)


# GUI
label0 = Label(root,text="My Study App",font=(
    "Sans Comic MS", 20, "bold"), bg="#f0f0f0", fg="black")
label0.place(relx=0.5,rely=0.18,anchor=CENTER)    

label1 = Label(root, text="Welcome!", font=(
    "Sans Comic MS", 20, "bold"), bg="#f0f0f0", fg="black")
label1.place(relx=0.5, rely=0.3, anchor=CENTER)

label2 = Label(root, text="If you have an account, proceed with Login in.\nOtherwise please proceed with Sign Up", font=(
    "Sans Comic MS", 14, "bold"), bg="#f0f0f0", fg="black")
label2.place(relx=0.5, rely=0.5, anchor=CENTER)

button_login = Button(root, text="Login", bg="red", fg="white", relief=FLAT, font=(
    "Sans Comic MS", 14, "bold"), command=login)
button_login.place(relx=0.3, rely=0.7, anchor=CENTER)

button_signup = Button(root, text="Sign Up", bg="green",
                       fg="white", relief=FLAT, font=(
                           "Sans Comic MS", 14, "bold"), command=signup)
button_signup.place(relx=0.7, rely=0.7, anchor=CENTER)

root.mainloop()
