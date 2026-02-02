"""
Clears the logfile.
"""
from consts import *

with open(LOGFILENAME, "w") as logfile:
    logfile.write("")