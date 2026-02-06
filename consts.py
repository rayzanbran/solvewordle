"""
Holds various constants used throughout the program.
"""
THIS = "solvewordle" # name of the main program folder

SCORESFILENAME = f"{THIS}/data/letterscores.csv" # file holding the numerical scores for each letter
LOGFILENAME = f"{THIS}/log.txt"                  # log on rejected words will be written to this file
WORDS = f"{THIS}/data/valid-wordle-words.txt"    # Wordle dictionary
OUT_PER_LINE = 6                                 # Number of solutions that will be printed per line