def run():
    test = "Я изучаю Python"
    words = ["Я", "изучаю", "Python"]

    print("\nДобро пожаловать на третий уровень!")
    print("Данный уровень реализует два метода:")
    print("1) split() — разбивает строку на список частей.")
    print("2) join() — объединяет строки из списка через заданный разделитель.")

    print(
        "Тесты тут!"
        f"\nТестовая строка: {test}"
        f"\n1) split(): {test.split()}"
        f"\nТестовый список: {words}"
        f"\n2) join() с разделителем '-': {'-'.join(words)}"
    )

    method = input("\nВведите номер метода (1–2): ").strip()

    if method == "1":
        text = input("Введите строку: ")
        separator = input(
            "Введите разделитель "
            "(Enter — разделение по пробельным символам): "
        )
        result = text.split() if separator == "" else text.split(separator)
        print(f"Вывод: {result}")

    elif method == "2":
        print("Введите элементы списка через '; '.")
        print("Например: Я; изучаю; Python")
        items = input().split("; ")
        separator = input(
            "Введите разделитель для объединения "
            "(Enter — без разделителя): "
        )
        print(f"Вывод: {separator.join(items)}")

    else:
        print("Такого метода нет.")
