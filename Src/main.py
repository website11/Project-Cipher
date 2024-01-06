from CaesarCipher import CaesarCipher
import CaesarCipher

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
            CaesarCipher.caesar_cipher()

        elif choice == "3":
            break
        else:
            print("Input Not Valid\n")