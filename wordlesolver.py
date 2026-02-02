"""
Finds possible Wordle solutions based on user input.
Saves a log from the most recent run, stored by default in ../log.txt
"""

import scorer
from consts import *

class Guess:
    """
    Class for holding guesses and their scores, for easier sorting.
    """
    def __init__(self, word, score=0):
        """
        initialize a Guess with at least a word.
        """
        self.word = word
        self.score = score
    
    # rich comparators for sorting
    def __gt__(self, other):
        if self.score > other.score:
            return True
        else:
            return False


    def __lt__(self, other):
        if self.score < other.score:
            return True
        else:
            return False
    
    def to_str(self):
        return self.word

masterkey = [] # array of valid wordle solutions

# read wordle dictionary into memory
with open(WORDS, "r") as words:
    for line in words:
        line = line.strip()
        masterkey.append(line)

grays = [] # 1D array tracking gray letters
yellows = [[], [], [], [], []] # 2D array tracking yellow letters at each position. Position 1 is index 0.
greens = [[], [], [], [], []] # 2D array tracking green letters at each position. Position 1 is index 0.

solutions = [] # array tracking all found solutions

# functions
def processyg(inputarr= ['-1'], targetarr= 'y'):
    """ Process inputarr to targetarr.
        inputarr: a non-empty array of tokens in format LN (see any input prompt)
        targetarr: y for yellows, g for greens
    """

    # process LN (L=letter N=number) tokens into appropriate array
    for i in inputarr:
        num = int(i[1]) - 1
        letter = i[0].lower()

        if targetarr == 'y':
            yellows[num].append(letter)
        else:
            greens[num].append(letter)

def get_inputs():
    """Sequentially prompts the user for gray, yellow, and green letters."""
    get_grays()
    get_yellows()
    get_greens()

def get_grays():
    """Gets gray letters from user."""

    # prompt for letters not in word (if any)
    print("Input gray letters (Ex. abcdefg):", end=" ")
    inputstr = input()

    for i in inputstr:
        if i not in grays: # prevent duplicates in grays
            grays.append(i.lower()) # convert letter to lowercase

def get_yellows():
    """Gets yellow letters from user."""
    
    # prompt for letters known to be in the word at unknown position, separated by spaces in format LN 
    # (L = letter | N = position(s) the letter is not at (1,2,3,4,5))
    print("Input yellow letters, separated by spaces, in the format LN(NNNN), where L is the letter and N is any positions where the letter is not at.")
    print("Example: a1234 b5")
    inputstr = input()

    inputarr = inputstr.split() # split into each LN token

    processyg(inputarr, 'y')

def get_greens():
    """Gets green letters from user."""

    # prompt for letters known to be in the word, separated by spaces in format LN (see above section comment)
    print("Input green letters, separated by spaces, in the format LN(NNNN), where L is the letter and N is any position where the letter is known to be.")
    print("Example: a1234 b5")
    inputstr = input()

    inputarr = inputstr.split()

    processyg(inputarr, 'g')

def reset():
    """Clears all user input and found solutions,
       readying the module for a new solve.
    """
    global grays
    global yellows
    global greens
    global solutions

    grays = []
    yellows = [[], [], [], [], []]
    greens = [[], [], [], [], []]
    solutions = []

# check user entered data against valid wordle words

# process: addition (deciding which words to add to the array)
# if at any point the checks fail, will skip past the word and not add it
def solve():
    """Find possible wordle solutions given the data previously provided by the user.
       NOTE: gray, yellow, and green letters must be provided before this is called.
       Logfile is opened and closed within this method.
    """
    logfile = open(LOGFILENAME, "w")

    print("finding solutions...")
    for word in masterkey:
        rejected = False
        # check that yellows are somewhere in word

        if not rejected:
            wordlen = len(word)
            for i in range(wordlen):
                letter = word[i]
                # check grays
                if letter not in grays:
                    pass
                else:
                    logfile.write(f"rejected {word} for gray {letter}\n")
                    break

                # check yellows not at certain locations
                if letter not in yellows[i]:
                    pass
                elif len(yellows[i]) < 1:
                    pass
                else:
                    logfile.write(f"rejected {word} for yellow {letter}\n")
                    break

                # check greens
                if letter in greens[i]:
                    pass
                elif len(greens[i]) < 1:
                    pass
                else:
                    logfile.write(f"rejected {word} for green {letter}\n")
                    break

                # if all letters passed all checks
                # this will only occur once in a word's checking
                if i == wordlen - 1:
                    for yellowlist in yellows:
                        for yellow in yellowlist:
                            if yellow not in word:
                                logfile.write(f"rejected {word} for no {letter}\n")
                                rejected = True
                    
                    if not rejected:
                        solutions.append(Guess(word=word, score=scorer.score(word)))

            continue
    logfile.close()
    solutions.sort(reverse=True)

def print_sols():
    """Print sorted solutions.
       NOTE: solutions must have been generated before this is called.
    """
    # display solutions
    print("guesses: (remember, not all of these are valid final answers!)")
    for i in solutions:
        print(f"{i.to_str()},", end=" ")
    print("\n")


# debug stuff
if(__name__ == "__main__"):
    print(grays)

    print(yellows)

    print(greens)