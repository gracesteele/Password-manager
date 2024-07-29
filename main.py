from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    info_to_save = f"{website} | {email} | {password}"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning("Oops", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                      f"Email: {email} \n"
                                                      f"Password: {password} \n"
                                                      f"Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as save_file:
                save_file.write(f"{info_to_save}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input = Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "gssteeleuk@gmail.com")

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# Buttons
gen_password = Button(text="Generate Password")
gen_password.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
