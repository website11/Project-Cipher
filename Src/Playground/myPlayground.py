from collections import Counter
import pandas as pd
import os
import re

# Single Monogram Interpretation
def generate_frequency_table(text):
    frequency_table = {}
    for letter in text:
        if letter.isalpha():
            if letter in frequency_table:
                frequency_table[letter] += 1
            else:
                frequency_table[letter] = 1
    items = sorted(frequency_table.items(), key=lambda item: item[1], reverse=True)
    return items



# Tetragram Interpretation

filenames = os.listdir("Compiled_Books")
text_path = r"/home/alexanderyw/Project-Cipher/Src/TestCases/Aristocrat_Puzzle.txt"
combined_text = ""
# Test
for filename in filenames:
    file_path = os.path.join("Compiled_Books", filename)
    with open(file_path, 'r') as file:
        combined_text += file.read()
clean_text = re.sub(r'[^a-zA-Z]',"",combined_text)
frequency_table = generate_frequency_table(clean_text.upper())
print(frequency_table)

with open(text_path, 'r') as trial:
    puzzle = trial.read()
    frequency_table_test = generate_frequency_table(puzzle)
    print(frequency_table_test)
# Attempt heuristic approach
# Analyze word frequency
# Try word and see if it works