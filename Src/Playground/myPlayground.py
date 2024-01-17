from collections import Counter
import pandas as pd

# Single Monogram Interpretation
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

# Tetragram Interpretation

word_df = pd.read_csv("/home/alexanderyw/Project-Cipher/Src/Dependency/unigram_freq.csv")

# Attempt heuristic approach
# Analyze word frequency
# Try word and see if it works