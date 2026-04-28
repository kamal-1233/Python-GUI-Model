from tkinter import *
from PIL import Image, ImageTk
import newUser

myroot = Tk()
myroot.geometry("700x400+400+100")
myroot.title("Kamal")

# Background Image
bg_image = Image.open("images/new1.jpg")
bg_image = bg_image.resize((700, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(myroot, image=bg_photo)
bg_label.place(x=0, y=0)
bg_label.image = bg_photo

# ------- Login Frame ---------
login_frame = Frame(myroot, bg='white', width=400, height=250)
login_frame.place(x=150, y=75)

# Heading
login_heading = Label(login_frame, text="C-Panel", font=("times new roman", 24, "bold"), bg="white")
login_heading.place(x=140, y=10)

# Email
email_label = Label(login_frame, text="Email", font=("times new roman", 14, "bold"), bg="white")
email_label.place(x=50, y=70)

email_entry = Entry(login_frame, font=("times new roman", 14), width=25)
email_entry.place(x=150, y=70)

# Password
password_label = Label(login_frame, text="Password", font=("times new roman", 14, "bold"), bg="white")
password_label.place(x=50, y=110)

password_entry = Entry(login_frame, font=("times new roman", 14), width=25, show="*")
password_entry.place(x=150, y=110)

# Login Button
login_button = Button(login_frame, text="Login",
                      font=("times new roman", 14, "bold"),
                      bg="blue", fg="white", cursor="hand2")
login_button.place(x=120, y=170)

# New User Button
new_user_button = Button(login_frame, text="New User",
                         font=("times new roman", 14, "bold"),
                         bg="green", fg="white", cursor="hand2")
new_user_button.place(x=220, y=170)
new_user_button.bind("<Button-1>", lambda k: newUser.signup(myroot))

myroot.mainloop()