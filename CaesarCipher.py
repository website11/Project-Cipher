
class CaesarCipher:
    def __init__(self, shift=1):
        self.shift = shift
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.encrypted_alphabet = (self.alphabet[self.shift:] +
                                   self.alphabet[:self.shift])

    def __str__(self):
        return self.encrypted_alphabet

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                char_index = self.alphabet.index(char.upper())
                encrypted_char = self.encrypted_alphabet[char_index]
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

