from tkinter import *
from PIL import Image, ImageTk

def signup(root):
    root.withdraw()

    signup_window = Toplevel(root)
    signup_window.geometry("800x400+400+100")
    signup_window.title("Create An Account")
    signup_window.resizable(False, False)

    # -- Background Image --
    bg_image = Image.open("images/userFrom.jpg")
    bg_image = bg_image.resize((800, 400), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(signup_window, image=bg_photo)
    bg_label.place(x=0, y=0)
    bg_label.image = bg_photo

    # ------- Form Card ---------
    form_frame = Frame(signup_window, bg="white")
    form_frame.place(x=200, y=40, width=400, height=320)

    # Heading
    heading = Label(form_frame, text="New User", font=("Segoe UI", 20, "bold"), bg="white")
    heading.place(x=120, y=10)

    # Username
    Label(form_frame, text="Username", font=("Segoe UI", 11), bg="white").place(x=30, y=60)
    Entry(form_frame, font=("Segoe UI", 12), width=25).place(x=150, y=60)

    # Email
    Label(form_frame, text="Email", font=("Segoe UI", 11), bg="white").place(x=30, y=100)
    Entry(form_frame, font=("Segoe UI", 12), width=25).place(x=150, y=100)

    # Gender
    gender_label = Label(form_frame, text="Gender", font=("Segoe UI", 11), bg="white")
    gender_label.place(x=30, y=140)

    gender_var = StringVar()
    gender_var.set("Male")  # default

    gender_male = Radiobutton(
    form_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    bg="white",
    font=("Segoe UI", 10)
)
    gender_male.place(x=150, y=140)

    gender_female = Radiobutton(
    form_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    bg="white",
    font=("Segoe UI", 10)
)
    gender_female.place(x=230, y=140)

    # State
    state_label = Label(form_frame, text="State", font=("Segoe UI", 11), bg="white")
    state_label.place(x=30, y=200)

    state_var = StringVar()
    state_var.set("Select State")

    state_options = [
    "Select State",
    "Himachal Pradesh",
    "Delhi",
    "Haryana",
    "Rajasthan",
    "Chhattisgarh"
]

    state_menu = OptionMenu(form_frame, state_var, *state_options)
    state_menu.config(font=("Segoe UI", 10), bg="white", width=18)
    state_menu.place(x=150, y=195)
    
    # Address
    address_label = Label(form_frame, text="Address", font=("Segoe UI", 11), bg="white")
    address_label.place(x=30, y=170)

    address_box = Text(
    form_frame,
    font=("Segoe UI", 11),
    width=22,
    height=3,
    bd=1,
    relief="solid"
)
    address_box.place(x=150, y=170)
    
    # Submit Button
    Button(form_frame, text="Register",
           font=("Segoe UI", 11, "bold"),
           bg="#4a90e2", fg="white",
           cursor="hand2", bd=0).place(x=150, y=280)

    # --- Close Button Handling ---
    def on_closing():
        signup_window.destroy()
        root.deiconify()

    signup_window.protocol("WM_DELETE_WINDOW", on_closing)