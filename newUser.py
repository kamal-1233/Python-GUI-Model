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

    # -- Background Image --
    bg_image = Image.open("images/userFrom.jpg")
    bg_image = bg_image.resize((800, 450), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(signup_window, image=bg_photo)
    bg_label.place(x=0, y=0)
    bg_label.image = bg_photo

    # Shadow
    shadow = Frame(signup_window, bg="#cfcfcf")
    shadow.place(x=205, y=45, width=400, height=350)

    # Form Frame
    form_frame = Frame(signup_window, bg="white")
    form_frame.place(x=200, y=40, width=400, height=350)

    # Heading
    Label(form_frame, text="Create Account",
          font=("Segoe UI", 18, "bold"),
          bg="white", fg="#333").place(x=110, y=10)

    # Username
    Label(form_frame, text="Username", font=("Segoe UI", 10), bg="white", fg="#555").place(x=30, y=60)
    name_entry = Entry(form_frame, font=("Segoe UI", 11), width=25, bd=1, relief="solid")
    name_entry.place(x=150, y=60)

    # Email
    Label(form_frame, text="Email", font=("Segoe UI", 10), bg="white", fg="#555").place(x=30, y=95)
    email_entry = Entry(form_frame, font=("Segoe UI", 11), width=25, bd=1, relief="solid")
    email_entry.place(x=150, y=95)

    # Gender
    Label(form_frame, text="Gender", font=("Segoe UI", 10), bg="white", fg="#555").place(x=30, y=130)

    gender_var = StringVar(value="Male")

    Radiobutton(form_frame, text="Male", variable=gender_var, value="Male",
                bg="white", font=("Segoe UI", 10)).place(x=150, y=130)

    Radiobutton(form_frame, text="Female", variable=gender_var, value="Female",
                bg="white", font=("Segoe UI", 10)).place(x=230, y=130)

    # Address
    Label(form_frame, text="Address", font=("Segoe UI", 10), bg="white", fg="#555").place(x=30, y=165)
    address_box = Text(form_frame, font=("Segoe UI", 10), width=22, height=2,
                       bd=1, relief="solid")
    address_box.place(x=150, y=165)

    # State
    Label(form_frame, text="State", font=("Segoe UI", 10), bg="white", fg="#555").place(x=30, y=210)

    state_var = StringVar(value="Select State")
    state_options = ["Select State", "Himachal Pradesh", "Delhi",
                     "Haryana", "Rajasthan", "Chhattisgarh"]

    state_menu = OptionMenu(form_frame, state_var, *state_options)
    state_menu.config(font=("Segoe UI", 9), bg="white", width=18)
    state_menu.place(x=150, y=205)

    # Password
    Label(form_frame, text="Password", font=("Segoe UI", 10), bg="white", fg="#555").place(x=30, y=250)
    password_entry = Entry(form_frame, font=("Segoe UI", 11), width=25,
                           bd=1, relief="solid", show="*")
    password_entry.place(x=150, y=250)

    # 🔥 Save Function
    def save_user():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        address = address_box.get("1.0", END).strip()
        gender = gender_var.get()
        state = state_var.get()
        
        if name =="":
            messagebox.showerror("Error","Name is required")
        else:
            if email =="":
                messagebox.showerror("Error","Email is required")
            else:
                if "@" in email and "." in email:
                    if password=="":
                         messagebox.showerror("Error","Password is required")
                    else:
                      if gender=="":
                        messagebox.showerror("Error","Gender is required")
                      else:
                        if state=="Select State":
                            messagebox.showerror("Error","State is required")
                        else:
                            if address=="":
                                messagebox.showerror("Error","Address is required")
                            else:
                                try:
                                    #--env content
                                    mycursor.execute(q)
                                    mydb.commit()
                                    messagebox.showinfo("Success","Account Created Successfully")
                                    signup_window.destroy()
                                    root.deiconify()     
                                except Exception as e:
                                    messagebox.showerror("Error",e)                        
                else:                                              
                    messagebox.showerror("Error","Invaild email Format @and . must required")
                    
                        
                



    # Register Button
    Button(form_frame, text="Register",
           font=("Segoe UI", 11, "bold"),
           bg="#4a90e2", fg="white",
           activebackground="#357ABD",
           cursor="hand2", bd=0,
           width=18,
           command=save_user).place(x=110, y=300)

    # Close Handling
    def on_closing():
        signup_window.destroy()
        root.deiconify()

    signup_window.protocol("WM_DELETE_WINDOW", on_closing)