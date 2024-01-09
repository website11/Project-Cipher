import nltk
import pandas as pd
import random
from nltk.corpus import words

nltk.download('words')


def aristocrat_menu():
    print("Aristocrat Options\n")
    while True:
        # Options
        print("1. Create an Aristocrat")
        print("2. Aristocrat Solver (from file)")
        print("3. Back")
        choice = input("Select an Option (ex. 1):\n")
        if choice == "1":
            print("Work-In-Progress\n")
        elif choice == "2":
            message_file = input("Enter File To Decrypt: \n")
            with open(message_file, "r") as f:
                encrypted_msg = f.read()
                aristocrat_solver = AristocratHelper(encrypted_msg)
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


    # Still has ongoing issues
    def generate_guess(self, target):
        df = pd.read_csv("Src/Dependency/wordFrequency.csv")
        frequent_words = df['word'].tolist()
        english_words_set = set(words.words())

        # Determine if a word matches the missing blanks
        def match_pattern(word, pattern):
            if len(str(word)) != len(pattern):
                return False
            for i in range(len(pattern)):
                if pattern[i] != '_' and pattern[i] != str(word).upper()[i]:
                    return False
            return True

        guesses = [word for word in frequent_words if match_pattern(word, target)]

        if not guesses:
            guesses = [word for word in english_words_set if match_pattern(word, target)]

        if guesses:
            # Later can implement further ordering by frequency or through context (if available)
            random_word = random.choice(guesses)
            return random_word
        else:
            print("No words matched!")

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
                split_solver = solver.split()
                word_dict = {i + 1: word for i, word in enumerate(split_solver)}
                print(word_dict)
                print("----------")
                option = input("Enter the corresponding number to the word you want to guess!\n")
                if option.isdigit() and (int(option) <= len(word_dict.keys())):
                    guess = self.generate_guess(word_dict.get(int(option)))
                    if guess:
                        split_encrypt = self.encrypted_message.split()
                        old_word = split_encrypt[int(option) - 1]
                        for index, char in enumerate(guess):
                            if char.isalpha():
                                solver = self.apply_letter_to_solver(solver, old_word[index].upper(), char.upper())
                                self.current_message = self.apply_letter_to_solver(self.current_message,
                                                                                   old_word[index].upper(),
                                                                                   char.upper())
                    else:
                        print("No matches found")
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
