import requests
from tkinter import *
from tkinter import messagebox
import getpass


root = Tk()
root.title("Requests")
root.geometry("400x400")


def request():
    response = requests.get('https://v6.exchangerate-api.com/v6/fac9f0aa288dff6d0a7c7a88/latest/USD')
    text = response.json()
    print(text)
    conversion_rates = text['conversion_rates'].keys()
    CurList = Listbox(root)
    CurList.place(x=170, y=120)
    for i in conversion_rates:
        CurList.insert(END, str(i))

    dict_Currency = float(edtCurs.get()) * text['conversion_rates'][CurList.get(ACTIVE)]
    answer = float(dict_Currency) * float(edtCurs.get())
    print(answer)
    # for i in dict_Currency.keys():
    #     if i == edtCurrency.get():
    #         messagebox.showinfo("working", "its working")
    #val = edtCurrency.get().upper()
    # dict_Currency = text['conversion_rates'][val]


lblTitle = Label(root, text="choose the currency")
lblTitle.place(x=55, y=80)
edtUSD = Entry(root, width=10)
edtUSD.place(x=40, y=100)

lblCurs = Label(root, text="USD")
lblCurs.place(x=185, y=80)
edtCurs = Entry(root, width=10)
edtCurs.place(x=170, y=100)
#
btn1 = Button(root, text="CONVERT", command=request)
btn1.place(x=105, y=300)
#

root.mainloop()
