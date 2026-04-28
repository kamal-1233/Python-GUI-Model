from tkinter import *
from PIL import Image, ImageTk

def signup(root):
    root.withdraw()  # hide main window

    signup_window = Toplevel(root)
    signup_window.geometry("1100x700+400+100")
    signup_window.title("Create An Account")
    signup_window.resizable(False, False)

    # -- Background Image --
    bg_image = Image.open("images/test.png")
    bg_image = bg_image.resize((1100, 700), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(signup_window, image=bg_photo)
    bg_label.place(x=0, y=0)
    bg_label.image = bg_photo  # important

    # --- Close Button Handling ---
    def on_closing():
        signup_window.destroy()
        root.deiconify()  # show main window again

# --- UserName , Useremail , Gender , Address, State , Password 
#  

    signup_window.protocol("WM_DELETE_WINDOW", on_closing)