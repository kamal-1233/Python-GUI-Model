from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def welcome_window(root, username, emailid):
    root.withdraw()

    welcome_win = Toplevel(root)
    welcome_win.geometry("800x450+400+100")
    welcome_win.title("Employee Dashboard")
    welcome_win.resizable(False, False)

    # Background
    bg_image = Image.open("images/userFrom.jpg")
    bg_image = bg_image.resize((800, 450), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(welcome_win, image=bg_photo)
    bg_label.place(x=0, y=0)
    bg_label.image = bg_photo

    # Card
    card = Frame(welcome_win, bg="white")
    card.place(x=200, y=80, width=400, height=280)

    # Heading
    Label(card, text="Employee Dashboard",
          font=("Segoe UI", 18, "bold"),
          bg="white", fg="#333").place(x=90, y=10)

    # User Info
    Label(card, text=f"Name: {username}",
          font=("Segoe UI", 11), bg="white").place(x=50, y=60)

    Label(card, text=f"Email: {emailid}",
          font=("Segoe UI", 11), bg="white").place(x=50, y=85)

    # -------- FUNCTIONS --------

    def my_profile():
        messagebox.showinfo("My Profile",
                            f"Name: {username}\nEmail: {emailid}")

    def edit_profile():
        edit_win = Toplevel(welcome_win)
        edit_win.geometry("400x300")
        edit_win.title("Edit Profile")

        Label(edit_win, text="Update Name").pack(pady=5)
        name_entry = Entry(edit_win)
        name_entry.insert(0, username)
        name_entry.pack()

        Label(edit_win, text="Update Email").pack(pady=5)
        email_entry = Entry(edit_win)
        email_entry.insert(0, emailid)
        email_entry.pack()

        def save():
            messagebox.showinfo("Success", "Profile Updated (Demo)")
            edit_win.destroy()

        Button(edit_win, text="Save", command=save).pack(pady=10)

    def raise_complaint():
        comp_win = Toplevel(welcome_win)
        comp_win.geometry("400x300")
        comp_win.title("Raise Complaint")

        Label(comp_win, text="Subject").pack(pady=5)
        subject = Entry(comp_win)
        subject.pack()

        Label(comp_win, text="Description").pack(pady=5)
        desc = Text(comp_win, height=5)
        desc.pack()

        def submit():
            messagebox.showinfo("Success", "Complaint Submitted")
            comp_win.destroy()

        Button(comp_win, text="Submit", command=submit).pack(pady=10)

    def logout():
        welcome_win.destroy()
        root.deiconify()

    # -------- BUTTONS --------

    Button(card, text="My Profile",
           width=18, bg="#3498db", fg="white",
           command=my_profile).place(x=120, y=120)

    Button(card, text="Edit Profile",
           width=18, bg="#f39c12", fg="white",
           command=edit_profile).place(x=120, y=155)

    Button(card, text="Raise Complaint",
           width=18, bg="#9b59b6", fg="white",
           command=raise_complaint).place(x=120, y=190)

    Button(card, text="Logout",
           width=18, bg="red", fg="white",
           command=logout).place(x=120, y=225)