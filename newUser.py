from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

def signup(root):
    root.withdraw()

    signup_window = Toplevel(root)
    signup_window.geometry("800x450+400+100")
    signup_window.title("Create An Account")
    signup_window.resizable(False, False)

    # Background Image
    bg_image = Image.open("images/userFrom.jpg")
    bg_image = bg_image.resize((800, 450), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(signup_window, image=bg_photo)
    bg_label.place(x=0, y=0)
    bg_label.image = bg_photo

    # Shadow
    Frame(signup_window, bg="#cfcfcf").place(x=205, y=45, width=400, height=350)

    # Form
    form_frame = Frame(signup_window, bg="white")
    form_frame.place(x=200, y=40, width=400, height=350)

    Label(form_frame, text="Create Account",
          font=("Segoe UI", 18, "bold"),
          bg="white", fg="#333").place(x=110, y=10)

    # Inputs
    name_entry = Entry(form_frame, font=("Segoe UI", 11), width=25)
    email_entry = Entry(form_frame, font=("Segoe UI", 11), width=25)
    password_entry = Entry(form_frame, font=("Segoe UI", 11), width=25, show="*")
    address_box = Text(form_frame, font=("Segoe UI", 10), width=22, height=2)

    gender_var = StringVar(value="Male")
    state_var = StringVar(value="Select State")

    # Labels
    Label(form_frame, text="Username", bg="white").place(x=30, y=60)
    name_entry.place(x=150, y=60)

    Label(form_frame, text="Email", bg="white").place(x=30, y=95)
    email_entry.place(x=150, y=95)

    Label(form_frame, text="Gender", bg="white").place(x=30, y=130)
    Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", bg="white").place(x=150, y=130)
    Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", bg="white").place(x=230, y=130)

    Label(form_frame, text="Address", bg="white").place(x=30, y=165)
    address_box.place(x=150, y=165)

    Label(form_frame, text="State", bg="white").place(x=30, y=210)
    OptionMenu(form_frame, state_var,
               "Select State", "Himachal Pradesh", "Delhi",
               "Haryana", "Rajasthan", "Chhattisgarh").place(x=150, y=205)

    Label(form_frame, text="Password", bg="white").place(x=30, y=250)
    password_entry.place(x=150, y=250)

    # 🔥 Save Function (Clean)
    def save_user():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        address = address_box.get("1.0", END).strip()
        gender = gender_var.get()
        state = state_var.get()

        # Validation
        if not name:
            messagebox.showerror("Error", "Name is required")
            return

        if not email:
            messagebox.showerror("Error", "Email is required")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email format")
            return

        if not password:
            messagebox.showerror("Error", "Password is required")
            return

        if state == "Select State":
            messagebox.showerror("Error", "Select a state")
            return

        if not address:
            messagebox.showerror("Error", "Address is required")
            return

        # DB Insert
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kamal@1224",
                database="Python_GuiDb"
            )

            cursor = mydb.cursor()

            q = """INSERT INTO newuser 
                   (name, email, password, gender, state, address) 
                   VALUES (%s,%s,%s,%s,%s,%s)"""

            cursor.execute(q, (name, email, password, gender, state, address))
            mydb.commit()

            messagebox.showinfo("Success", "Account Created Successfully")

            cursor.close()
            mydb.close()

            signup_window.destroy()
            root.deiconify()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    Button(form_frame, text="Register",
           bg="#4a90e2", fg="white",
           cursor="hand2",
           command=save_user).place(x=150, y=300)

    def on_closing():
        signup_window.destroy()
        root.deiconify()

    signup_window.protocol("WM_DELETE_WINDOW", on_closing)