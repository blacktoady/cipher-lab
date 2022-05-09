import numpy as np
from numpy import linalg as LA


class Poligram_cipher:
    """Клас для полігамного шифрування, що містить шифр Playfair і шифр Хілла."""

    def __init__(self, message: str) -> None:
        self.message = message
        self.alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ _,.'
        # Матриця з ключем "АГРЕГАЦІЯ"
        self.matrix = [
            ["А", "Г", "Р", "Е", "Ц", "І"],
            ["Я", "Б", "В", "Ґ", "Д", "Є"],
            ["Ж", "З", "И", "Й", "Ї", "К"],
            ["Л", "М", "Н", "О", "П", "С"],
            ["Т", "У", "Ф", "Х", "Ч", "Ш"],
            ["Щ", "Ь", "Ю", " ", ",", "."]
        ]

    def Playfair_Cipher(self):
        # Створення списку та перевірка на дозволенні символи
        message = []
        for symbol in self.message:
            if symbol in self.alphabet:
                message.append(symbol)
            else:
                print(f'Не допустимий символ для шифрування - {symbol}')
                return 0
        # Пошук однакових символів
        for i in range(1, len(message)):
            if message[i] == message[i - 1]:
                message.insert(i, 'X')
        # Якщо кількість символів не парна - добовляємо "Х"
        if len(message) % 2 != 0:
            message.append('X')
        # Розділення тексту по два символи
        binary_message = []
        count = ''
        for i in message:
            count += i
            if len(count) == 2:
                binary_message.append(count)
                count = ''
        # Шифрування
        encrypt = ''
        switch = 0
        # Перебір подвійних символів
        for i in range(len(binary_message)):
            # k = 0 або k = 1 (Для розділення подвійних символів)
            for k in range(2):
                # Перебір рядків матриці
                for x in range(len(self.matrix)):
                    # Перебір символів в рядку
                    for y in range(len(self.matrix[x])):
                        # Якщо символ з матриці рівний символу з відкритого повідомлення
                        if self.matrix[x][y] == binary_message[i][k]:
                            # Якщо 0 і 1 символи відкритого повідомлення знаходяться на одному рядку в матриці
                            if binary_message[i][0] in self.matrix[x] and binary_message[i][1] in self.matrix[x]:
                                # Якщо символ в матриці не рівний початку матричного рядка
                                if self.matrix[x][y] != self.matrix[x][-1]:
                                    # Добавляємо до encrypt значення символа матриці з відступом +1
                                    encrypt += self.matrix[x][y + 1]
                                # Інакше символи 0 і 1 знаходяться на різних рядках матриці
                                else:
                                    # Добавляємо до encrypt значення символа матриці з відступом -5
                                    encrypt += self.matrix[x][y - 5]
                            # Інакше якщо символи 0 і 1 знаходяться на різних рядках матриці
                            else:
                                # Перебір рядків матриці
                                for a in range(len(self.matrix)):
                                    # Перебір символів в рядку
                                    for b in range(len(self.matrix[a])):
                                        # Якщо символ з матриці рівний символу 0 з зашифрованого повідомлення
                                        if self.matrix[a][b] == binary_message[i][0]:
                                            # Створюємо змінну х0, в якій міститься координата 0 символу
                                            x0 = a
                                        # Якщо символ з матриці рівний символу 1 з зашифрованого повідомлення
                                        if self.matrix[a][b] == binary_message[i][1]:
                                            # Створюємо змінну х1, в якій міститься координата 1 символу
                                            x1 = a
                                # Якщо змінна switch дорівнює 0
                                if switch == 0:
                                    # Добавляємо до змінної encrypt координати значення матриці х1,у1
                                    encrypt += self.matrix[x1][y]
                                    switch = 1
                                else:
                                    # Добавляємо до змінної encrypt координати значення матриці х0,у
                                    encrypt += self.matrix[x0][y]
                                    switch = 0
        # Виведення зашифрованого повідомлення
        print('Зашифроване повідомлення:', encrypt)
        # Ділення зашифрованого тексту по 2 символи
        binary_message = []
        count = ''
        for i in encrypt:
            count += i
            if len(count) == 2:
                binary_message.append(count)
                count = ''
        # Розшифровка
        decrypt = []
        switch = 0
        # Далі виконубться дії, дзеркальні шифруванню повідомлення
        for i in range(len(binary_message)):
            for k in range(2):
                for x in range(len(self.matrix)):
                    for y in range(len(self.matrix[x])):
                        if self.matrix[x][y] == binary_message[i][k]:
                            if binary_message[i][0] in self.matrix[x] and binary_message[i][1] in self.matrix[x]:
                                if self.matrix[x][y] != self.matrix[x][0]:
                                    decrypt.append(self.matrix[x][y - 1])
                                else:
                                    decrypt.append(self.matrix[x][y + 5])
                            else:
                                for a in range(len(self.matrix)):
                                    for b in range(len(self.matrix[a])):
                                        if self.matrix[a][b] == binary_message[i][0]:
                                            x0 = a
                                        if self.matrix[a][b] == binary_message[i][1]:
                                            x1 = a
                                if switch == 0:
                                    decrypt += self.matrix[x1][y]
                                    switch = 1
                                else:
                                    decrypt += self.matrix[x0][y]
                                    switch = 0
        # Видалення символів "Х"
        for i in range(len(decrypt) - 1):
            if decrypt[i] == 'X':
                if decrypt[i] != decrypt[-1]:
                    if decrypt[i - 1] == decrypt[i + 1]:
                        decrypt.remove(decrypt[i])
                else:
                    decrypt.remove(decrypt[i])
        # Виведення розшифрованого повідомлення
        print('Розшифроване повідомлення:', ''.join(decrypt))

    def Hyla_Cipher(self, key):
        # Створення необхідних змінних
        text_numbers = []
        key_code = []
        res = []
        encrypted_message = ''
        # Заповнення списку відповідними індексами повідомлення
        for symbol in self.message:
            if symbol in self.alphabet:
                text_numbers.append(self.alphabet.find(symbol))
            else:
                print(f'Не допустимий символ для шифрування - {symbol}')
                return 0
        for symbol in key:
            if symbol in self.alphabet:
                key_code.append(self.alphabet.find(symbol))
        # Створення ключової матриці
        key_matrix = np.array(self.chunkify(key_code, 4))
        text_matrix = self.chunkify(text_numbers, 4)
        for text_block in text_matrix:
            res.append((np.array(text_block).dot(key_matrix)) % 37)
        for block in res:
            for number in block:
                encrypted_message += self.alphabet[number]
        print('Зашифроване повідомлення:', encrypted_message)
        # decryption()
        text_numbers.clear()
        for symbol in encrypted_message:
            if symbol in self.alphabet:
                text_numbers.append(self.alphabet.find(symbol))
        text_matrix = self.chunkify(text_numbers, 4)
        # Знаходимо детермінант матриці ключа
        det_matrix_key = int(LA.det(key_matrix))
        # Розширений алгоритм Евкліда
        determinant = self.gcdex(det_matrix_key, len(self.alphabet))
        # Обрахунок оберненого детермінанту елементу
        key_matrix_inverse_determinant = self.inverse_determinant_element(det_matrix_key, determinant[1])
        result_0 = []
        alliance_matrix = np.array(self.chunkify(self.algebraic_additions(key_matrix), 4))
        for i in alliance_matrix:
            for j in i:
                if j < 0:
                    j = abs(j) % 37
                    result_0.append(-j)
                else:
                    j = j % 37
                    result_0.append(j)
        result_0 = np.array(self.chunkify(result_0, 4))
        result = []
        for i in result_0:
            for j in i:
                if j < 0:
                    j = (abs(j) * key_matrix_inverse_determinant) % 37
                    result.append(-j)
                else:
                    j = (j * key_matrix_inverse_determinant) % 37
                    result.append(j)
        result = np.array(self.chunkify(result, 4))
        result_transpose = result.transpose()
        inverse_modulo_to_the_key_matrix = []
        for i in result_transpose:
            for j in i:
                if j < 0:
                    j = 37 + j
                    inverse_modulo_to_the_key_matrix.append(j)
                else:
                    inverse_modulo_to_the_key_matrix.append(j)
        inverse_modulo_to_the_key_matrix = np.array(self.chunkify(inverse_modulo_to_the_key_matrix, 4))
        message_decryption = []
        for i in text_matrix:
            message_decryption.append((np.array(i).dot(inverse_modulo_to_the_key_matrix)) % 37)
        message_decryption = [x for l in message_decryption for x in l]
        decrypted_message = ''
        for number in message_decryption:
            decrypted_message += self.alphabet[number]
        print('Дешифроване повідомлення:', decrypted_message)

    # Функція для розбиття списку на блоки
    def chunkify(self, items, chunk_size):
        matrix = []
        for i in range(0, len(items), chunk_size):
            matrix.append(items[i:i + chunk_size])
        while len(matrix[-1]) != 4:
            matrix[-1].append(33)
        return matrix

    # Розширений алгоритм Евкліда
    def gcdex(self, a, b):
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = self.gcdex(b, a % b)
            return d, y, x - y * (a // b)

    # Обернений детермінанту елемент
    def inverse_determinant_element(self, det, x):
        if det < 0 and x > 0:
            return x
        elif det > 0 and x < 0:
            return 37 + x
        elif det > 0 and x > 0:
            return x
        elif det < 0 and x < 0:
            return -x

    # Алгебраїчні доповнення
    def algebraic_additions(self, key_matrix):
        result = []
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                Mi = np.delete(key_matrix, [i], axis=0)
                Mij = np.delete(Mi, [j], 1)
                if (i + j) % 2 == 0:
                    result.append((self.int_r(LA.det(Mij))))
                else:
                    result.append(-(self.int_r(LA.det(Mij))))
        return result

    # Округлення числа
    def int_r(self, num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num


def main() -> None:
    message = input("Введіть повідомлення для шифрування: ").upper()
    if not message:
        message = "Я, ПОНОМАРЬОВ АНАТОЛІЙ ВЛАДИСЛАВОВИЧ, СТУДЕНТ УНІВЕРСИТЕТУ"
    cipher = Poligram_cipher(message)
    choice = input('Виберіть яким методом буде відбуватись шифрування\n1-Шифр Playfair\n2-Шифр Хілла\nВаш вибір: ')
    if choice == '1':
        cipher.Playfair_Cipher()
    elif choice == '2':
        key = input("Введіть ключ для шифрування: ").upper()
        if not key:
            key = 'АКЛІМАТИЗУВАТИСЯ'
        cipher.Hyla_Cipher(key)
    else:
        print('Не вірний вибір!')


if __name__ == '__main__':
    main()
