# building on scorer-setup, now take the data in counts.csv and use it 
# to generate the weight for each letter.
import csv

countsdict = {} # dictionary to store the count of each letter
total = 0
scoresdict = {} # dictionary to store the scores of each letter
vowels = 'aeiou'


# read counts
with open("wordle/counts.csv", "r", newline='') as countsfile:
    countsreader = csv.reader(countsfile)

    for row in countsreader:
        countsdict[row[0]] = int(row[1])
        scoresdict[row[0]] = 0 # initialize appropriate spots in scoresdict
        total += int(row[1])


# find percentage out of 100 of each letter
for letter in list(countsdict.keys()):
    scoresdict[letter] = int(1000000 * round(countsdict[letter] / total, 6)) 
    # round each % to six digits and turn it into an int so the computer
    # can do integer math instead of floating point math

# save scores to scores.csv
with open("wordle/letterscores.csv", "w", newline='') as scoresfile:
    scoreswriter = csv.writer(scoresfile)
    for item in list(scoresdict.items()):
        scoreswriter.writerow([item[0], item[1]])