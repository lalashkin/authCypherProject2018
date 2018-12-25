import random


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def xgcd(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0

    while b != 0:
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y


def get_primes(start, stop):
    s = [0]
    primes = list()
    for k in range(start, stop):
        s.append(1)

    for k in range(start, stop):
        if s[k - 1] == 1:
            for l in range(k*k, stop, k):
                s[l - 1] = 0

    for i in range(start, stop):
        if s[i - 1] == 1:
            primes.append(i)

    return primes


def chooseE(totient):
    while True:
        e = random.randrange(2, totient)

        if gcd(e, totient) == 1:
            return e


class RSA:

    def __init__(self):
        self.e = None
        self.d = None
        self.n = None
        self.get_keys()

    def get_keys(self):
        primes = get_primes(2, 1000)

        p = primes[random.randint(100, len(primes))]
        q = primes[random.randint(100, len(primes))]

        self.n = p * q
        euler = (p - 1) * (q - 1)
        self.e = chooseE(euler)
        divisor, x, y = xgcd(self.e, euler)

        if x < 0:
            self.d = x + euler
        else:
            self.d = x

    def encrypt(self, message):
        char_list = list()
        for char in message:
            encrypted_char = pow(ord(char), self.e) % self.n
            char_list.append(encrypted_char)
        return char_list

    def decrypt(self, cipher):
        char_list = list()
        for char in cipher:
            decrypted_char = pow(char, self.d) % self.n
            char_list.append(chr(decrypted_char))
        return char_list
