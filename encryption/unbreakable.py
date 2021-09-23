import random
from cipher import Cipher


class Unbreakable(Cipher):

    def __init__(self):
        super().__init__()
        self.key_word = self.generate_keys()

    def encode(self, text):
        """ tar % len(key_word)"""
        encoded_message = ""
        word_index = 0
        for char in text:
            # num_val til char + num_val til key_word % 95. + 32 for å justere for typecast
            cod_val = (((ord(char)) + (ord(self.key_word[word_index]))) % 95) + 32
            encoded_message += chr(cod_val)
            word_index += 1
            if word_index == len(self.key_word):
                word_index = 0
        return encoded_message

    def decode(self, text, key_word=None):
        """  """
        if key_word is None:
            key_word = self.key_word
        dec_word = ""
        for char in key_word:
            dec_index = ((126 - ord(char)) % 95) + 32
            dec_word += chr(dec_index)
        decoded_message = ""
        word_index = 0
        for char in text:
            cod_val = ((ord(char) + ord(dec_word[word_index])) % 95)
            if cod_val < 32:
                cod_val = cod_val + 95
            decoded_message += chr(cod_val)
            word_index += 1
            if word_index == len(dec_word):
                word_index = 0
        return decoded_message

    def generate_keys(self):
        english_words = open("english_words.txt", "r")
        for i in range(0, random.randint(0, 264060)):
            english_words.readline()
        key = english_words.readline().rstrip('\n')
        english_words.close()
        return key

    def get_possible_keys(self):
        english_words = open("english_words.txt", "r")
        possible_keys = []
        for i in range(0, 264060):
            possible_keys.append(english_words.readline().rstrip('\n'))
        english_words.close()
        return possible_keys

    def verify(self, clear_text):
        encoded_text = self.encode(clear_text)
        decoded_text = self.decode(encoded_text)
        print(clear_text)
        print(decoded_text)
        if clear_text == decoded_text:
            return True
        return False
