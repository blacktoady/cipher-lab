class SHA1:

    def __init__(self, message: str):
        self.message = message
        self.bytes = ''

    def hash_sha1(self):
        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        for n in range(len(self.message)):
            self.bytes += '{0:08b}'.format(ord(self.message[n]))
        bits = self.bytes + "1"
        pBits = bits
        while len(pBits) % 512 != 448:
            pBits += "0"
        pBits += '{0:064b}'.format(len(bits) - 1)

        def chunks(l, n):
            return [l[i:i + n] for i in range(0, len(l), n)]

        def rol(n, b):
            return ((n << b) | (n >> (32 - b))) & 0xffffffff

        for c in chunks(pBits, 512):
            words = chunks(c, 32)
            w = [0] * 80
            for n in range(0, 16):
                w[n] = int(words[n], 2)
            for i in range(16, 80):
                w[i] = rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

            a = h0
            b = h1
            c = h2
            d = h3
            e = h4

            for i in range(0, 80):
                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
                e = d
                d = c
                c = rol(b, 30)
                b = a
                a = temp

            h0 = h0 + a & 0xffffffff
            h1 = h1 + b & 0xffffffff
            h2 = h2 + c & 0xffffffff
            h3 = h3 + d & 0xffffffff
            h4 = h4 + e & 0xffffffff

        return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

    def check_hash(self, intact_hash, audit_hash):
        if intact_hash == audit_hash:
            return print("Цілісність підтверджена!")
        else:
            return print("Перевірка не пройдена. Дані були пошкоджені!")


def main():
    message = input("Введіть повідомлення для хешування: ")
    sha1 = SHA1(message)
    intact_hash = sha1.hash_sha1()
    print("Хеш-код повідомлення:", intact_hash)
    audit_hash = input("Введіть хеш-код: ")
    print(sha1.check_hash(intact_hash, audit_hash))


if __name__ == "__main__":
    main()
