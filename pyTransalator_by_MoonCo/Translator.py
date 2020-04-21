import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import os




def getSomeText():
    res = txt.get(1.0, END)
    res1 = combo.get()
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = "trnsl.1.1.20191004T184614Z.d34ab526c102883d.b36cdff4bbe3aa7cceeca10188e9e8464ee0c7aa"
    text = res
    lang = res1

    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})

    result = json.loads(r.text)
    txt.delete(1.0, END)

    txt.insert(END, ', '.join(result['text']))



def clear():
    list1 = window.pack_slaves()
    for l in list1:
        l.destroy()

def clicked():
    clear()
    global txt
    txt = scrolledtext.ScrolledText(window, width=40, height=10)
    txt.insert(INSERT, 'Write your request')
    txt.pack()
    global combo
    combo = Combobox(window)
    combo['values'] = ("ru-en", "en-ru", "tr-ru", "ru-tr")
    combo.current(0)
    combo.pack(side=RIGHT, padx=5, pady=5)
    btn1 = Button(window, image=image1, command=getSomeText, bd=0)
    btn1.pack(pady=10)
    panel1 = Label(window, image = image2, bd=0)
    panel1.pack(side=LEFT)



window = Tk()
window.title("Translator")
window.geometry('315x400')
img = ImageTk.PhotoImage(Image.open("translatorLogo.jpg"))
panel = Label(window, image = img, bd=0)
panel.pack()
image = ImageTk.PhotoImage(file="logoButton.jpg")
window["bg"] = "white"
image1 = ImageTk.PhotoImage(file="logoButton2.jpg")
image2 = ImageTk.PhotoImage(file="logoPicture.jpg")
btn = Button(window, image=image, bd=0, command=clicked)
btn.pack(pady = 50)
window.mainloop()
