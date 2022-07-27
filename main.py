from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]
    generated_pass = pass_letters + pass_symbols + pass_numbers
    random.shuffle(generated_pass)
    str_pass = "".join(generated_pass)
    password_input.insert(0, str_pass)
    pyperclip.copy(str_pass)


def save_pass():
    website = website_input.get()
    u_email = user_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message='dont leave any of fields empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'you are entered:\n email: {u_email}\n password: {password}\n '
                                                      f'Click ok to save')
        if is_ok:
            with open('passwords.txt', 'a') as pass_file:
                pass_file.write(f'{website} | {u_email} | {password} \n')
                messagebox.showinfo(message='saving ok')
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
# ---------------------------- CANVAS ------------------------------- #
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# ---------------------------- LABELS & BUTTONS ------------------------------- #
label_website = Label(text='Website')
label_website.grid(column=0, row=1)
label_user = Label(text='Email/Username')
label_user.grid(column=0, row=2)
label_password = Label(text='Password')
label_password.grid(column=0, row=3)

website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
#website_get = website_input.get()

user_input = Entry(width=39)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, 'my_email@com')


password_input = Entry(width=30)
password_input.grid(column=1, row=3)

gen_button = Button(text='Generate', command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(width=33, text='Add', command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()