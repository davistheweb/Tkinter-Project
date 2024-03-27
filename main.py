import os
import sqlite3
import customtkinter
# from PIL import Image


my_app = customtkinter.CTk()
my_app.title("Student Login")
my_app.geometry("400x400")

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 13, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 12, 'bold', 'underline')

# Create database
conn = sqlite3.connect('login.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS login(Username TEXT NOT NULL, Password TEXT NOT NULL)")

# Create the form
For_Frame1 = customtkinter.CTkFrame(my_app, bg_color='cyan', fg_color='cyan', width=600, height=390)
For_Frame1.place(x=0, y=0)

# Load image
'''''
image_path = os.path.join(os.path.dirname(__file__), 'myimg.jpg ')
For_Image1 = customtkinter.CTkImage(light_image=Image.open(image_path), size=(50, 50))
For_Image1_label = customtkinter.CTkLabel(my_app, image=For_Image1,  bg="#001220")
For_Image1_label.place(x=0, y=0)
'''''
# create signup form

# SignUp_Label = customtkinter.CTkLabel(For_Frame1, font=font1, text_color="#fff", bg_color="#001200")
User_entry = customtkinter.CTkEntry(For_Frame1, font=font2, text_color="#fff",
                                    bg_color="#121111", border_color="#004780",
                                    border_width=1, placeholder_text="Username",
                                    placeholder_text_color="#a3a3a3", width=200, height=50)
User_entry.place(x=100, y=80)

Password_entry = customtkinter.CTkEntry(For_Frame1, font=font2, show="*", text_color="#fff",
                                        bg_color="#121111", border_color="#004780",
                                        border_width=1, placeholder_text="Password",
                                        placeholder_text_color="#a3a3a3", width=200, height=50)

Password_entry.place(x=100, y=150)

SignUp_button = customtkinter.CTkButton(For_Frame1, font=font3, text_color="#fff", text='Signup',
                                        hover_color="#121111", bg_color="#121111",
                                        cursor="hand2", corner_radius=5,
                                        fg_color="#121111", width=200)
SignUp_button.place(x=100, y=220)

login_label = customtkinter.CTkLabel(For_Frame1, font=font4, text="Already have an account?", text_color="#fff",
                                     bg_color="#121111", padx=10)
login_label.place(x=100, y=270)

login_button = customtkinter.CTkButton(For_Frame1, font=font4, text_color="#fff", text="Login",
                                       fg_color="#121111", bg_color="#121111", hover_color="#121111",
                                       cursor="hand2", width=10)
login_button.place(x=270, y=270)


if __name__ == '__main__':
    my_app.mainloop()
