from tkinter import *
from PIL import Image, ImageTk
import newUser

myroot = Tk()
myroot.geometry("800x400+400+100")
myroot.title("Python-Interface")

# Background Image
bg_image = Image.open("images/Login.jpg")
bg_image = bg_image.resize((800, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(myroot, image=bg_photo)
bg_label.place(x=0, y=0)
bg_label.image = bg_photo

# ------- Login Frame ---------

# Shadow (fake shadow effect)
shadow_frame = Frame(myroot, bg="#cfcfcf")
shadow_frame.place(x=195, y=80, width=400, height=260)

# Main card
login_frame = Frame(myroot, bg='white')
login_frame.place(x=190, y=75, width=400, height=260)

# Heading
login_heading = Label(
    login_frame,
    text="Control Panel",
    font=("Segoe UI", 20, "bold"),
    bg="white",
    fg="#333"
)
login_heading.place(x=110, y=15)

# Email
email_label = Label(login_frame, text="Email", font=("Segoe UI", 11), bg="white", fg="#555")
email_label.place(x=40, y=70)

email_entry = Entry(login_frame, font=("Segoe UI", 12), width=25, bd=1, relief="solid")
email_entry.place(x=40, y=95)

# Password
password_label = Label(login_frame, text="Password", font=("Segoe UI", 11), bg="white", fg="#555")
password_label.place(x=40, y=130)

password_entry = Entry(login_frame, font=("Segoe UI", 12), width=25, bd=1, relief="solid", show="*")
password_entry.place(x=40, y=155)

# Login Button
login_button = Button(
    login_frame,
    text="Login",
    font=("Segoe UI", 11, "bold"),
    bg="#4a90e2",
    fg="white",
    activebackground="#357ABD",
    cursor="hand2",
    bd=0,
    width=12
)
login_button.place(x=60, y=205)

# New User Button
new_user_button = Button(
    login_frame,
    text="New User",
    font=("Segoe UI", 11, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    cursor="hand2",
    bd=0,
    width=12
)
new_user_button.place(x=200, y=205)

new_user_button.bind("<Button-1>", lambda k: newUser.signup(myroot))

myroot.mainloop()