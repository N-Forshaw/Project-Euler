### Project Euler
### Problem 15

#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?

#Notes:
# a 1x1 grid has 2 routes, a 2x2 grid has 6 routes, a 3x3 grid has 20 routes from trial & error. The pattern I see is that a nxn grid has a number of
# routes equal to the central number in the 2n row of pascal's triangle, i.e. 2n C 3.

# The formula for this number is n!/[(n-r)! x r!], letting n = 2n and r = n, this becomes (2n)!/(n!)^2

from math import factorial

n = 20 # we want nxn grid

numOfPaths = int(factorial(2*n)/(factorial(n)**2))

print(numOfPaths)
# Solution = 137846528820

# Note that this is perhaps cheating in a sense, since I just spotted a pattern and did a calculation I could have done on my calculator. I may return to
# this problem and try a program that actually searches each path and counts them. 
