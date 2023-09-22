from math import *
from tkinter import *
import random
from itertools import repeat
import string

root = Tk()
root.title("Lucidblu Password Master")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.configure(bg="black")

warning = Label(root, text="Work in progress\nMore apps available at lucidblu.rf.gd\nMade by lucidblu\n")
warning.grid(column=1, row=0)

app_label = Label(root, text="App / Website:")
app_label.grid(column=0, row=1)
app_label_field = Entry()
app_label_field.grid(column=1, row=1)

username_label = Label(root, text="Username:")
username_label.grid(column=0, row=2)
username_label_field = Entry()
username_label_field.grid(column=1, row=2)

password_label = Label(root, text="Password:")
password_label.grid(column=0, row=3)
password_label_field = Entry()
password_label_field.grid(column=1, row=3)

def quit():
    print(app_label_field.get())
    print(username_label_field.get())
    print(password_label_field.get())
    root.quit()
def write_to_file():
    password = password_label_field.get()
    password = str.encode(password)
    password2 = str(password)
    password2 = password2.replace('b', '')
    passwords = open("passwords.txt", "a")
    passwords.write(str(app_label_field.get()))
    passwords.write(" ")
    passwords.write(str(username_label_field.get()))
    passwords.write(" ")
    passwords.write(str(password2))
    passwords.write("109232")
    passwords.close()
def read_file():
    check = open("passwords.txt", "r")
    check = check.read()
    if check == "":
        print("No saved passwords")
    else:
        with open("passwords.txt") as f:
            contents = str(f.readlines())
            contents = contents.replace(',', '')
            contents = contents.replace("'", '')
            contents = contents.replace('[', '')
            contents = contents.replace(']', '')
            contents = contents.replace('"', '')
            contents = contents.replace('109232', '\n')
            print(contents)
    top = Toplevel(root)
    top.geometry("800x300")
    top.title("Generated Password")
    listPasswords = Label(top, text=contents)
    listPasswords.grid(column=0, row=0)
    quitPopup = Button(top, text="Quit", command=quitPopup)
    quitPopup.grid(column=0, row=1)
def generatePasswordPopup():
    def quitPopup():
        root.quit()
    def insertGeneratedPassword():
        password_label_field.delete(0, "end")
        password_label_field.insert(0, endPassList)
    top = Toplevel(root)
    complexityInput = popup_Label_field.get()
    passNumberList = []
    passLetterList = []
    endPassList = []
    for i in range(int(complexityInput)):
        passGenNumber = random.randrange(9)
        passGenLetter = random.choice(string.ascii_letters)
        passNumberList.append(passGenNumber)
        passLetterList.append(passGenLetter)
        endPassList.append(random.choice(str(passGenNumber) + passGenLetter))
    endPassList = str(endPassList)
    endPassList = endPassList.replace(',', '')
    endPassList = endPassList.replace("'", '')
    endPassList = endPassList.replace('[', '')
    endPassList = endPassList.replace(']', '')
    endPassList = endPassList.replace('"', '')
    endPassList = endPassList.replace(' ', '')
     # top.geometry("750x250")
    screen_width = top.winfo_screenwidth()
    screen_width = screen_width / 15
    screen_height = top.winfo_screenheight()
    screen_height = screen_height / 10
    top.title("Generated Password")
    generatedPasswordLabel = Label(top, text=endPassList)
    generatedPasswordLabel.grid(column=0, row=0)
    quitPopup = Button(top, text="Quit", command=quitPopup)
    quitPopup.grid(column=0, row=1)
    insertPassword = Button(top, text="Set as password", command=insertGeneratedPassword)
    insertPassword.grid(column=1, row=1)

submit_button = Button(root, text="Quit", command=quit)
submit_button.grid(column=0, row=21)
write_button = Button(root, text="Write to files", command=write_to_file)
write_button.grid(column=1, row=21)
read_button = Button(root, text="Read saved passwords", command=read_file)
read_button.grid(column=2, row=21)

warning.configure(fg="white", bg="black")
app_label.configure(fg="white", bg="black")
app_label_field.configure(fg="white", bg="black")
username_label.configure(fg="white", bg="black")
username_label_field.configure(fg="white", bg="black")
password_label.configure(fg="white", bg="black")
password_label_field.configure(fg="white", bg="black")
submit_button.configure(fg="white", bg="black")
write_button.configure(fg="white", bg="black")
read_button.configure(fg="white", bg="black")

root.mainloop()
