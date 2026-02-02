"""This functions as main for the program."""
# Solve wordles.

import wordlesolver as wordle

print("Enter X to exit, or anything else to continue.")
userinput = input()
# main loop
while userinput != ('X') and userinput != ('x'): # sentinels
    wordle.get_inputs()
    wordle.solve()
    wordle.print_sols()

    wordle.reset()
    
    print("Enter X to exit, or anything else to solve another word.")
    userinput = input()

# quit