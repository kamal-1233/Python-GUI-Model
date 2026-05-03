from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

def signup(root):
    root.withdraw()

    signup_window = Toplevel(root)
    signup_window.geometry("800x550+400+100")
    signup_window.title("Add Employee")
    signup_window.resizable(False, False)

    # Background
    bg_image = Image.open("images/userFrom.jpg")
    bg_image = bg_image.resize((800, 550), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    Label(signup_window, image=bg_photo).place(x=0, y=0)

    # Shadow
    Frame(signup_window, bg="#cfcfcf").place(x=205, y=45, width=400, height=450)

    # Form
    form_frame = Frame(signup_window, bg="white")
    form_frame.place(x=200, y=40, width=400, height=450)

    Label(form_frame, text="Add Employee",
          font=("Segoe UI", 18, "bold"),
          bg="white", fg="#333").place(x=120, y=10)

    # Entries
    name_entry = Entry(form_frame, width=25)
    email_entry = Entry(form_frame, width=25)
    password_entry = Entry(form_frame, width=25, show="*")
    phone_entry = Entry(form_frame, width=25)
    dept_entry = Entry(form_frame, width=25)
    salary_entry = Entry(form_frame, width=25)
    address_box = Text(form_frame, width=22, height=2)

    gender_var = StringVar(value="Male")
    state_var = StringVar(value="Select State")

    x1 = 40
    x2 = 150

    # Labels + Fields
    Label(form_frame, text="Name", bg="white").place(x=x1, y=60)
    name_entry.place(x=x2, y=60)

    Label(form_frame, text="Email", bg="white").place(x=x1, y=95)
    email_entry.place(x=x2, y=95)

    Label(form_frame, text="Password", bg="white").place(x=x1, y=130)
    password_entry.place(x=x2, y=130)

    Label(form_frame, text="Phone", bg="white").place(x=x1, y=165)
    phone_entry.place(x=x2, y=165)

    Label(form_frame, text="Department", bg="white").place(x=x1, y=200)
    dept_entry.place(x=x2, y=200)

    Label(form_frame, text="Salary", bg="white").place(x=x1, y=235)
    salary_entry.place(x=x2, y=235)

    Label(form_frame, text="Gender", bg="white").place(x=x1, y=270)
    Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", bg="white").place(x=x2, y=270)
    Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", bg="white").place(x=x2+80, y=270)

    Label(form_frame, text="State", bg="white").place(x=x1, y=305)
    OptionMenu(form_frame, state_var,
               "Select State", "Himachal Pradesh", "Delhi",
               "Haryana", "Rajasthan", "Chhattisgarh").place(x=x2, y=300)

    Label(form_frame, text="Address", bg="white").place(x=x1, y=340)
    address_box.place(x=x2, y=340)

    # 🔥 Save Employee
    def save_user():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        phone = phone_entry.get().strip()
        dept = dept_entry.get().strip()
        salary = salary_entry.get().strip()
        address = address_box.get("1.0", END).strip()
        gender = gender_var.get()
        state = state_var.get()

        # Validation
        if not name:
            messagebox.showerror("Error", "Name required")
            return
        if not email or "@" not in email:
            messagebox.showerror("Error", "Valid email required")
            return
        if not password:
            messagebox.showerror("Error", "Password required")
            return
        if not phone:
            messagebox.showerror("Error", "Phone required")
            return
        if not dept:
            messagebox.showerror("Error", "Department required")
            return
        if not salary.isdigit():
            messagebox.showerror("Error", "Salary must be number")
            return
        if state == "Select State":
            messagebox.showerror("Error", "Select state")
            return
        if not address:
            messagebox.showerror("Error", "Address required")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kamal@1224",
                database="Python_GuiDb"
            )
            cursor = db.cursor()

            q = """INSERT INTO newuser
            (name,email,password,gender,state,address,phone,department,salary)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            cursor.execute(q, (
                name, email, password, gender,
                state, address, phone, dept, salary
            ))

            db.commit()

            messagebox.showinfo("Success", "Employee Added Successfully")

            cursor.close()
            db.close()

            signup_window.destroy()
            root.deiconify()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    Button(form_frame, text="Add Employee",
           bg="#2ecc71", fg="white",
           width=18, command=save_user).place(x=130, y=400)

    def on_closing():
        signup_window.destroy()
        root.deiconify()

    signup_window.protocol("WM_DELETE_WINDOW", on_closing)