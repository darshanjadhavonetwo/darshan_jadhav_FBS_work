from tkinter import *

def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


window = Tk()
window.title("Calculator")

entry = Entry(window, width=25, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

btn1 = Button(window, text="1", width=5, height=2, command=lambda: button_click(1))
btn1.grid(row=1, column=0)

btn2 = Button(window, text="2", width=5, height=2, command=lambda: button_click(2))
btn2.grid(row=1, column=1)

btn3 = Button(window, text="3", width=5, height=2, command=lambda: button_click(3))
btn3.grid(row=1, column=2)

btn4 = Button(window, text="4", width=5, height=2, command=lambda: button_click(4))
btn4.grid(row=1, column=3)

btn_plus = Button(window, text="+", width=5, height=2, command=lambda: button_click("+"))
btn_plus.grid(row=1, column=4)

btn5 = Button(window, text="5", width=5, height=2, command=lambda: button_click(5))
btn5.grid(row=2, column=0)

btn6 = Button(window, text="6", width=5, height=2, command=lambda: button_click(6))
btn6.grid(row=2, column=1)

btn7 = Button(window, text="7", width=5, height=2, command=lambda: button_click(7))
btn7.grid(row=2, column=2)

btn8 = Button(window, text="8", width=5, height=2, command=lambda: button_click(8))
btn8.grid(row=2, column=3)

btn_minus = Button(window, text="-", width=5, height=2, command=lambda: button_click("-"))
btn_minus.grid(row=2, column=4)


btn9 = Button(window, text="9", width=5, height=2, command=lambda: button_click(9))
btn9.grid(row=3, column=0)

btn10 = Button(window, text="0", width=5, height=2, command=lambda: button_click(0))
btn10.grid(row=3, column=1)

btn00 = Button(window, text="00", width=5, height=2, command=lambda: button_click("00"))
btn00.grid(row=3, column=2)

btn_mul = Button(window, text="*", width=5, height=2, command=lambda: button_click("*"))
btn_mul.grid(row=3, column=3)

btn_div = Button(window, text="/", width=5, height=2, command=lambda: button_click("/"))
btn_div.grid(row=3, column=4)


btn_clear = Button(window, text="C", width=5, height=2, command=button_clear)
btn_clear.grid(row=4, column=0)

btn_equal = Button(window, text="=", width=15, height=2, command=button_equal)
btn_equal.grid(row=4, column=1, columnspan=2)

btn_dot = Button(window, text=".", width=5, height=2, command=lambda: button_click("."))
btn_dot.grid(row=4, column=3)

btn_zero = Button(window, text="0", width=5, height=2, command=lambda: button_click(0))
btn_zero.grid(row=4, column=4)

window.mainloop()
