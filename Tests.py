import binascii

from RC4Module import RC4
from DESModule import DES, DES3, convert_from_bin
from RSAModule import RSA


def test_DES():
    print("-->", "Starting DES cypher test\n")
    key1 = "MySecretKey"
    plaintext1 = "My aunt is ill!"
    des1 = DES(key1)
    cypher1 = des1.DES_encrypt(plaintext1)
    decypher1 = convert_from_bin(''.join(des1.DES_decrypt(cypher1)), des1.msg_indices)
    print("Key:", key1)
    print("Encrypted bits: " + ''.join(cypher1))
    print("Decrypted text: " + decypher1, "\n")

    assert plaintext1 == decypher1, "Plaintext should be equal: " + plaintext1

    key2 = "WhoDid911"
    plaintext2 = "Nobody knows :c"
    des2 = DES(key2)
    cypher2 = des2.DES_encrypt(plaintext2)
    decypher2 = convert_from_bin(''.join(des2.DES_decrypt(cypher2)), des2.msg_indices)
    print("Key:", key2)
    print("Encrypted bits: " + ''.join(cypher2))
    print("Decrypted text: " + decypher2, "\n")

    assert plaintext2 == decypher2, "Plaintext should be equal: " + plaintext2

    key3 = "Pssst!"
    plaintext3 = "It's free real estate!"
    des3 = DES(key3)
    cypher3 = des3.DES_encrypt(plaintext3)
    decypher3 = convert_from_bin(''.join(des3.DES_decrypt(cypher3)), des3.msg_indices)
    print("Key:", key3)
    print("Encrypted bits: " + ''.join(cypher3))
    print("Decrypted text: " + decypher3, "\n")

    assert plaintext3 == decypher3, "Plaintext should be equal: " + plaintext3


def test_3DES_EDE():
    print("-->", "Starting 3DES-EDE cypher test\n")
    keys1 = ["Somebody", "once", "told me"]
    plaintext1 = "The world is gonna roll me"
    des1 = DES3(keys1)
    cypher1 = des1.DES3_encrypt(plaintext1)
    decypher1 = convert_from_bin(''.join(des1.DES3_decrypt(cypher1)), des1.msg_indices)
    print("Key:", keys1)
    print("Encrypted bits: " + ''.join(cypher1))
    print("Decrypted text: " + decypher1, "\n")

    assert plaintext1 == decypher1, "Plaintext should be equal: " + plaintext1

    keys2 = ["Hit", "or", "miss"]
    plaintext2 = "I guess they never miss, huh?"
    des2 = DES3(keys2)
    cypher2 = des2.DES3_encrypt(plaintext2)
    decypher2 = convert_from_bin(''.join(des2.DES3_decrypt(cypher2)), des2.msg_indices)
    print("Key:", keys2)
    print("Encrypted bits: " + ''.join(cypher2))
    print("Decrypted text: " + decypher2, "\n")

    assert plaintext2 == decypher2, "Plaintext should be equal: " + plaintext2

    key3 = "Pssst!"
    plaintext3 = "It's free real estate!"
    des3 = DES(key3)
    cypher3 = des3.DES_encrypt(plaintext3)
    decypher3 = convert_from_bin(''.join(des3.DES_decrypt(cypher3)), des3.msg_indices)
    print("Encrypted bits: " + ''.join(cypher3))
    print("Decrypted text: " + decypher3, "\n")

    assert plaintext3 == decypher3, "Plaintext should be equal: " + plaintext3


def test_RCA4():

    print("-->", "Starting RCA-4 cypher test\n")

    key1 = "Key"
    plain1 = "Plaintext"
    encryptor1 = RC4(key1)
    decryptor1 = RC4(key1)
    crypt1 = encryptor1.encrypt(plain1.encode("ASCII"), len(plain1.encode("ASCII")))
    decrypt1 = decryptor1.decrypt(crypt1, len(crypt1))
    print("Key:", key1)
    print("Encrypted text 1: ", binascii.hexlify(crypt1))
    print("Decrypted text 3:", decrypt1.decode("ASCII"), "\n")

    key2 = "Wiki"
    plain2 = "pedia"
    encryptor2 = RC4(key2)
    decryptor2 = RC4(key2)
    crypt2 = encryptor2.encrypt(plain2.encode("ASCII"), len(plain2.encode("ASCII")))
    decrypt2 = decryptor2.decrypt(crypt2, len(crypt2))
    print("Key:", key2)
    print("Encrypted text 2: ", binascii.hexlify(crypt2))
    print("Decrypted text 3:", decrypt2.decode("ASCII"), "\n")

    key3 = "Secret"
    plain3 = "Attack at dawn"
    encryptor3 = RC4(key3)
    decryptor3 = RC4(key3)
    crypt3 = encryptor3.encrypt(plain3.encode("ASCII"), len(plain3.encode("ASCII")))
    decrypt3 = decryptor3.decrypt(crypt3, len(crypt3))
    print("Key:", key3)
    print("Encrypted text 3: ", binascii.hexlify(crypt3))
    print("Decrypted text 3:", decrypt3.decode("ASCII"), "\n")

    # https://en.wikipedia.org/wiki/RC4#Test_vectors

    assert binascii.hexlify(crypt1) == b'BBF316E8D940AF0AD3'.lower(), "Cypher should be equal BBF316E8D940AF0AD3"
    assert binascii.hexlify(crypt2) == b'1021BF0420'.lower(), "Cypher should be equal 1021BF0420"
    assert binascii.hexlify(crypt3) == b'45A01F645FC35B383552544B9BF5'.lower(), "Cypher should be equal " \
                                                                                "45A01F645FC35B383552544B9BF5"
    assert decrypt3.decode("ASCII") == plain3, "Text should be: " + plain3


def test_RSA():
    print("-->", "Starting RSA cypher test\n")
    plaintext1 = "You spin me right round!"
    rsa1 = RSA()
    cypher1 = rsa1.encrypt(plaintext1)
    decypher1 = rsa1.decrypt(cypher1)
    print("Public Key:", rsa1.e)
    print("Private Key:", rsa1.d)
    print("Encrypted bits: ", cypher1)
    print("Decrypted text: " + ''.join(decypher1), "\n")

    assert plaintext1 == ''.join(decypher1), "Plaintext should be equal: " + plaintext1

    plaintext2 = "Cotton eyed Joe"
    rsa2 = RSA()
    cypher2 = rsa2.encrypt(plaintext2)
    decypher2 = rsa2.decrypt(cypher2)
    print("Public Key:", rsa2.e)
    print("Private Key:", rsa2.d)
    print("Encrypted bits: ", cypher2)
    print("Decrypted text: " + ''.join(decypher2), "\n")

    assert plaintext2 == ''.join(decypher2), "Plaintext should be equal: " + plaintext2

    plaintext3 = "Thessaloniki"
    rsa3 = RSA()
    cypher3 = rsa3.encrypt(plaintext3)
    decypher3 = rsa3.decrypt(cypher3)
    print("Public Key:", rsa3.e)
    print("Private Key:", rsa3.d)
    print("Encrypted bits: ", cypher3)
    print("Decrypted text: " + ''.join(decypher3), "\n")

    assert plaintext3 == ''.join(decypher3), "Plaintext should be equal: " + plaintext3
