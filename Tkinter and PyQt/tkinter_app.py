import tkinter as tk
from tkinter import messagebox, ttk

def convert():
    try:
        val = float(entry.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = val
        elif from_unit == "Цельсий":
            if to_unit == "Фаренгейт":
                result = val * 9/5 + 32
            else:
                result = val + 273.15
        elif from_unit == "Фаренгейт":
            if to_unit == "Цельсий":
                result = (val - 32) * 5/9
            else:
                result = (val - 32) * 5/9 + 273.15
        else:
            if to_unit == "Цельсий":
                result = val - 273.15
            else:
                result = (val - 273.15) * 9/5 + 32

        lbl_result.config(text=f"Результат: {result:.2f} {to_unit}")
        
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректное число.")

root = tk.Tk()
root.title("Конвертер температур (Tkinter)")
root.geometry("350x250")

lbl_title = tk.Label(root, text="Введите температуру:", font=("Arial", 12))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

entry = tk.Entry(root, width=15)
entry.grid(row=1, column=0, columnspan=2, pady=5)

combo_from = ttk.Combobox(root, values=["Цельсий", "Фаренгейт", "Кельвин"], state="readonly", width=12)
combo_from.set("Цельсий")
combo_from.grid(row=2, column=0, pady=10, padx=10)

combo_to = ttk.Combobox(root, values=["Цельсий", "Фаренгейт", "Кельвин"], state="readonly", width=12)
combo_to.set("Фаренгейт")
combo_to.grid(row=2, column=1, pady=10, padx=10)

btn_convert = tk.Button(root, text="Конвертировать", command=convert, bg="#4CAF50", fg="white")
btn_convert.grid(row=3, column=0, columnspan=2, pady=15)

lbl_result = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"))
lbl_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
