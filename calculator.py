import ttkbootstrap as ttk
from tkinter import messagebox
from tkinter.font import Font
from ttkbootstrap.constants import *

def calculate_tax():
    try:
        income = float(entry_income.get())
        percentaje = float(entry_percentage.get())
        total = income * (percentaje / 100)
        if income < 0 or percentaje < 0:
            messagebox.showwarning("Invalid Input", "Income and percentage must be positive.")
            return
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid numbers for income and percentage.")

def clear_fields():
    entry_income.delete(0, ttk.END)
    entry_percentage.delete(0, ttk.END)
    entry_total.delete(0, ttk.END)


root = ttk.Window(themename="darkly")
root.title("Tax Calculator ")

label_title = Font(font="Poppins", size=20, weight="bold")
label_text = Font(font="Poppins", size=10)

label_title = ttk.Label(root, text="Tex Calculator", font=label_title, anchor=CENTER)
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label_income = ttk.Label(root, text="Income:", font=label_text)
label_income.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_income = ttk.Entry(root, font=label_text)
entry_income.grid(row=1, column=1, padx=10, pady=5)

label_percentage = ttk.Label(root, text="Percentage:", font=label_text)
label_percentage.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_percentage = ttk.Entry(root, font=label_text)
entry_percentage.grid(row=2, column=1, padx=10, pady=5)

label_total = ttk.Label(root, text="Total:", font=label_text)
label_total.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_total = ttk.Entry(root, font=label_text, state="readonly")
entry_total.grid(row=3, column=1, padx=10, pady=5)

button_calculate = ttk.Button(root, text="Calculate", command=calculate_tax, bootstyle="success")
button_calculate.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="e")

button_clear = ttk.Button(root, text="Clear", command=clear_fields, bootstyle="danger")
button_clear.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="e")

root.mainloop()