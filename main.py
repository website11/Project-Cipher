from CaesarCipher import CaesarCipher


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
                        print("Code could not be decrypted! Try another threshold!")

        elif choice == "4":
            break


if __name__ == '__main__':
    print("Project Cipher\n")
    while True:
        print("Select a Cipher")
        print("1. Caesar Cipher")
        print("2. Aristocrat Helper")
        print("3. Exit")
        choice = input("Select an Option (ex. 1):\n")

        # Caesar Cipher
        if choice == "1":
            caesar_cipher()

        elif choice == "3":
            break
        else:
            print("Input Not Valid\n")