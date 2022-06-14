import string, random

SYMBOLS_STRING = "!#$%&.*@?"
BASE_STRING = string.ascii_uppercase + string.ascii_lowercase + string.digits + SYMBOLS_STRING
PASSWORD_LENGTH_DISPLAY = "\nLongitud de contrasena (min. y default {}): "
DEFAULT_PASSWORD_LENGTH = 6

def main():
    print("Simple Password Generator 1.0.0\n---")
    input_display = PASSWORD_LENGTH_DISPLAY.format(DEFAULT_PASSWORD_LENGTH)
    password_length = get_input_value(input_display, DEFAULT_PASSWORD_LENGTH)
    if password_length < DEFAULT_PASSWORD_LENGTH:
        password_length = DEFAULT_PASSWORD_LENGTH
    print(f"> Longitud: {password_length}")
    password = generate_password(password_length)
    print(f"\n-->  {password}  <--")
    print("\nAdios!")


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


if __name__ == '__main__':
    main()