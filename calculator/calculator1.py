# Подход через функции

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def main():
    print("--- Калькулятор: Через функции ---")
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию (+, -, *, /): ")
        b = float(input("Введите второе число: "))

        if op == '+':
            print(f"Результат: {add(a, b)}")
        elif op == '-':
            print(f"Результат: {subtract(a, b)}")
        elif op == '*':
            print(f"Результат: {multiply(a, b)}")
        elif op == '/':
            print(f"Результат: {divide(a, b)}")
        else:
            print("Ошибка: неизвестная операция")
    except ValueError:
        print("Ошибка: нужно вводить числа")

if __name__ == "__main__":
    main()
