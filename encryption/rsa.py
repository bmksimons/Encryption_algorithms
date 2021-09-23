import random
from cipher import Cipher
from crypto_utils import modular_inverse, blocks_from_text, text_from_blocks, generate_random_prime


class RSA(Cipher):

    def __init__(self):
        super().__init__()
        self.keys = self.generate_keys()
        self.encrypting_key = self.keys[0]
        self.decrypting_key = self.keys[1]

    def encode(self, text):
        encoded_message = []
        blocks_integers = blocks_from_text(text, 1)
        for block in blocks_integers:
            encoded_message.append(pow(block, self.encrypting_key[1], self.encrypting_key[0]))
        return encoded_message

    def decode(self, blocks):
        decoded_blocks = []
        for block in blocks:
            decoded_blocks.append(pow(block, self.decrypting_key[1], self.decrypting_key[0]))
        return text_from_blocks(decoded_blocks, 8)

    def generate_keys(self):
        prime_q = generate_random_prime(8)
        prime_p = generate_random_prime(8)
        key_n = prime_p*prime_q
        rho = (prime_p-1)*(prime_q-1)
        key_e = random.randint(3, rho-1)
        key_d = modular_inverse(key_e, rho)
        # has to find a key_d with a modular inverse
        while not key_d:
            key_e = random.randint(3, rho - 1)
            key_d = modular_inverse(key_e, rho)
        # (n, e) is public key for encryption, (n, d) is secret key for decryption
        return (key_n, key_e), (key_n, key_d)

    def verify(self, clear_text):
        encoded_text = self.encode(clear_text)
        decoded_text = self.decode(encoded_text)
        print(clear_text)
        print(decoded_text)
        if clear_text == decoded_text:
            return True
        return False
