from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
def trig_test(x, function_type):
    x = x / 180 * 3.1415
    q = x  
    s = 0  
    for i in range(1, 1000): 
        s += q
        q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i)) 
    try:
        if function_type == "sin":
            return round(s, 3)
        g = round(s, 3)  
        cos_x = (1 - g**2) ** 0.5
        if function_type == "cos":
            return round(cos_x, 3)
        if function_type == "tg":
            if cos_x == 0:  
                raise ZeroDivisionError("Тангенс не определён для данного угла.")
            return round(g / cos_x, 3)
        if function_type == "ctg":
            if g == 0:  
                raise ZeroDivisionError("Котангенс не определён для данного угла.")
            return round(cos_x / g, 3)
        raise ValueError("Неизвестный тип тригонометрической функции.")
    except ZeroDivisionError as e:
        return str(e)  
    except ValueError as e:
        return str(e)  
def convert_test(num, base):
    if base < 2 or base > 36:
        raise ValueError("Основание системы счисления должно быть в диапазоне от 2 до 36.")
    if num < 0:
        return '-' + convert_test(-num, base)
    elif num == 0:
        return '0'   
    digits = []
    while num:
        digits.append(int(num % base))
        num = num // base   
    if base > 10:
        for i in range(len(digits)):
            if digits[i] >= 10:
                digits[i] = chr(digits[i] - 10 + ord('A')) 
    return ''.join(str(x) for x in digits[::-1])
def factorial_test(x):
    if not isinstance(x, int):  
        raise ValueError
    if x < 0:  
        raise ValueError
    result_fact = 1
    for h in range(2, x + 1):
        result_fact *= h
    return result_fact
def process_base_conversion(base):
    calc_entry.insert(END, " = " + str(convert_test(int(calc_entry.get()), base)))
def process_trig_operation(operation):
    calc_entry.insert(END, " = " + str(trig_test(float(calc_entry.get()), operation)))
def calc(key):
    global Abs
    if key == "=":
        str_1 = "0123456789*)(/."
        if calc_entry.get()[0] not in str_1:
            messagebox.showerror("Ошибка!", "Введенные символы не являются числами или цифрами")
            return
        try:
            result = eval(calc_entry.get())
            Abs = result
            calc_entry.insert(END, " = " + str(result))
        except:
            calc_entry.insert(END, "Ошибка")
            messagebox.showerror("Ошибка!", "Неверное выражение!")
    elif key == "Del":
        calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "Abs":
        calc_entry.insert(END, str(Abs))
    elif key == "Exit":
        root.destroy()
        sys.exit()
    elif key in ["sin", "cos", "tg", "ctg"]:
        process_trig_operation(key)
    elif key == "x!":
        calc_entry.insert(END, " = " + str(fact_test(int(calc_entry.get()))))
    elif key in ["+", "-", "*", "/", "(", ")"]:
        calc_entry.insert(END, key)
    elif key in ["2-ная", "3-ная", "4-ная", "5-ная", "6-ная", "7-ная", "8-ная", "9-ная", "16-ная"]:
        process_base_conversion(int(key.split('-')[0]))
    elif key == "xⁿ":
        calc_entry.insert(END, "**") 
    else:
        calc_entry.insert(END, key)
root = Tk()
root.title("Calculator")
calc_entry = Entry(root, width=50)
calc_entry.grid(row=0, column=0, columnspan=5)
calc_icons = [
    "7", "8", "9", "+", "*", "4", "5", "6", "-", "/",
    "1", "2", "3", "=", "xⁿ", "0", ".", "Del", "ctg",
    "sin", "cos", "tg", "2-ная", "3-ная", "4-ная",
    "5-ная", "6-ная", "7-ная", "8-ная", "9-ная",
    "16-ная", "x!", "Abs", "(", ")", "Exit", "±"]
r, c = 1, 0
for i in calc_icons:
    cmd = lambda x=i: calc(x)
    button = ttk.Button(root, text=i, command=cmd, width=10)
    button.grid(row=r, column=c, sticky='nsew')
    c += 1
    if c > 4:
        c = 0
        r += 1
root.mainloop()    