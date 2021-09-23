import affine
import rsa
import caesar
import multiplication
import person
import unbreakable


class Test:
    """ Tests the ciphers"""

    def __init__(self):
        self.sender = person.Sender()
        self.receiver = person.Receiver()
        self.cipher = None

    def get_cipher(self):
        return self.cipher

    def set_values(self):
        print("When crypting your message you can choose between the ciphers: "
              "\n 1. Caesar"
              "\n 2. Multiplication"
              "\n 3. Affine"
              "\n 4. Unbreakable"
              "\n 5. RSA")
        cipher_ver = input("Enter the cipher you want...")
        if cipher_ver.lower() == "caesar":
            self.cipher = caesar.Caesar()
        elif cipher_ver.lower() == "multiplication":
            self.cipher = multiplication.Multiplication()
        elif cipher_ver.lower() == "affine":
            self.cipher = affine.Affine()
        elif cipher_ver.lower() == "unbreakable":
            self.cipher = unbreakable.Unbreakable()
        elif cipher_ver.lower() == "rsa":
            self.cipher = rsa.RSA()
        else:
            print("not valid cipher. Try again")
            self.set_values()
        self.sender.set_cipher(self.cipher)
        self.receiver.set_cipher(self.cipher)
        self.sender.set_receiver(self.receiver)

    """Check's if the encryption algorithm encodes and decodes the message correctly.
    If so, return value is True
    If not, return value is False"""
    def test_encode_decode(self):
        self.sender.operate_cipher()
        message = self.receiver.operate_cipher()
        if message == self.sender.get_message():
            print("After encryption and decryption the message is retrieved as: " + message)
            return True
        return False


def main():
    test_run = Test()
    test_run.set_values()
    test_run.test_encode_decode()


if __name__ == "__main__":
    main()
