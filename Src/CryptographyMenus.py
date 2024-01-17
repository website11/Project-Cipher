from Cryptography import AristocratCipher, CaesarCipher
import os


def caesar_cipher_menu():
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
            shift = CaesarCipher.get_valid_shift()

            if shift is None:
                return

            upDown = input("Shift Up or Down? (Up/Down):\n")
            print(upDown)
            if upDown.lower() != "up" and upDown.lower() != "down":
                print("Answer Not Valid\n")
            else:
                # Valid Shift
                cipher = CaesarCipher.CaesarCipher(shift, upDown.lower())
                encrypted_message = cipher.encrypt(message)
                print(encrypted_message)
                print("")

        # Decryption
        elif choice == "2":
            message = input("Enter Message To Decrypt: \n")
            shift = CaesarCipher.get_valid_shift()

            if shift is None:
                return

            upDown = input("Shifted Up or Down? (Up/Down):\n")
            if upDown.lower() != "up" and upDown.lower() != "down":
                print("Answer Not Valid\n")
            else:
                # Valid Shift
                cipher = CaesarCipher.CaesarCipher(shift, upDown.lower())
                decrypted_message = cipher.encrypt(message)
                print(decrypted_message)
                print("")

        # Auto-Decryption
        elif choice == "3":
            file = input("Enter File to Decrypt (One Phrase per Line):\n")
            if not os.path.isfile(file):
                print("File does not exist. Please check the filename and try again.\n")
                continue

            threshold = input("Enter # of English Dictionary Words Threshold:\n")
            upDown = input("Shifted Up or Down? (Up/Down):\n")
            if upDown.lower() != "up" and upDown.lower() != "down":
                print("Answer Not Valid\n")

            cipher = CaesarCipher.CaesarCipher(0, upDown.lower())
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

        # Exit Menu
        elif choice == "4":
            break
        else:
            print("Invalid Option\n")


# Add backtrack option for hints because of potential to be wrong
def aristocrat_menu():
    print("Aristocrat Options\n")
    while True:
        # Options
        print("1. Create an Aristocrat")
        print("2. Manual Aristocrat Solver (from file)")
        print("3. Automated Aristocrat Solver (from file)")
        print("4. Back")
        choice = input("Select an Option (ex. 1):\n")
        if choice == "1":
            print("Work-In-Progress\n")
        elif choice == "2":
            message_file = input("Enter File To Decrypt: \n")
            with open(message_file, "r") as f:
                encrypted_msg = f.read()
                aristocrat_solver = AristocratCipher.AristocratHelper(encrypted_msg)
                aristocrat_solver.decrypt_solver()
        elif choice == "4":
            break
        else:
            print("Invalid Option\n")