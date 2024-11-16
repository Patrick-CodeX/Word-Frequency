

import json

#file_name = input("Input a file you want to calculate. ")

file_name = "File.txt"

with open(file_name, "r") as file:

    content = file.read()

words = content.split()

word_freq = {}

# Count the frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Print the word frequencies

output_file = "Word_Frequencies"

with open(output_file, "w") as file2:
    for word, freq in word_freq.items():
        file2.write(f"{word}:{freq}\n")

