# Errors, Exceptions and JSON Data

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password_generated = ''.join(password_list)
    password_entry.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            # Update a JSON file:
            with open("data.json", mode="r") as data_file:
                # Step 1: Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Step 2: Update new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Step 3: Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            # reset all fields
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            email_username_entry.insert(0, "nganguyen.ny@gmail.com")
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    website = website_entry.get()

    # Open JSON as 'data_file'
    try:
        with open("data.json", mode="r") as data_file:
            # Save content into a 'data' variable
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found")
    else:
        if website in data:
            # Search the key 'data["website"]' for the password value
            found_email = data[website]["email"]
            found_password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {found_email}\nPassword: {found_password}"
                                                       f"\n[Password was copied for use!]")
            pyperclip.copy(found_password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for the website {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.insert(0, "nganguyen.ny@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


def add_button_clicked():
    save()


search_button = Button(text="Search", width=12, command=search_password)
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(width=36, text="Add", command=add_button_clicked)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
