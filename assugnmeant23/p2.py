from tkinter import *

rates = {"USD": 1.0, "INR": 74.5,"EUR": 0.85}

def convert():
    amount_str = entery1.get()
    from_curr = entery2.get().upper()
    to_curr = entery3.get().upper()

    if amount_str.replace(".", "", 1).isdigit():
        amount = float(amount_str)

        if from_curr in rates and to_curr in rates:
            converted = amount * rates[to_curr] / rates[from_curr]
            result_label.config(text=f"Converted Amount: {converted:.2f} {to_curr}")
        else:
            result_label.config(text="Invalid currency code!")
    else:
        result_label.config(text="Please enter a valid number")

if __name__ == "__main__":
    window = Tk()
    window.geometry("400x300")
    window.config(bg="light blue")
    window.title("Currency Converter")

    text1 = Label(window, text="Amount:", bg="light blue")
    entery1 = Entry(window)

    text2 = Label(window, text="From Currency (USD/INR/EUR):", bg="light blue")
    entery2 = Entry(window)

    text3 = Label(window, text="To Currency (USD/INR/EUR):", bg="light blue")
    entery3 = Entry(window)

    btn = Button(window, text="Convert", command=convert)
    result_label = Label(window, text="", bg="light blue", font=("Arial", 12))


    text1.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    entery1.grid(row=1, column=2, pady=5)

    text2.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    entery2.grid(row=2, column=2, pady=5)

    text3.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    entery3.grid(row=3, column=2, pady=5)

    btn.grid(row=4, column=2, pady=10)
    result_label.grid(row=5, column=1, columnspan=2, pady=10)

    window.mainloop()
