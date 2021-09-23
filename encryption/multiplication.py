import random
from cipher import Cipher
from crypto_utils import modular_inverse


class Multiplication(Cipher):

    def __init__(self):
        super().__init__()
        self.key = self.generate_keys()

    def encode(self, text):
        encoded_message = ""
        for char in text:
            num_val = ((ord(char) * self.key - 32) % 95) + 32
            encoded_message += chr(num_val)
        return encoded_message

    def decode(self, text, key=None):
        if key is None:
            key = self.key
        decoded_message = ""
        inverse = modular_inverse(key, 95)
        for char in text:
            cod_val = ((ord(char)*inverse - 32) % 95) + 32
            decoded_message += chr(cod_val)
        return decoded_message

    def generate_keys(self):
        ran_int = random.randint(1, 500)
        while True:
            if not modular_inverse(ran_int, 95):
                ran_int = random.randint(1, 500)
            else:
                return ran_int
        return False

    def get_possible_keys(self):
        possible_keys = []
        for i in range(1, 500):
            if not modular_inverse(i, 95):
                continue
            possible_keys.append(i)
        return possible_keys

    def verify(self, clear_text):
        encoded_text = self.encode(clear_text)
        decoded_text = self.decode(encoded_text)
        print(clear_text)
        print(decoded_text)
        if clear_text == decoded_text:
            return True
        return False
