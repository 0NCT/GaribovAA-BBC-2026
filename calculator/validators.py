
def get_number(prompt="Введите число: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: нужно ввести число. Попробуйте снова.")

def ask_continue():
    while True:
        answer = input("Продолжить? (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Пожалуйста, ответьте 'да' или 'нет'.")
