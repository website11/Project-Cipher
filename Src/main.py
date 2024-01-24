import CryptographyMenus as cm

if __name__ == '__main__':
    print("Project Cipher\n")
    while True:
        print("Select a Cipher")
        print("1. Caesar Cipher")
        print("2. Aristocrat Cipher")
        print("3. Baconian Cipher")
        print("4. Exit")
        choice = input("Select an Option (ex. 1):\n")

        # Caesar Cipher
        if choice == "1":
            cm.caesar_cipher_menu()

        elif choice == "2":
            cm.aristocrat_menu()

        elif choice == "3":
            cm.baconian_menu()
        elif choice == "4":
            break
        else:
            print("Input Not Valid\n")