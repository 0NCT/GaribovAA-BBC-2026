from calculator import OPERATIONS
from validators import get_number, ask_continue
from ui import show_menu, show_result, show_error

def run():
    print("Добро пожаловать в калькулятор!")
    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            print("До свидания!")
            break

        if choice not in OPERATIONS:
            show_error("такой операции нет")
            continue

        name, func, symbol = OPERATIONS[choice]
        print(f"\nВыбрано: {name}")

        a = get_number("Введите первое число: ")
        b = get_number("Введите второе число: ")

        try:
            result = func(a, b)
            show_result(result)
        except ZeroDivisionError as e:
            show_error(str(e))

        if not ask_continue():
            print("До свидания!")
            break

if __name__ == "__main__":
    run()
