class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        return a / b

    def run(self):
        print("--- Калькулятор: Через класс ---")
        try:
            a = float(input("Введите первое число: "))
            op = input("Введите операцию (+, -, *, /): ")
            b = float(input("Введите второе число: "))

            if op == '+':
                print(f"Результат: {self.add(a, b)}")
            elif op == '-':
                print(f"Результат: {self.subtract(a, b)}")
            elif op == '*':
                print(f"Результат: {self.multiply(a, b)}")
            elif op == '/':
                print(f"Результат: {self.divide(a, b)}")
            else:
                print("Ошибка: неизвестная операция")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
        except ValueError:
            print("Ошибка: нужно вводить числа")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
