from calculator import OPERATIONS

def show_menu():
    print("\n--- КАЛЬКУЛЯТОР ---")
    for key, (name, _, symbol) in OPERATIONS.items():
        print(f"{key}. {name} ({symbol})")
    print("0. Выход")

def show_result(result):
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print(f"Результат: {result}")

def show_error(message):
    print(f"Ошибка: {message}")
