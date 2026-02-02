"""
Holds various consts used throughout the program.
"""
THIS = "solvewordle" # name of the main program folder

SCORESFILENAME = f"{THIS}/data/letterscores.csv" # file holding the numerical scores for each letter
LOGFILENAME = f"{THIS}/log.txt"                  # log on rejected words will be written to this file
WORDS = f"{THIS}/data/valid-wordle-words.txt"    # Wordle dictionary