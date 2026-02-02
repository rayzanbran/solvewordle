"""
Clears the logfile. Only run if you want to clear the logfile.
"""
from consts import *

with open(LOGFILENAME, "w") as logfile:
    logfile.write("")