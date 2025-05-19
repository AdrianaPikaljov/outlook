import smtplib
import ssl
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog, messagebox
import random
from outlookmodul import *

aken = Tk()
aken.title("outlook")
aken.geometry("700x500")
aken.configure(bg="lightgrey")

aken.iconbitmap("outlook.ico")

# Väljad
pealkiri = Label(aken, text="OUTLOOK", font=("Comic Sans MS", 20), bg="lightgrey")
pealkiri.place(x=225, y=15)

label_email = Label(aken, text="EMAIL:", font=("Comic Sans MS", 18), bg="#2e8efe", fg="white")
label_email.place(x=15, y=60)
label_teema = Label(aken, text="TEEMA:", font=("Comic Sans MS", 18), bg="#2e8efe", fg="white")
label_teema.place(x=15, y=100)
label_lisa = Label(aken, text="LISA:", font=("Comic Sans MS", 18), bg="#2e8efe", fg="white")
label_lisa.place(x=15, y=378)
label_kiri = Label(aken, text="KIRI:", font=("Comic Sans MS", 18), bg="#2e8efe", fg="white")
label_kiri.place(x=15, y=250)

sisse1 = Entry(aken, font=("Comic Sans MS", 18), bg="white", fg="black", width=20)
sisse1.place(x=135, y=60)
sisse2 = Entry(aken, font=("Comic Sans MS", 18), bg="white", fg="black", width=20)
sisse2.place(x=135, y=100)
tekstikast = Text(aken, height=4, width=35, font=("Comic Sans MS", 14), bg="white", fg="black")
tekstikast.place(x=135, y=200)

l_lisatud = Label(aken, text="", font=("Comic Sans MS", 10), bg="lightgrey", fg="black")
l_lisatud.place(x=135, y=430)

# Nupud
Button(aken, text="LISA PILT", command=lambda: vali_pilt(l_lisatud), font=("Comic Sans MS", 14), bg="#2e8efe", fg="white").place(x=135, y=375)
Button(aken, text="SAADA", command=lambda: saada_kiri(sisse1.get(), sisse2.get(), tekstikast.get("1.0", END).strip()), font=("Comic Sans MS", 14), bg="#2e8efe", fg="white").place(x=480, y=375)

Button(aken, text="SALVESTA MUSTAND", command=lambda: save_to_file(sisse1.get(), sisse2.get(), tekstikast.get("1.0", END).strip()), font=("Comic Sans MS", 14), bg="lightgrey", fg="black").place(x=135, y=310)
Button(aken, text="PUHASTA KÕIK", command=lambda: [sisse1.delete(0, END), sisse2.delete(0, END), tekstikast.delete("1.0", END), l_lisatud.configure(text="")], font=("Comic Sans MS", 14), bg="lightgrey", fg="black").place(x=490, y=310)
Button(aken, text="MUSTANDID", command=lambda: open_file_window(aken), font=("Comic Sans MS", 14), bg="lightgrey", fg="black").place(x=350, y=310)

aken.mainloop()
