
# Attempt to solve cryptogram through tetragram statistics




'''
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
            
            
                        elif choice == "3":
                split_solver = solver.split()
                word_dict = {i + 1: word for i, word in enumerate(split_solver)}
                print(word_dict)
                print("----------")
                option = input("Enter the corresponding number to the word you want to guess!\n")
                if option.isdigit() and (int(option) <= len(word_dict.keys())):
                    guess = self.generate_guess(word_dict.get(int(option)))

                    # Filling in the blank with the guess
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
            '''