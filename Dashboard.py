from tkinter import *
from PIL import Image, ImageTk

def welcome_window(root, username, emailid):
    root.withdraw()

    welcome_win = Toplevel(root)
    welcome_win.geometry("800x450+400+100")
    welcome_win.title("Welcome: " + emailid)
    welcome_win.resizable(False, False)

    # -- Background Image --
    bg_image = Image.open("images/userFrom.jpg")
    bg_image = bg_image.resize((800, 450), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(welcome_win, image=bg_photo)
    bg_label.place(x=0, y=0)
    bg_label.image = bg_photo

    # 🔥 Card (center box)
    card = Frame(welcome_win, bg="white")
    card.place(x=200, y=120, width=400, height=200)

    # Welcome Heading
    Label(card, text="Welcome",
          font=("Segoe UI", 20, "bold"),
          bg="white", fg="#333").place(x=140, y=20)

    # Username
    Label(card, text=f"Name: {username}",
          font=("Segoe UI", 12),
          bg="white").place(x=50, y=80)

    # Email
    Label(card, text=f"Email: {emailid}",
          font=("Segoe UI", 12),
          bg="white").place(x=50, y=110)

    # Logout Button
    def logout():
        welcome_win.destroy()
        root.deiconify()

    Button(card, text="Logout",
           font=("Segoe UI", 11, "bold"),
           bg="red", fg="white",
           cursor="hand2",
           command=logout).place(x=150, y=150)