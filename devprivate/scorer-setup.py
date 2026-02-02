# count the number of times letters appear in the wordle dictionary.
# store counts in counts.csv

import csv

lettercounts = []

# populate counts with 0
for i in range(26):
    lettercounts.append(0)

# count letters in every word
with open("wordle/valid-wordle-words.txt", "r") as dictionary:
    word = dictionary.readline()
    word = word[:4]
    print(word)
    while len(word) > 1: # every word in the wordle dict is 5 chars long
        for letter in word:
            #print(letter)
            if letter.isalnum():
                lettercounts[ord(letter) - ord('a')]+= 1
        word = dictionary.readline()

# print the dictionary values
for i in range(len(lettercounts)):
    print(f"{chr(i + ord('a'))} : {lettercounts[i]}")

# add the dictionary values to the csv
with open("wordle/counts.csv", "w", newline='') as countsfile:
    countswriter = csv.writer(countsfile)

    for i in range(len(lettercounts)):
        countswriter.writerow([chr(i + ord('a')), lettercounts[i]])