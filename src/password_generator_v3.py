import string, random, re
from typing import Tuple

LETTERS_STRING = string.ascii_lowercase + string.ascii_uppercase
DIGITS_STRING = string.digits
SYMBOLS_STRING = "!#$%&.*@?"
PASSWORD_LENGTH_DISPLAY = "\nLongitud de contrasena (min. y defecto {}): "
NUMBERS_LENGTH_DISPLAY = "Cuantos numeros (max. {max}, defecto {default})? "
SYMBOLS_LENGTH_DSIPLAY = "Cuantos simbolos (max. {max}, defecto {default})? "
DEFAULT_PASSWORD_LENGTH = 6
DEFAULT_NUMBERS_QUANTITY = 2
DEFAULT_SYMBOLS_QUANTITY = 1


def main():
    print("Password Generator 3.0.0\n---")
    password_length, how_many_numbers, how_many_symbols = \
        DEFAULT_PASSWORD_LENGTH, 0, 0
    options_menu = "\n[Regenerar (g) | Reiniciar (s) | Salir (x)]: "
    option = "S"
    while True:
        if option == 'S':
            password_length, how_many_numbers, how_many_symbols = \
                get_parameters()
            option = "G"
        elif option == "G":
            password = generate_password(password_length, how_many_numbers,
                how_many_symbols)
            print(f"\n-->  {password}  <--")
            option = ""
        elif option == "X":
            break
        else:
            option = input(options_menu).upper()

    print("\nAdios!")


def get_parameters() -> Tuple[int, int, int]:
    input_display = PASSWORD_LENGTH_DISPLAY.format(DEFAULT_PASSWORD_LENGTH)
    password_length = get_input_value(input_display, DEFAULT_PASSWORD_LENGTH)
    if password_length < DEFAULT_PASSWORD_LENGTH:
        password_length = DEFAULT_PASSWORD_LENGTH
    print(f"> Longitud: {password_length}")

    input_display = NUMBERS_LENGTH_DISPLAY.format(max=password_length,
        default=DEFAULT_NUMBERS_QUANTITY)
    how_many_numbers = get_input_value(input_display, DEFAULT_NUMBERS_QUANTITY)
    if how_many_numbers > password_length:
        how_many_numbers = password_length
    print(f"> Numeros: {how_many_numbers}")
    
    max_symbols = password_length - how_many_numbers
    if max_symbols == 0:
        how_many_symbols = 0
    else:
        input_message = SYMBOLS_LENGTH_DSIPLAY.format(max=max_symbols,
            default=DEFAULT_SYMBOLS_QUANTITY)
        how_many_symbols = get_input_value(input_message,
            DEFAULT_SYMBOLS_QUANTITY)
        if how_many_symbols > max_symbols:
            how_many_symbols = max_symbols
        print(f"> Simbolos: {how_many_symbols}")

    return password_length, how_many_numbers, how_many_symbols


def get_input_value(input_message: str, default_value: int) -> int:
    input_value = input(input_message)
    try:
        input_value = int(input_value)
    except:
        input_value = default_value
    return input_value


def generate_password(password_length: int, how_many_numbers: int,
        how_many_symbols: int) -> str:    
    how_many_letters = password_length - (how_many_numbers + how_many_symbols)
    if (how_many_letters >= 2):
        random_letters = get_random_letters(how_many_letters)
    else:
        random_letters = ""
    random_numbers = generate_sample(DIGITS_STRING, how_many_numbers)
    random_symbols = generate_sample(SYMBOLS_STRING, how_many_symbols)
    password = random_letters + random_numbers + random_symbols
    password = generate_sample(password, password_length)
    return password


def get_random_letters(how_many_letters: int) -> str:
    is_valid_string = False
    while not is_valid_string:
        random_letters = generate_sample(LETTERS_STRING, how_many_letters)
        regex_pattern = r'[A-Z].+[a-z]|[a-z].+[A-Z]'
        # La cadena contiene mayusculas y nimusculas.
        is_valid_string = re.search(regex_pattern, random_letters)
    return random_letters


def generate_sample(char_string: str, sample_length: int) -> str:
    sample = random.sample(char_string, k=sample_length)
    sample = "".join(sample)
    return sample


if __name__ == "__main__":
    main()