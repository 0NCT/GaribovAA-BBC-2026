while True:
    expression = input("Введите пример (2 + 3) или exit: ").strip()

    if expression.lower() == "exit":
        break

    try:
        a, operator, b = expression.split()
        a, b = float(a), float(b)

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b
        elif operator == "**":
            result = a ** b
        elif operator == "%":
            result = a % b
        else:
            print("Неизвестная операция")
            continue

        print(result)
    except ValueError:
        print("Введите два числа и операцию через пробел")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except OverflowError:
        print("Слишком большое число")
