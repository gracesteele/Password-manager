from tkinter import *
from tkinter import messagebox
import password
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.insert(0, password.generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file(data, filename):
    with open(filename, "w") as save_file:
        json.dump(data, save_file, indent=4)


def save_data():
    website = website_input.get()
    email = email_input.get()
    pass_word = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pass_word,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(pass_word) == 0:
        messagebox.showwarning("Oops", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email} \n"
                                                              f"Password: {pass_word} \n"
                                                              f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as save_file:
                    # Reading old data
                    data = json.load(save_file)
            except FileNotFoundError:
                write_to_file(new_data, "data.json")
            else:
                # Updating old data with new data
                data.update(new_data)

                write_to_file(data, "data.json")
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ------------------------- FIND PASSWORD ----------------------------- #
def find_password():
    try:
        with open("data.json", "r") as open_file:
            data = json.load(open_file)
    except FileNotFoundError:
        messagebox.showwarning("Oops", "No save data.")
    else:
        website = website_input.get()
        if website in data:
            email = data[website]["email"]
            pass_word = data[website]["password"]
            messagebox.showinfo(f"{website}",
                                f"Email: {email}\nPassword: {pass_word}")
        else:
            messagebox.showwarning("Oops", f"No details for {website} exists.")
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "gssteeleuk@gmail.com")

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# Buttons
gen_password = Button(text="Generate Password", width=14, command=password_generator)
gen_password.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
