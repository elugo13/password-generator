import string, random, re
from typing import Tuple

SYMBOLS_STRING = "!#$%&.*@?"
BASE_STRING = string.ascii_uppercase + string.ascii_lowercase + string.digits + SYMBOLS_STRING
PASSWORD_LENGTH_DISPLAY = "\nLongitud de contrasena (min. y defecto {}): "
NUMBERS_LENGTH_DISPLAY = "Cuantos numeros (defecto {default})? "
SYMBOLS_LENGTH_DSIPLAY = "Cuantos simbolos (defecto {default})? "
DEFAULT_PASSWORD_LENGTH = 6
DEFAULT_NUMBERS_QUANTITY = 2
DEFAULT_SYMBOLS_QUANTITY = 1


def main():
    print("Password Generator 1.0.0\n---")
    password_length, how_many_numbers, how_many_symbols = \
                get_parameters()
    while True:
        password = generate_password(password_length)
        is_password_valid = validate_password(password, how_many_numbers,
                how_many_symbols)
        if is_password_valid:
            break
    print(f"\n-->  {password}  <--")
    print("\nAdios!")


def get_parameters() -> Tuple[int, int, int]:
    input_display = PASSWORD_LENGTH_DISPLAY.format(DEFAULT_PASSWORD_LENGTH)
    password_length = get_input_value(input_display, DEFAULT_PASSWORD_LENGTH)
    if password_length < DEFAULT_PASSWORD_LENGTH:
        password_length = DEFAULT_PASSWORD_LENGTH
    print(f"> Longitud: {password_length}")

    input_display = NUMBERS_LENGTH_DISPLAY.format(
        default=DEFAULT_NUMBERS_QUANTITY)
    how_many_numbers = get_input_value(input_display, DEFAULT_NUMBERS_QUANTITY)
    print(f"> Numeros: {how_many_numbers}")

    input_message = SYMBOLS_LENGTH_DSIPLAY.format(
        default=DEFAULT_SYMBOLS_QUANTITY)
    how_many_symbols = get_input_value(input_message,
        DEFAULT_SYMBOLS_QUANTITY)
    print(f"> Simbolos: {how_many_symbols}")

    return password_length, how_many_numbers, how_many_symbols


def get_input_value(input_message: str, default_value: int) -> int:
    input_value = input(input_message)
    try:
        input_value = int(input_value)
    except:
        input_value = default_value
    return input_value


def generate_password(password_length: int) -> str:
    password = random.sample(BASE_STRING, k=password_length)
    password = "".join(password)
    return password


def validate_password(password: str, how_many_numbers: int,
                how_many_symbols: int) -> bool:
    has_upper_case = re.search(r'[A-Z]', password)
    has_lower_case = re.search(r'[a-z]', password)
    has_digits = len(re.findall(r'\d', password)) == how_many_numbers
    has_symbols = len(re.findall(r'\W', password)) == how_many_symbols
    return has_upper_case and has_lower_case and has_digits and has_symbols


def generate_sample(char_string: str, sample_length: int) -> str:
    sample = random.sample(char_string, k=sample_length)
    sample = "".join(sample)
    return sample


if __name__ == "__main__":
    main()