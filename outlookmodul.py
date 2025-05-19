import smtplib
import ssl
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog, messagebox
import random

file = None
thems_fail = "thems.txt"

def vali_pilt(label):
    global file
    file = filedialog.askopenfilename(title="Vali fail", filetypes=[("Kõik failid", "*.*")])
    label.configure(text=file)
    return file

def save_to_file(kellele, teema, kiri, file_name=None):
    with open(thems_fail, "a", encoding="utf-8") as f:
        f.write(f"e-post: {kellele}, teema: {teema}, kiri: {kiri}\n")
        if file_name:
            f.write(f"Manus: {file_name}\n")

def saada_kiri(kellele, teema, kiri):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "pikaljovadri@gmail.com"
    salasõna = "" 

    msg = EmailMessage()
    msg["Subject"] = teema
    msg["From"] = kellelt
    msg["To"] = kellele

    msg.set_content(kiri)
    msg.add_alternative(f"""
    <html><body><h1 style="color:#ff0000;">{teema}</h1><p>{kiri}</p></body></html>
    """, subtype="html")

    if file:
        try:
            with open(file, "rb") as f:
                data = f.read()
                msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=f.name.split("/")[-1])
        except Exception as e:
            messagebox.showerror("Viga", f"Manust ei saanud lisada:\n{e}")
            return

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(kellelt, salasõna)
            server.send_message(msg)
        messagebox.showinfo("Saadetud", "Kiri saadetud edukalt!")
    except Exception as e:
        messagebox.showerror("Saatmise viga", f"{e}")

def open_file_window(parent):
    try:
        with open(thems_fail, "r", encoding="utf-8") as f:
            content = f.read()
        win = Toplevel(parent)
        win.title("Mustandid")
        win.geometry("600x400")
        txt = Text(win, wrap=WORD, font=("Comic Sans MS", 12))
        txt.pack(padx=10, pady=10)
        txt.insert(END, content)
        txt.config(state=DISABLED)
    except:
        messagebox.showerror("Viga", "Faili ei saa avada")
