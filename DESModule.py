import textwrap, binascii


PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50,
       42, 34, 26, 18, 10, 2, 59, 51, 43, 35,
       27, 19, 11, 3, 60, 52, 44, 36, 63, 55,
       47, 39, 31, 23, 15, 7, 62, 54, 46, 38,
       30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33,
       48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

EXPANSION_TABLE = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12,
                   13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24,
                   25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

SBOX = [
    # Box-1
    [
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    # Box-2

    [
    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],

    # Box-3

    [
    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

    ],

    # Box-4
    [
    [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],

    # Box-5
    [
    [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    # Box-6

    [
    [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

    ],
    # Box-7
    [
    [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    # Box-8

    [
    [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]

]

PERMUTATION_TABLE = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
                     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

INITIAL_PERMUTATION_TABLE = ['58 ', '50 ', '42 ', '34 ', '26 ', '18 ', '10 ', '2',
                             '60 ', '52 ', '44 ', '36 ', '28 ', '20 ', '12 ', '4',
                             '62 ', '54 ', '46 ', '38 ', '30 ', '22 ', '14 ', '6',
                             '64 ', '56 ', '48 ', '40 ', '32 ', '24 ', '16 ', '8',
                             '57 ', '49 ', '41 ', '33 ', '25 ', '17 ', '9 ', '1',
                             '59 ', '51 ', '43 ', '35 ', '27 ', '19 ', '11 ', '3',
                             '61 ', '53 ', '45 ', '37 ', '29 ', '21 ', '13 ', '5',
                             '63 ', '55 ', '47 ', '39 ', '31 ', '23 ', '15 ', '7']


INVERSE_PERMUTATION_TABLE = ['40 ', '8 ', '48 ', '16 ', '56 ', '24 ', '64 ', '32',
                             '39 ', '7 ', '47 ', '15 ', '55 ', '23 ', '63 ', '31',
                             '38 ', '6 ', '46 ', '14 ',  '54 ', '22 ', '62 ', '30',
                             '37 ', '5 ', '45 ', '13 ', '53 ', '21 ', '61 ', '29',
                             '36 ', '4 ', '44 ', '12 ', '52 ', '20 ', '60 ', '28',
                             '35 ', '3 ', '43 ', '11 ', '51 ', '19 ', '59 ', '27',
                             '34 ', '2 ', '42 ', '10 ', '50 ', '18 ', '58 ', '26',
                             '33 ', '1 ', '41 ', '9 ', '49 ', '17 ', '57 ', '25']


def apply_PC1(pc1_table, keys_64bits):
    keys_56bits = ""
    for index in pc1_table:
        keys_56bits += keys_64bits[index-1]
    return keys_56bits


def split(keys_56bits):
    left_keys, right_keys = keys_56bits[:28], keys_56bits[28:]
    return left_keys, right_keys


def circular_left_shift(bits, numberofbits):
    shiftedbits = bits[numberofbits:] + bits[:numberofbits]
    return shiftedbits


def apply_PC2(pc2_table, keys_56bits):
    keys_48bits = ""
    for index in pc2_table:
        keys_48bits += keys_56bits[index-1]
    return keys_48bits


def generate_keys(key_64bits):
    round_keys = list()
    pc1_out = apply_PC1(PC1, key_64bits)
    L0, R0 = split(pc1_out)
    for round_number in range(16):
        newL = circular_left_shift(L0, round_shifts[round_number])
        newR = circular_left_shift(R0, round_shifts[round_number])
        round_keys.append(''.join(apply_PC2(PC2, newL + newR)))
        L0 = newL
        R0 = newR
    return round_keys


def apply_expansion(exp_table, bits32):
        bits48 = ""
        for index in exp_table:
            bits48 += bits32[index-1]
        return bits48


def XOR(bits1, bits2):
    xor_result = ""
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]:
                xor_result += '0'
        else:
            xor_result += '1'
    return xor_result


def split_6bits(XOR_48bits):
    list_6bits = textwrap.wrap(XOR_48bits, 6)
    return list_6bits


def get_f_and_l_bit(bits6):
    twobits = bits6[0] + bits6[-1]
    return twobits


def get_middle_bits(bits6):
    fourbits = bits6[1:5]
    return fourbits


def sbox_lookup(sbox, first_last, middle4):
    sbox_value = SBOX[sbox][int(first_last, base=2)][int(middle4, base=2)]
    return bin(sbox_value)[2:].zfill(4)


def final_permutation(perm_table, sbox_32bits):
    final_32bits = ""
    for index in perm_table:
        final_32bits += sbox_32bits[index-1]
    return final_32bits


def round_function(pre32bits, key_48bits):
    result = ""
    expanded_left = apply_expansion(EXPANSION_TABLE, pre32bits)
    xor_value = XOR(expanded_left, key_48bits)
    bits6list = split_6bits(xor_value)
    for sboxcount, bits6 in enumerate(bits6list):
        first_last = get_f_and_l_bit(bits6)
        middle4 = get_middle_bits(bits6)
        sboxvalue = sbox_lookup(sboxcount, first_last, middle4)
        result += sboxvalue
    final32bits = final_permutation(PERMUTATION_TABLE, result)
    return final32bits


def convert_to_bin(item):
    item_bytes = list()
    bytes_indices = list()
    for char in item:
        item_bytes.append(bin(int.from_bytes(char.encode("ASCII"), 'big'))[2:])
        bytes_indices.append(len(bin(int.from_bytes(char.encode("ASCII"), 'big'))[2:]))
    return ''.join(item_bytes), bytes_indices


def convert_from_bin(item, indices):
    item = list(item)
    item_chars = list()

    for indice in indices:
        char = ""
        for i in range(indice):
            char += item[0]
            item.pop(0)
        char = int(char, 2)
        char = char.to_bytes((char.bit_length() + 7) // 8, 'big').decode("ASCII")
        item_chars.append(char)
    return ''.join(item_chars)


def apply_permutation(perm_table, plaintext):
    permutated_ptext = ""
    for index in perm_table:
        permutated_ptext += plaintext[int(index)-1]
    return permutated_ptext


def add_till_64(small_block):
    while len(small_block) < 64:
        small_block = small_block + '0'
    return small_block


class DES3:

    def __init__(self, keys):
        self.keys = list()
        for key in keys:
            current_key, keys_indices = convert_to_bin(key)[:64]
            self.keys.append(current_key)
        self.roundkeys = list()
        self.msg_indices = list()

    def DES3_encrypt(self, message):
        cipher = list()

        byte_message, self.msg_indices = convert_to_bin(message)

        byte_message = textwrap.wrap(byte_message, 64)

        for i, key in enumerate(self.keys):

            temp_cypher = list()

            if len(key) < 64:
                key = add_till_64(key)

            self.roundkeys = generate_keys(key)

            for msg_block in byte_message:

                if len(msg_block) < 64:
                    msg_block = add_till_64(msg_block)

                p_plaintext = apply_permutation(INITIAL_PERMUTATION_TABLE, msg_block)
                L, R = p_plaintext[:32], p_plaintext[32:]

                if i == 1:
                    for round in range(16):
                        newR = XOR(L, round_function(R, self.roundkeys[15 - round]))
                        newL = R
                        R = newR
                        L = newL
                else:
                    for round in range(16):
                        newR = XOR(L, round_function(R, self.roundkeys[round]))
                        newL = R
                        R = newR
                        L = newL

                temp_cypher.append(apply_permutation(INVERSE_PERMUTATION_TABLE, R+L))

            byte_message = temp_cypher

        cipher = byte_message
        return cipher

    def DES3_decrypt(self, cipher):
        decipher = list()
        temp_cypher = cipher

        for i, key in enumerate(self.keys[::-1]):

            temp_msg = list()

            if len(key) < 64:
                key = add_till_64(key)

            self.roundkeys = generate_keys(key)

            for msg_block in temp_cypher:

                p_plaintext = apply_permutation(INITIAL_PERMUTATION_TABLE, msg_block)
                L, R = p_plaintext[:32], p_plaintext[32:]

                if i == 1:
                    for round in range(16):
                        newR = XOR(L, round_function(R, self.roundkeys[round]))
                        newL = R
                        R = newR
                        L = newL
                else:
                    for round in range(16):
                        newR = XOR(L, round_function(R, self.roundkeys[15 - round]))
                        newL = R
                        R = newR
                        L = newL

                temp_msg.append(apply_permutation(INVERSE_PERMUTATION_TABLE, R+L))

            temp_cypher = temp_msg

        decipher = temp_cypher
        return decipher


class DES:

    def __init__(self, key):
        self.key, self.keyindices = convert_to_bin(key)[:64]
        self.roundkeys = list()
        self.msg_indices = list()

    def DES_encrypt(self, message):
        cipher = list()

        byte_message, self.msg_indices = convert_to_bin(message)

        byte_message = textwrap.wrap(byte_message, 64)

        if len(self.key) < 64:
            self.key = add_till_64(self.key)

        self.roundkeys = generate_keys(self.key)

        for msg_block in byte_message:

            if len(msg_block) < 64:
                msg_block = add_till_64(msg_block)

            p_plaintext = apply_permutation(INITIAL_PERMUTATION_TABLE, msg_block)
            L, R = p_plaintext[:32], p_plaintext[32:]

            for round in range(16):
                newR = XOR(L, round_function(R, self.roundkeys[round]))
                newL = R
                R = newR
                L = newL

            cipher.append(apply_permutation(INVERSE_PERMUTATION_TABLE, R+L))

        return cipher

    def DES_decrypt(self, cipher):
        decipher = list()

        for block in cipher:

            p_plaintext = apply_permutation(INITIAL_PERMUTATION_TABLE, block)
            L, R = p_plaintext[:32], p_plaintext[32:]

            for round in range(16):
                newR = XOR(L, round_function(R, self.roundkeys[15 - round]))
                newL = R
                R = newR
                L = newL

            decipher.append(apply_permutation(INVERSE_PERMUTATION_TABLE, R+L))

        return decipher
