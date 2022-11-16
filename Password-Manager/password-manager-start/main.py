from tkinter import *
import string
import secrets

# ---------------------------- PASSWORD VIEWER ------------------------------- #
def view_pass():
    label = Label(window, text='this is the page2')
    label.place(relx=0.3, rely=0.4)
    win = Tk()
    win.mainloop()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    symbols = ['!', '@', '#', '$', '%', '^']  # Can add more

    password = ""

    for _ in range(3):
        password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(symbols)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open('data.txt', 'a') as data_file:
        data_file.write(f'{website} | {email} | {password}\n')
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username')
email_label.grid(column=0, row=2)
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'nhedgeworth@gmail.com')
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
generate_password_button = Button(text='Generate Password', width=30, command=gen_password)
generate_password_button.grid(column=1, row=5, columnspan=2)
add_button = Button(text='Add', width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)
view_password_button = Button(text='View Passwords', width=30, command=view_pass)
view_password_button.grid(column=1, row=6)






window.mainloop()
