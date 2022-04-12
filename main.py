from colors import bcolors
from sympy import isprime


DEBUG = False

# alphavite_num = {
#     0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p',
#     16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z',
# }
alphavite_num = {
    0: 'а',
    1: 'б',
    2: 'в',
    3: 'г',
    4: 'ґ',
    5: 'д',
    6: 'е',
    7: 'є',
    8: 'ж',
    9: 'з',
    10: 'и',
    11: 'і',
    12: 'ї',
    13: 'й',
    14: 'к',
    15: 'л',
    16: 'м',
    17: 'н',
    18: 'о',
    19: 'п',
    20: 'р',
    21: 'с',
    22: 'т',
    23: 'у',
    24: 'ф',
    25: 'х',
    26: 'ц',
    27: 'ч',
    28: 'ш',
    29: 'щ',
    30: 'ь',
    31: 'ю',
    32: 'я',

}

# alphavite_letter = {
#     'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
#     'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
# }
alphavite_letter = {
    'а': 0,
    'б': 1,
    'в': 2,
    'г': 3,
    'ґ': 4,
    'д': 5,
    'е': 6,
    'є': 7,
    'ж': 8,
    'з': 9,
    'и': 10,
    'і': 11,
    'ї': 12,
    'й': 13,
    'к': 14,
    'л': 15,
    'м': 16,
    'н': 17,
    'о': 18,
    'п': 19,
    'р': 20,
    'с': 21,
    'т': 22,
    'у': 23,
    'ф': 24,
    'х': 25,
    'ц': 26,
    'ч': 27,
    'ш': 28,
    'щ': 29,
    'ь': 30,
    'ю': 31,
    'я': 32,
}

polygramm_letter = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я", ".", ",", " "]

# print(len(polygramm_letter))

class Caesar:
    def __init__(self, phrase, key):
        self.phrase = tuple(phrase.lower())
        self.key = int(key)
    def encrypt(self):
        encr_list = list()

        for i in self.phrase:
            if alphavite_letter.get(i) >= 0:
                letter_num = int(alphavite_letter.get(i))
                encr_num = letter_num + self.key

                if encr_num >= len(alphavite_num):
                    encr_list.append(alphavite_num.get(encr_num - len(alphavite_num)))
                else:
                    encr_list.append(alphavite_num.get(encr_num))

        print(bcolors.UNDERLINE + 'your plain text:\n' + bcolors.ENDC + bcolors.HEADER + ''.join(self.phrase).upper() + bcolors.ENDC)
        print(bcolors.UNDERLINE + '\nyour encrypted cipher:\n' + bcolors.ENDC + bcolors.OKGREEN + ''.join(encr_list).upper() + bcolors.ENDC)
    def decode(self):
        dec_list = list()
        for i in self.phrase:
            if alphavite_letter.get(i) >= 0:
                letter_num = int(alphavite_letter.get(i))
                dec_num = letter_num - self.key
                if dec_num < 0:
                    dec_list.append(alphavite_num.get(dec_num + len(alphavite_num)))
                else:
                    dec_list.append(alphavite_num.get(dec_num))

        print(bcolors.UNDERLINE + 'your cipher text:\n' + bcolors.ENDC + bcolors.HEADER + ''.join(self.phrase).upper() + bcolors.ENDC)
        print(bcolors.UNDERLINE + '\nyour decoded text:\n' + bcolors.ENDC + bcolors.OKGREEN + ''.join(dec_list).upper() + bcolors.ENDC)

class Linear:
    def __init__(self, phrase, key):
        self.phrase = tuple(phrase.lower())
        self.key = int(key)

    def encrypt(self):
        encr_list = list()

        if isprime(len(self.phrase)) and self.key < len(alphavite_num) and self.key >= 0:
            for i in self.phrase:
                if alphavite_letter.get(i) >= 0:
                    letter_num = int(alphavite_letter.get(i))
                    letter_num = (letter_num * self.key) % len(alphavite_num)
                    encr_list.append(alphavite_num.get(letter_num))
            print(bcolors.UNDERLINE + 'your plain text:\n' + bcolors.ENDC + bcolors.HEADER + ''.join(
                self.phrase).upper() + bcolors.ENDC)
            print(bcolors.UNDERLINE + '\nyour encrypted cipher:\n' + bcolors.ENDC + bcolors.OKGREEN + ''.join(
                encr_list).upper() + bcolors.ENDC)

        else:
            print(bcolors.WARNING + "key isn't correct!" + bcolors.ENDC)
    def decode(self):
        decr_list = list()

        if isprime(len(self.phrase)) and self.key < len(alphavite_num) and self.key >= 0:
            for i in self.phrase:
                if alphavite_letter.get(i) >= 0:
                    letter_num = int(alphavite_letter.get(i))
                    letter_num = (letter_num * pow(self.key, -1, len(alphavite_num))) % len(alphavite_num)
                    decr_list.append(alphavite_num.get(letter_num))
            print(bcolors.UNDERLINE + 'your cipher text:\n' + bcolors.ENDC + bcolors.HEADER + ''.join(
                self.phrase).upper() + bcolors.ENDC)
            print(bcolors.UNDERLINE + '\nyour decoded text:\n' + bcolors.ENDC + bcolors.OKGREEN + ''.join(
                decr_list).upper() + bcolors.ENDC)

        else:
            print(bcolors.WARNING + "key isn't correct!" + bcolors.ENDC)

class Affine:
    def __init__(self, phrase, key1, key2):
        self.phrase = tuple(phrase.lower())
        self.key1 = int(key1)
        self.key2 = int(key2)

    def encrypt(self):
        encr_list = list()

        if isprime(len(self.phrase)) and self.key1 < len(alphavite_num) and self.key1 >= 0 and self.key2 < len(alphavite_num) and self.key2 >= 0:
            for i in self.phrase:
                if alphavite_letter.get(i) >= 0:
                    letter_num = int(alphavite_letter.get(i))
                    letter_num = (letter_num * self.key1 + self.key2) % len(alphavite_num)
                    encr_list.append(alphavite_num.get(letter_num))
            print(bcolors.UNDERLINE + 'your plain text:\n' + bcolors.ENDC + bcolors.HEADER + ''.join(
                self.phrase).upper() + bcolors.ENDC)
            print(bcolors.UNDERLINE + '\nyour encrypted cipher:\n' + bcolors.ENDC + bcolors.OKGREEN + ''.join(
                encr_list).upper() + bcolors.ENDC)

        else:
            print(bcolors.WARNING + "key isn't correct!" + bcolors.ENDC)

    def decode(self):
        decr_list = list()

        k_inv = pow(self.key1, -1, len(alphavite_num))
        t_inv = pow((-k_inv * self.key2), 1, len(alphavite_num))
        if isprime(len(self.phrase)) and self.key1 < len(alphavite_num) and self.key1 >= 0 and self.key2 < len(alphavite_num) and self.key2 >= 0:
            for i in self.phrase:
                if alphavite_letter.get(i) >= 0:
                    letter_num = int(alphavite_letter.get(i))
                    letter_num = (letter_num * k_inv + t_inv) % len(alphavite_num)
                    decr_list.append(alphavite_num.get(letter_num))
            print(bcolors.UNDERLINE + 'your cipher text:\n' + bcolors.ENDC + bcolors.HEADER + ''.join(
                self.phrase).upper() + bcolors.ENDC)
            print(bcolors.UNDERLINE + '\nyour decoded text:\n' + bcolors.ENDC + bcolors.OKGREEN + ''.join(
                decr_list).upper() + bcolors.ENDC)

        else:
            print(bcolors.WARNING + "key isn't correct!" + bcolors.ENDC)

# class Playfair:
#     def __init__

if __name__ == '__main__':

    if DEBUG :
        print(bcolors.WARNING + 'DEBUG MODE' + bcolors.ENDC)
        Affine('qwertyu', 3, 2).encrypt()
        Affine('YQOBHWK', 3, 2).decode()

        Linear('qwertyu', 3).encrypt()
        Linear('WOMZFUI', 3).decode()

        Caesar('alpha', 3).encrypt()
        Caesar('doskd', 3).decode()

    else:
        print(bcolors.HEADER +
                '      :::     :::   :::       ::::::::           :::        ::::    :::\n',
                '     :+:     :+:   :+:      :+:    :+:        :+: :+:      :+:+:   :+:\n',
                '    +:+      +:+ +:+       +:+              +:+   +:+     :+:+:+  +:+\n',
                '   +#+       +#++:        +#+             +#++:++#++:    +#+ +:+ +#+\n',
                '  +#+        +#+         +#+             +#+     +#+    +#+  +#+#+#\n',
                ' #+#        #+#         #+#    #+#      #+#     #+#    #+#   #+#+#\n',
                '########## ###          ########       ###     ###    ###    ####\n' + bcolors.ENDC)

        type_cipher = int(input('select cipher and press ENTER:\n1. Caesar\n2. Linear\n3. Affine\n'))
        operation_cypher = int(input('select cipher operation and press ENTER:\n1. Encrypt\n2. Decrypt\n'))
        phrase = input('enter your phrase:\n')
        phrase = phrase.replace(',', '').replace(' ', '')
        key1 = input('key:\n')
        key2 = input('key 2(if exist, else leave blank and press ENTER):\n')
        if type_cipher == 1 and operation_cypher == 1:
            Caesar(phrase, key1).encrypt()
        elif type_cipher == 1 and operation_cypher == 2:
            Caesar(phrase, key1).decode()
        elif type_cipher == 2 and operation_cypher == 1:
            Linear(phrase, key1).encrypt()
        elif type_cipher == 2 and operation_cypher == 2:
            Linear(phrase, key1).decode()
        elif type_cipher == 3 and operation_cypher == 1:
            Affine(phrase, key1, key2).encrypt()
        elif type_cipher == 3 and operation_cypher == 2:
            Affine(phrase, key1, key2).decode()
        else:
            print(bcolors.WARNING + "something wen't wrong.." + bcolors.ENDC)



