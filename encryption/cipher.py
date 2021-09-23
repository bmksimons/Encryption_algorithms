
class Cipher:
    """ pylint, unnecessary pass..........."""

    def encode(self, text):
        """
        @:argument text: the text to encode
        @:return the encoded text
        """

    def decode(self, text, key):
        """
        @:argument text: the encoded text
        @:argument key: None
        @:return the decoded text
        """

    def generate_keys(self):
        """
        @:return generates a random key suitable for the cipher
        """

    def get_possible_keys(self):
        """
        @:return all suitable keys for the cipher
        """

    def verify(self, clear_text):
        """
        @:argument clear_text: message to encode and decode
        @:return True if the text is encodede and decoded correctly, False otherwise
        """
