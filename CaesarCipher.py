
class CaesarCipher:
    def __init__(self, shift=1):
        self.shift = shift
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.encrypted_alphabet = (self.alphabet[self.shift:] +
                                   self.alphabet[:self.shift])

    def __str__(self):
        return self.encrypted_alphabet


    def encrypt(self):
