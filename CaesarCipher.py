import enchant
import re

d = enchant.Dict("en_US")


def get_valid_shift():
    shift = input("Enter Shift Amount (up to 25): \n")

    # Convert shift to an integer
    try:
        shift = int(shift)
    except ValueError:
        print("Invalid Shift - not a number")
        return None

    # Check if shift is greater than 25
    if shift > 25:
        print("Invalid Shift - greater than 25")
        return None

    # Return the valid shift
    return shift


def caesar_cipher():
    print("Caesar Cipher Options\n")
    while True:
        # Options
        print("1. Encrypt Message")
        print("2. Manual Decrypt (with key)")
        print("3. Automatic Decrypt (no key) - Insert File")
        print("4. Back")
        choice = input("Select an Option (ex. 1):\n")

        # Encryption
        if choice == "1":
            message = input("Enter Message To Encrypt: \n")
            shift = get_valid_shift()

            if shift is None:
                return

            upDown = input("Shift Up or Down? (Up/Down):\n")
            print(upDown)
            if upDown.lower() != "up" and upDown.lower() != "down":
                print("Answer Not Valid\n")
            else:
                # Valid Shift
                cipher = CaesarCipher(shift, upDown.lower())
                encrypted_message = cipher.encrypt(message)
                print(encrypted_message)
                print("")

        # Decryption
        elif choice == "2":
            message = input("Enter Message To Decrypt: \n")
            shift = get_valid_shift()

            if shift is None:
                return

            upDown = input("Shifted Up or Down? (Up/Down):\n")
            if upDown.lower() != "up" and upDown.lower() != "down":
                print("Answer Not Valid\n")
            else:
                # Valid Shift
                cipher = CaesarCipher(shift, upDown.lower())
                decrypted_message = cipher.encrypt(message)
                print(decrypted_message)
                print("")

        # Auto-Decryption
        elif choice == "3":
            file = input("Enter File to Decrypt (One Phrase per Line):\n")
            threshold = input("Enter # of English Dictionary Words Threshold:\n")
            upDown = input("Shifted Up or Down? (Up/Down):\n")
            if upDown.lower() != "up" and upDown.lower() != "down":
                print("Answer Not Valid\n")

            cipher = CaesarCipher(0, upDown.lower())
            if not threshold.isdigit():
                print("Invalid Threshold - not a number")
                return
            with open(file, "r") as f:
                for line in f:
                    decrypted_message, shift = cipher.auto_decrypt(line, int(threshold))
                    if shift != "ERROR":
                        print("Shifted " + str(shift) + " times" + "\n" + decrypted_message)
                    else:
                        print("Code could not be decrypted! Try another threshold!" + "\n" + line)
                print("")
        elif choice == "4":
            break


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

