from cipher import Cipher
from caesar import Caesar
from multiplication import Multiplication
from crypto_utils import modular_inverse


class Affine(Cipher):

    def __init__(self):
        super().__init__()
        self.multi = Multiplication()
        self.cae = Caesar()
        self.key = (self.multi.generate_keys(), self.cae.generate_keys())

    def encode(self, text):
        encoded_message = ""
        for char in text:
            cod_val = ((self.key[0]*ord(char) + self.key[1] - 32) % 95) + 32
            encoded_message += chr(cod_val)
        return encoded_message

    def decode(self, text, key=None):
        if key is None:
            key = self.key
        decoded_message = ""
        mod = modular_inverse(key[0], 95)
        for char in text:
            cod_val = (((ord(char) - self.key[1])*mod - 32) % 95) + 32
            decoded_message += chr(cod_val)
        return decoded_message

    def get_possible_keys(self):
        return [(x, y) for x in self.multi.get_possible_keys() for y in self.cae.get_possible_keys()]

    def verify(self, clear_text):
        encoded_text = self.encode(clear_text)
        decoded_text = self.decode(encoded_text)
        print(clear_text)
        print(decoded_text)
        if clear_text == decoded_text:
            return True
        return False
