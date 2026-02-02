# Score a word using calculated scores for each letter.

import csv
from consts import *

scoresdict = {} # dictionary to store the scores for each letter

# read scores from csv into memory **when module loaded**
with open(SCORESFILENAME, "r", newline='') as scoresfile:
    scoresreader = csv.reader(scoresfile)
    print("loading scorer...")
    for line in scoresreader:
        scoresdict[line[0]] = int(line[1]) # register each letter score
    print("done.")

def score(word):
    """Score a word and return the integer score."""
    score = 0
    for letter in word:
        score += scoresdict[letter]
    
    return score