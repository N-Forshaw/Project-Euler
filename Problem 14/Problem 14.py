### Project Euler
### Problem 14

#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

# Notes:
# A simple approach that I will take first would be just to iterate through teh first million numbers, count the length of the sequence, and
# brute force find the longest. One shortcut would be to check if a power of 2 is reached (which would lead straight back to 1) or to keep a
# record of the chain lengths from the numbers lower than the start number, however I chose to stick with the brute force method as it is simplest
# and found the solution in a reasonable time frame

upperBound = 1000000 # Highest number (i.e. we're checking under this)
longestChain = 0 # length of longest chain found so far
longChainStartNum = 0

# Iterate through each number
for i in range(1,upperBound):
    n = i
    chainLength = 0
    # Run until we reach 1 (where it is believed each series finish, and I think it's fair to assume they do for this problem)
    while n != 1:

        # Check if odd or even and move to next number
        if (n % 2) == 0:
            # Even
            n = n / 2
        else:
            # Odd
            n = 3*n + 1

        chainLength += 1

    if chainLength > longestChain:
        longestChain = chainLength
        longChainStartNum = i

# Once all have been checked, display the number that gave the longest chain
print(longChainStartNum)
# Solution: 837799
