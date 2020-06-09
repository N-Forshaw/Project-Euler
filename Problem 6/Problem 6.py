### Project Euler
### Problem 6

# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Notes
# It can be shown that sum(n)^2 - sum(n^2) is equal to the sum of the pair products of the numbers, i.e. sum(nm). Since nm = mn, the difference is twice
# the sum of unique pairs in this way.

limit = 100  # Limit to check up until, i.e. first 100 natural numbers

difference = 0

# Iterate through the numbers
for i in range(0,limit+1):
    # Iterate through all the higher numbers. In doing so, this avoids checking the same product twice, since nm = mn. Theoretically this should halve the
    # Number of iterations
    for j in range(i+1,limit+1):
        difference += (2 * i * j) # Add this term to the final solution

print(difference) # Output result

# Solution is 25164150
        
