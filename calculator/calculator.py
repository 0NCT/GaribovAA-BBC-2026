import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def floor_divide(a, b):
    """Целочисленное деление."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a // b

def remainder(a, b):
    """Остаток от деления."""
    if b == 0:
        raise ZeroDivisionError("Остаток от деления на ноль невозможен")
    return a % b

def power(a, b):
    return a ** b

def sqrt(a):
    """Квадратный корень."""
    if a < 0:
        raise ValueError("Корень из отрицательного числа не существует")
    return math.sqrt(a)

def absolute(a):
    """Модуль числа."""
    return abs(a)

def factorial(a):
    """Факториал (только для целых неотрицательных)."""
    if a < 0 or not float(a).is_integer():
        raise ValueError("Факториал определён только для целых неотрицательных чисел")
    return math.factorial(int(a))

def logarithm(a):
    """Натуральный логарифм."""
    if a <= 0:
        raise ValueError("Логарифм определён только для положительных чисел")
    return math.log(a)


OPERATIONS = {
    "1": ("Сложение",              add,          "+",  2),
    "2": ("Вычитание",             subtract,     "-",  2),
    "3": ("Умножение",             multiply,     "*",  2),
    "4": ("Деление",               divide,       "/",  2),
    "5": ("Возведение в степень",  power,        "**", 2),
    "6": ("Остаток от деления",    remainder,    "%",  2),
    "7": ("Целочисленное деление", floor_divide, "//", 2),
    "8": ("Квадратный корень",     sqrt,         "√",  1),
    "9": ("Модуль числа",          absolute,     "|x|", 1),
    "10": ("Факториал",            factorial,    "!",  1),
    "11": ("Натуральный логарифм", logarithm,    "ln", 1),
}
