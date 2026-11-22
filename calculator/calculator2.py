def run_calculator():
    print("--- Калькулятор: 1 функция и while ---")
    print("Для выхода введите 'q' вместо числа.")
    
    while True:
        try:
            a_input = input("\nВведите первое число (или 'q'): ")
            if a_input.lower() == 'q':
                break
            a = float(a_input)
            
            op = input("Введите операцию (+, -, *, /): ")
            
            b_input = input("Введите второе число: ")
            b = float(b_input)
            
            if op == '+':
                print(f"Результат: {a + b}")
            elif op == '-':
                print(f"Результат: {a - b}")
            elif op == '*':
                print(f"Результат: {a * b}")
            elif op == '/':
                if b == 0:
                    print("Ошибка: деление на ноль")
                else:
                    print(f"Результат: {a / b}")
            else:
                print("Ошибка: неизвестная операция")
                
        except ValueError:
            print("Ошибка: нужно вводить числа")

run_calculator()
