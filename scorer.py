"""
Scores a word using calculated scores for each letter.
"""

import csv
from consts import *

scoresdict = {} # dictionary to store the scores for each letter
given = []


# read scores from csv into memory **when module loaded**
with open(SCORESFILENAME, "r", newline='') as scoresfile:
    scoresreader = csv.reader(scoresfile)
    print("loading scorer...")
    for line in scoresreader:
        scoresdict[line[0]] = int(line[1]) # register each letter score
    print("done.")

def _calc_letter_score(letter, scored):
    """
    Calculate the score of a letter.
    
    :param letter: the letter to be scored.
    :param scored: array of letters that have already been scored for this word.
    """
    # using info in given and scored, calc word score and return

    score = 0
    score += scoresdict[letter]

    # score mutators
    if letter not in given: # score unentered letters higher
        score *= 2
    if letter in scored: # score repeat letters lower
        score /= 2

    return score

def upd_given(letters):
    """
    Clear and update the already-entered letters.

    :param letters: an array of chars
    """
    # clear given
    global given
    given = []

    # add new letters
    for letter in letters:
        given.append(letter)

def score(word):
    """
    Score a word and return the integer score.

    :param word: string to be scored.
    """
    score = 0

    scored = []

    for letter in word:
        score += _calc_letter_score(letter, scored)
        scored.append(letter)

    return score