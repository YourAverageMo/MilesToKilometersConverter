from tkinter import *


def calc():
    result["text"] = round(float(input.get()) * 1.609344, 2)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 16))
miles.grid(column=2, row=0)

equal = Label(text="is equal to", font=("Arial", 16))
equal.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 16))
result.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 16))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calc)
button.grid(column=1, row=2)


window.mainloop()
