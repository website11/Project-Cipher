
def aristocrat_menu():
    print("Aristocrat Options\n")
    while True:
        # Options
        print("1. Create an Aristocrat")
        print("2. Aristocrat Helper (from file)")
        print("3. Back")
        choice = input("Select an Option (ex. 1):\n")
        if choice == "1":
            print("Work-In-Progress\n")
        elif choice == "2":
            encrypted_message = input("Enter Message To Decrypt: \n")
            aristocrat_solver = AristocratHelper(encrypted_message)
            aristocrat_solver.decrypt_solver()
        elif choice == "3":
            break
        else:
            print("Invalid Option\n")


class AristocratHelper:
    def __init__(self, encrypted_message=""):
        self.encrypted_message = encrypted_message
        self.current_message = encrypted_message[:]

    def create_empty_message(self):
        empty_message = ""
        for char in self.encrypted_message:
            if char.isalpha():
                empty_message += "_"
            else:
                empty_message += char
        return empty_message

    def decrypt_solver(self):
        solver = self.create_empty_message()[:]
        while True:
            print("Encrypted View:")
            print(self.encrypted_message)
            print("--------------------------")
            print("Solver View:")
            print(solver)
            print("--------------------------")
            print("Complete View:")
            print(self.current_message)
            print("--------------------------")

            print("1. Replace a Letter (ex. A->C)       2. Show Frequency Table")
            print("3. Receive an Automated Hint (WIP)   4. Check Possible Answer")
            print("5. Reset Board                       6. Back")
            choice = input("Select an Option (ex. 1):\n")
            if choice == "1":
                letter_to_replace = input("Enter the letter to replace: \n")
                replacement_letter = input("Enter the replacement letter: \n")
                # solver = solver.replace(letter_to_replace, replacement_letter)
            elif choice == "2":
                print("Work-In-Progress\n")
                # self.show_frequency_table()
            elif choice == "3":
                print("Work-In-Progress\n")
            elif choice == "4":
                break
            else:
                print("Invalid Option\n")
