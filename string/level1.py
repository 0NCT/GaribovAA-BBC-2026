def run():
    test = "пРиВет МИР"

    print("\nДобро пожаловать на первый уровень!")
    print("Данный уровень реализует три метода:")
    print("1) upper() — переводит строку в верхний регистр.")
    print("2) lower() — переводит строку в нижний регистр.")
    print("3) capitalize() — делает первую букву заглавной, остальные строчными.")

    print(
        "Тесты тут!"
        f"\nТестовая строка: {test}"
        f"\n1) {test.upper()}"
        f"\n2) {test.lower()}"
        f"\n3) {test.capitalize()}"
    )

    print("\nВведите строку и номер метода через ', '.")
    print("Например: Привет мир, 1")
    parts = input().rsplit(", ", 1)

    if len(parts) != 2:
        print("Ошибка: нужно ввести строку и номер метода через ', '.")
        return

    value, method = parts

    if method == "1":
        print(f"Вывод: {value.upper()}")
    elif method == "2":
        print(f"Вывод: {value.lower()}")
    elif method == "3":
        print(f"Вывод: {value.capitalize()}")
    else:
        print("Такого метода нет.")
