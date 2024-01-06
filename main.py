from CaesarCipher import CaesarCipher

def caesar_cipher():
    print("Caesar Cipher Options\n")
    while True:
        print("1. Encrypt Message")
        print("2. Manual Decrypt (with key)")
        print("3. Automatic Decrypt (no key)")
        print("4. Back")
        choice = input("Select an Option (ex. 1):\n")
        # Encryption
        if choice == "1":
            message = input("Enter Message To Encrypt: \n")
            shift = input("Enter Shift Amount (up to 25): \n")

            # Convert shift to an integer
            try:
                shift = int(shift)
            except ValueError:
                print("Invalid Shift - not a number")
                return

            # Check if shift is greater than 25
            if shift > 25:
                print("Invalid Shift - greater than 25")
                return

            # Valid Shift
            cipher = CaesarCipher(shift)
            encrypted_message = cipher.encrypt(message)
            print(encrypted_message)
            print("")

        elif choice == "4":
            break


if __name__ == '__main__':
    print("Project Cipher\n")
    while True:
        print("Select a Cipher")
        print("1. Caesar Cipher")
        print("2. Exit")
        choice = input("Select an Option (ex. 1):\n")

        # Caesar Cipher
        if choice == "1":
            caesar_cipher()

        elif choice == "2":
            break
        else:
            print("Input Not Valid\n")