import requests
from tkinter import *
from tkinter import messagebox
import getpass


root = Tk()
root.title("CURRENCY CONVERTOR")
root.geometry("400x450")

response = requests.get('https://v6.exchangerate-api.com/v6/fac9f0aa288dff6d0a7c7a88/latest/USD')
text = response.json()
conversion_rates = text['conversion_rates'].keys()

def Clear():
    edtCurs.delete(0, END)
    edtUSD.delete(0, END)


def request():
    if edtUSD.get() != "":
        messagebox.showwarning("warning", "Clear the edits first")
    else:
        dict_Currency = float(edtCurs.get()) * text['conversion_rates'][CurList.get(ACTIVE)]
        edtUSD.insert(0, dict_Currency)


lblTitle = Label(root, text="USD")
lblTitle.place(x=80, y=80)
edtUSD = Entry(root, width=10)
edtUSD.place(x=70, y=100)

lbCurrency = Label(root, text="choose a currency")
lbCurrency.place(x=100, y=140)

CurList = Listbox(root)
CurList.place(x=100, y=180)
for i in conversion_rates:
    CurList.insert(END, str(i))

lblCurs = Label(root, text="Enter amount")
lblCurs.place(x=200, y=80)
edtCurs = Entry(root, width=10)
edtCurs.place(x=200, y=100)

btn1 = Button(root, text="CONVERT", command=request)
btn1.place(x=105, y=380)

btnClear = Button(root, text="CLEAR", command=Clear)
btnClear.place(x=200, y=380)

root.mainloop()
