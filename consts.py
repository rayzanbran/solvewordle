"""
Holds various constants used throughout the program.
"""
THIS = "solvewordle" # name of the main program folder

SCORESFILENAME = f"{THIS}/data/letterscores.csv" # file holding the numerical scores for each letter
LOGFILENAME = f"{THIS}/logs/log.txt"                  # log on rejected words will be written to this file
SCORERLOGFILE = f"{THIS}/logs/scorer-log.txt"         # scorer log file
WORDS = f"{THIS}/data/valid-wordle-words.txt"    # Wordle dictionary

OUT_PER_LINE = 5                                 # Number of solutions that will be printed per line
SOLS_GIVEN = 10                                  # Number of solutions that will be printed, total.