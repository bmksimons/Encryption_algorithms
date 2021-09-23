import random
from cipher import Cipher


class Caesar(Cipher):

    def __init__(self):
        super().__init__()
        self.key = self.generate_keys()

    def encode(self, text):
        encoded_message = ""
        for char in text:
            num_val = ord(char) + self.key
            encoded_message += chr(num_val)
        return encoded_message

    def decode(self, text, key=None):
        if key is None:
            key = self.key
        decoded_message = ""
        for char in text:
            cod_val = (ord(char) - key)
            decoded_message += chr(cod_val)
        return decoded_message

    def generate_keys(self):
        return random.randint(0, 95)

    def get_possible_keys(self):
        return list(range(0, 95))

    def verify(self, clear_text):
        encoded_text = self.encode(clear_text)
        decoded_text = self.decode(encoded_text)
        print(clear_text)
        print(decoded_text)
        if clear_text == decoded_text:
            return True
        return False
