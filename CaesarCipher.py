import enchant
import re

d = enchant.Dict("en_US")

class CaesarCipher:
    def __init__(self, shift=1, upDown="up"):
        self.shift = shift
        self.upDown = upDown
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if upDown == "up":
            self.encrypted_alphabet = (self.alphabet[self.shift:] +
                                    self.alphabet[:self.shift])
        else:
            self.encrypted_alphabet = (self.alphabet[-self.shift:] +
            self.alphabet[:-self.shift])

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

    def auto_decrypt(self, message, threshold):
        shift = 0
        while shift <= 25:
            passed = 0
            decrypted_message = ""
            if self.upDown == "up":
                self.encrypted_alphabet = (self.alphabet[shift:] +
                                          self.alphabet[:shift])
            else:
                self.encrypted_alphabet = (self.alphabet[-shift:] +
                self.alphabet[:-shift])
            for char in message:
                if char.isalpha():
                    char_index = self.encrypted_alphabet.index(char.upper())
                    decrypted_char = self.alphabet[char_index]
                    decrypted_message += decrypted_char
                else:
                    decrypted_message += char
            words = decrypted_message.split(" ")
            for word in words:
                word = re.sub('[^a-zA-Z]', '', word)
                if d.check(word):
                    passed += 1
            if passed >= threshold:
                return decrypted_message, shift
            else:
                shift += 1
        return message, "ERROR"

