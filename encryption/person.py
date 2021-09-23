import unbreakable


class Person:
    """ Superclass for the classes Sender and Receiver"""

    def __init__(self):
        self.cipher = None
        self.key = ""
        self.encoded_message = ""

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_cipher(self, cipher):
        self.cipher = cipher

    def get_cipher(self):
        return self.cipher

    def set_encoded_message(self, encoded_message):
        self.encoded_message = encoded_message

    def get_encoded_message(self):
        return self.encoded_message

    def operate_cipher(self):
        """ Encodes or decodes a message """


class Sender(Person):
    """ Encrypts a chosen message """

    def __init__(self):
        self.receiver = None
        self.message = ""
        super().__init__()

    def set_receiver(self, receiver):
        self.receiver = receiver

    def get_receiver(self):
        return self.receiver

    def get_message(self):
        return self.message

    def operate_cipher(self):
        self.message = input("Write which message you want to send...")
        encoded_message = self.get_cipher().encode(self.message)
        self.receiver.set_encoded_message(encoded_message)
        return encoded_message


class Receiver(Person):
    """ Decrypts an encoded message sent from the Sender class """

    def operate_cipher(self):
        decoded_message = self.get_cipher().decode(self.get_encoded_message())
        return decoded_message
