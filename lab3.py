from itertools import cycle


class Cipher:
    """Клас для полігамного шифрування, що містить шифр Playfair і шифр Хілла."""

    def __init__(self, message: str) -> None:
        self.message = message
        self.alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,."

    def encode(self, text, key):
        try:
            encode_message = lambda a: self.alphabet[(self.alphabet.index(a[0]) + self.alphabet.index(a[1]) % 37) % 37]
            return ''.join(map(encode_message, zip(text, cycle(key))))
        except ValueError:
            pass

    def decode(self, coded_text, key):
        try:
            decode_message = lambda a: self.alphabet[self.alphabet.index(a[0]) - self.alphabet.index(a[1]) % 37]
            return ''.join(map(decode_message, zip(coded_text, cycle(key))))
        except TypeError:
            pass

def main():
    message = input("Введіть повідомлення для шифрування: ").upper()
    if not message:
        message = "Я, ПОНОМАРЬОВ АНАТОЛІЙ ВЛАДИСЛАВОВИЧ, СТУДЕНТ УНІВЕРСИТЕТУ"
    key = input("Введіть ключ для шифрування: ").upper()
    if not key:
        key = "ПОНОМАРЬОВ"
    cipher = Cipher(message)
    print("Зашифроване повідомлення:", cipher.encode(message, key))
    print("Розшифроване повідомлення:", cipher.decode(cipher.encode(message, key), key))


if __name__ == '__main__':
    main()
