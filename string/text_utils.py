def normalize_text(text):
    cleaned = ""

    for char in text:
        if char.isalnum() or char.isspace() or char in ".,!?:;-":
            cleaned += char
        else:
            cleaned += " "

    cleaned = " ".join(cleaned.split())

    for symbol in ".,!?:;":
        cleaned = cleaned.replace(" " + symbol, symbol)

    result = ""

    for char in cleaned:
        if char in ".,!?:;" and result.endswith(char):
            continue
        result += char

    return result.strip().capitalize()
