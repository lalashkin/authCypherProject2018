import Tests
import RSAModule


if __name__ == '__main__':

    try:
        Tests.test_DES()
        Tests.test_3DES_EDE()
        Tests.test_RCA4()
        Tests.test_RSA()

        print("\nAll tests passed successfully!")

    except AssertionError:

        print("\nCannot assert cyphers!")



