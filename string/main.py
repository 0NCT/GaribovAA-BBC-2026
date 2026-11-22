import level1
import level2
import level3
import level4
import level5


LEVELS = {
    1: level1.run,
    2: level2.run,
    3: level3.run,
    4: level4.run,
    5: level5.run,
}


def main():
    print("Здравствуйте! Добро пожаловать в программу работы со строками!")

    try:
        choice = int(input("Выберите уровень (1–5): "))
    except ValueError:
        print("Ошибка: номер уровня должен быть целым числом.")
        return

    handler = LEVELS.get(choice)
    if handler is None:
        print("Такого уровня нет. Выберите число от 1 до 5.")
        return

    handler()


if __name__ == "__main__":
    main()
