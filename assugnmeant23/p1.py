from tkinter import *
from tkinter import messagebox 

def main():
    username = entery1.get()
    password = entery2.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Login is successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

if __name__ == '__main__':
    window = Tk()
    window.geometry("400x400")
    window.title("Login Page")

    text1 = Label(window, text="Enter the username:")
    entery1 = Entry(window)

    text2 = Label(window, text="Enter the password:")
    entery2 = Entry(window)

    btn = Button(window, text="LOGIN", command=main)

    text1.grid(row=1, column=1)
    entery1.grid(row=1, column=2)
    text2.grid(row=2, column=1)
    entery2.grid(row=2, column=2)
    btn.grid(row=3, column=1, columnspan=2)

    window.mainloop()
