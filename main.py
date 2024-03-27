import os
import sqlite3
import customtkinter
from PIL import Image


my_app = customtkinter.CTk()
my_app.title("Login")
my_app.config(bg="cyan")

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 13, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 23, 'bold', 'underline')

# Create database
conn = sqlite3.connect('login.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS login(Username TEXT NOT NULL, Password TEXT NOT NULL)")

# Create the form
For_Frame1 = customtkinter.CTkFrame(my_app, bg_color='cyan', fg_color='red', width=650, height=390)
For_Frame1.place(x=0, y=0)

# Load image
image_path = os.path.join(os.path.dirname(__file__), 'myimg.jpg ')
For_Image1 = customtkinter.CTkImage(light_image=Image.open(image_path), size=(50, 50))
For_Image1_label = customtkinter.CTkLabel(my_app, image=For_Image1,  bg="#001220")
For_Image1_label.place(x=0, y=0)

# create signup form

SignUp_Label = customtkinter.CTkLabel(For_Frame1, font=font1, text_color="#fff", bg_color="#001200")
User_entry = customtkinter.CTkEntry(For_Frame1, font=font2, text_color="#fff",
                                    bg_color="#121111", border_color="#004780",
                                    border_width=3, placeholder_text="Username",
                                    placeholder_text_color="#a3a3a3", width=200, height=50)
User_entry.place(x=230, y=80)
password_entry = customtkinter.CTkEntry(For_Frame1, font=font2, show="*", text_color="#fff",
                                        fg_color="#001a2e", bg_color="#121111", border_color="#004780",
                                        border_width=3, placeholder_text="Password",
                                        placeholder_text_color="green", width=200, height=50)

password_entry.place(x=230, y=150)

signUp_button = customtkinter.CTkButton(For_Frame1, font=font3, text_color="#fff", text='signup',
                                        fg_color="#00965d", hover_color="#006c44", bg_color="cyan",
                                        cursor="hand2", corner_radius=5, width=120)
signUp_button.place(x=230, y=220)

login_label = customtkinter.CTkLabel(For_Frame1, font=font4, text="Already have an account?", text_color="#fff",
                                     bg_color="red")
login_label.place(x=230, y=250)

login_button = customtkinter.CTkButton(For_Frame1, font=font4, text_color="#006f77", text="login",
                                       fg_color="#001220", cursor="hand2", width=40)
login_button.place(x=550, y=250)


if __name__ == '__main__':
    my_app.mainloop()
