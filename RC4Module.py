
class RC4:

    def __init__(self, user_key):

        self.key = user_key
        self.x = 0
        self.y = 0
        self.s = self.ksa()

    def ksa(self):

        S = bytearray()

        byte_key = self.key.encode("ASCII")

        for i in range(0, 256):
            S.append(i)

        j = 0

        for i in range(0, 256):
            j = (j + S[i] + byte_key[i % len(byte_key)]) % 256
            S[i], S[j] = S[j], S[i]

        return S

    def prga(self):
        self.x = (self.x + 1) % 256
        self.y = (self.y + self.s[self.x]) % 256

        self.s[self.x], self.s[self.y] = self.s[self.y], self.s[self.x]

        return self.s[(self.s[self.x] + self.s[self.y]) % 256]

    def encrypt(self, data, size):
        data_list = data[:size]
        cipher = bytearray()

        for m in range(len(data_list)):
            cipher.append(data_list[m] ^ self.prga())

        return cipher

    def decrypt(self, data, size):
        return self.encrypt(data, size)

