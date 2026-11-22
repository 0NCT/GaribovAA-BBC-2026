def run():
    digit_test = "12345"
    alpha_test = "Привет"
    strip_test = "   Привет мир   "
    format_test = "Привет, {}! Тебе {} лет."

    print("\nДобро пожаловать на четвёртый уровень!")
    print("Данный уровень реализует четыре метода:")
    print("1) isdigit() — проверяет, состоит ли непустая строка из цифр.")
    print("2) isalpha() — проверяет, состоит ли непустая строка из букв.")
    print("3) strip() — удаляет символы с начала и конца строки.")
    print("   Без аргумента удаляет пробельные символы.")
    print("4) format() — подставляет значения в шаблон строки.")

    print(
        "Тесты тут!"
        f"\n1) {digit_test!r}.isdigit(): {digit_test.isdigit()}"
        f"\n2) {alpha_test!r}.isalpha(): {alpha_test.isalpha()}"
        f"\n3) {strip_test!r}.strip(): {strip_test.strip()!r}"
        f"\n4) format(): {format_test.format('Анна', 20)}"
    )

    method = input("\nВведите номер метода (1–4): ").strip()

    if method == "1":
        text = input("Введите строку: ")
        print(f"Вывод: {text.isdigit()}")

    elif method == "2":
        text = input("Введите строку: ")
        print(f"Вывод: {text.isalpha()}")

    elif method == "3":
        text = input("Введите строку: ")
        chars = input(
            "Введите символы для удаления с краёв "
            "(Enter — пробельные символы): "
        )
        result = text.strip() if chars == "" else text.strip(chars)
        print(f"Вывод: {result!r}")

    elif method == "4":
        print("Введите шаблон с {} или числовыми полями {0}, {1} и т. д.")
        print("Например: Привет, {}! Тебе {} лет.")
        template = input("Шаблон: ")

        print("Введите значения через '; '.")
        print("Например: Анна; 20")
        values = input().split("; ")

        try:
            print(f"Вывод: {template.format(*values)}")
        except (IndexError, KeyError, ValueError) as error:
            print(f"Ошибка форматирования: {error}")
            print("Проверьте шаблон и количество введённых значений.")

    else:
        print("Такого метода нет.")
