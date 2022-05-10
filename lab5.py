from random import randrange
import math
import time


class TemperingCodes:
    alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,.'

    def __init__(self, message: str):
        self.message = message
        self.encrypt = ''
        self.decrypt = ''
        self.decrypt_alphabet = {1028: "Є", 1030: "І", 1031: "Ї", 44: ",", 32: " ", "Ы": ",", "П": " ", "Ч": "І"}
        self.keys = ''
        self.gama = []

    def modulation_cypher(self):
        indexes = []
        for symbol in self.message:
            if symbol not in self.alphabet:
                print("Не допустимий символ!")
                return 0
            indexes.append(self.alphabet.find(symbol))
        count = 0
        while len(self.gama) != len(self.message):
            seed = time.time() + count
            numeric = lehmer_gen(seed, 1)
            if numeric > 0:
                self.gama.append(numeric)
            count += 1
        encrypted_indexes = list(map(lambda x, y: (x + y) % 37, indexes, self.gama))
        for index in encrypted_indexes:
            self.encrypt += self.alphabet[index]
        print("Зашифроване повдомлення: " + self.encrypt)
        for index in list(map(lambda x, y: ((x + len(self.alphabet)) - y) % 37, encrypted_indexes, self.gama)):
            self.decrypt += self.alphabet[index]
        print("Розшифроване повідомлення: " + self.decrypt)

    def binary_tempering(self):
        for symbol in self.message:
            blumBlumNumber = None
            while not blumBlumNumber:
                Blum = BlumBlumShub(6)
                randomNum = int(Blum.get_random_bits(), 2)
                if randomNum <= 33:
                    blumBlumNumber = randomNum
            key = blumBlumNumber
            self.keys += str(key) + " "
            if ord(symbol) in self.decrypt_alphabet:
                gg = ord(symbol) + key - 17
                self.encrypt += chr((gg % 33) + ord("А")).upper()
            elif ord(symbol) < 1040 or ord(symbol) > 1071:
                self.encrypt += " "
            else:
                gg = ord(symbol) + key - 17
                self.encrypt += chr((gg % 33) + ord("А")).upper()
        print("Зашифроване повідомлення: ", self.encrypt)
        key = ""
        for k in self.keys:
            if k != " ":
                key += k
            else:
                self.gama.append(key)
                key = ""
                continue
        half_res = ""
        res = ""
        for k, c in enumerate(self.encrypt):
            gg = ord(c) - int(self.gama[k]) - 17
            half_res += chr((gg % 33) + ord("А"))
        for symbol in half_res:
            if symbol in self.decrypt_alphabet:
                res += self.decrypt_alphabet[symbol]
            else:
                res += symbol
        count = 0
        for symbol in res:
            if symbol == self.message[count]:
                self.decrypt += symbol
                count += 1
            else:
                self.decrypt += self.message[count]
                count += 1
        print("Розшифроване повідомлення: ", self.decrypt)


def lehmer_gen(seed, size):
    m = 38
    a = 23
    b = 12345
    if size == 1:
        return math.ceil(math.fmod(a * math.ceil(seed) + b, m))
    r = [0 for _ in range(size)]
    r[0] = math.ceil(seed)
    for i in range(1, size):
        r[i] = math.ceil(math.fmod((a * r[i - 1] + b), m))
    return r[1:size]


def e(n):
    prime = [True for _ in range(n + 1)]
    primes = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes


class BlumBlumShub(object):
    def __init__(self, length):
        self.length = length
        self.primes = e(1000)

    def gen_primes(self):
        out_primes = []
        while len(out_primes) < 2:
            curr_prime = self.primes[randrange(len(self.primes))]
            if curr_prime % 4 == 3:
                out_primes.append(curr_prime)
        return out_primes

    def random_generator(self):
        x = randrange(1000000)
        while self.length:
            x += 1
            p, q = self.gen_primes()
            m = p * q
            z = (x**2) % m
            self.length -= 1
            yield str(bin(z).count('1') % 2)

    def get_random_bits(self):
        return ''.join(self.random_generator())


def main():
    message = input("Введіть повідомлення для шифрування: ").upper()
    choice = input(
        "Виберіть метод для шифрування:\n1-Гамування по модулю K\n\
2-Двійкове гамування\n\
Ваш вибір: ")
    instance = TemperingCodes(message)
    if choice == '1':
        instance.modulation_cypher()
    elif choice == '2':
        instance.binary_tempering()
    else:
        print("Невірний вибір!")


if __name__ == "__main__":
    main()
