
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

def power(a, b):
    return a ** b

OPERATIONS = {
    "1": ("Сложение", add, "+"),
    "2": ("Вычитание", subtract, "-"),
    "3": ("Умножение", multiply, "*"),
    "4": ("Деление", divide, "/"),
    "5": ("Возведение в степень", power, "**"),
}
