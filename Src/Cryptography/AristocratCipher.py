import nltk
import pandas as pd
import random
from nltk.corpus import words

nltk.download('words')


# ----------------------------------------------------------------------------------
# Aristocrat Class
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

    def apply_letter_to_solver(self, solver, letter_to_replace, replacement_letter):
        updated_solver = list(solver)
        for i, letter in enumerate(self.encrypted_message):
            if letter == letter_to_replace:
                updated_solver[i] = replacement_letter
        return "".join(updated_solver)

    def generate_frequency_table(self, column_count=8):
        frequency_table = {}
        for letter in self.encrypted_message:
            if letter.isalpha():
                if letter in frequency_table:
                    frequency_table[letter] += 1
                else:
                    frequency_table[letter] = 1
        items = sorted(frequency_table.items(), key=lambda item: item[1], reverse=True)
        return items

    def decrypt_solver(self):
        solver = self.create_empty_message()[:]
        used_letters = {}
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
            print("Used Letters: " + str(list(used_letters.values())))

            print("1. Replace a Letter (ex. A->C)       2. Show Frequency Table")
            print("3. Receive an Automated Guess        4. Check Possible Answer (WIP)")
            print("5. Reset Board                       6. Back")
            choice = input("Select an Option (ex. 1):\n")

            # Replace a letter
            if choice == "1":
                letter_to_replace = input("Enter the letter to replace: \n")
                replacement_letter = input("Enter the replacement letter: \n")
                if letter_to_replace.isalpha() and (replacement_letter.isalpha() or replacement_letter == ""):
                    used_letters[letter_to_replace.upper()] = replacement_letter.upper()
                    if replacement_letter == "":
                        replacement_letter = "_"
                    solver = self.apply_letter_to_solver(solver, letter_to_replace.upper(), replacement_letter.upper())
                    self.current_message = self.apply_letter_to_solver(self.current_message, letter_to_replace.upper(),
                                                                       replacement_letter.upper())
                else:
                    print("Invalid input. Please enter alphabetic characters only.")

            # Show frequency table
            elif choice == "2":
                items = self.generate_frequency_table()
                # format table as columns
                while items:
                    row = items[:8]
                    items = items[8:]
                    for name, count in row:
                        print(f"{name} = {count}", end='\t')
                    print()

                while True:
                    print("1. Back")
                    choice = input("Select an Option (ex. 1):\n")
                    if choice == "1":
                        break

            # Receive Automatic Guess
            elif choice == "3":
                break
            elif choice == "4":
                break
            elif choice == "5":
                solver = self.create_empty_message()[:]
                self.current_message = self.encrypted_message[:]
                used_letters = {}
            elif choice == "6":
                break
            else:
                print("Invalid Option\n")
