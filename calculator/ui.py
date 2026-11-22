from calculator import OPERATIONS

def show_menu():
    print("\n--- КАЛЬКУЛЯТОР ---")
    for key, (name, _, symbol, arity) in OPERATIONS.items():
        formula = f"{symbol}(x)" if arity == 1 else f"x {symbol} y"
        print(f"{key:>2}. {name:<24} {formula}")
    print(" 0. Выход")

def show_result(result):
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print(f"Результат: {result}")

def show_error(message):
    print(f"Ошибка: {message}")
