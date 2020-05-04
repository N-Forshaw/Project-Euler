### Project Euler
### Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def getNextPrime(n):
    if n == 1:      # Recursion ends when divided by all primes (thus next number is 1)
        return []   # Return an empty list for the primes to be added to
    else:
        for i in range(2, n+1): # Try divide by all numbers until you find the first whole number multiple, which will be a prime
            if (n % i) == 0:    # Check whether n is divisible by i
                primes = getNextPrime(n//i) # Continue recursion, finding the lowest prime factor of n / i
                primes.append(i)            # Add i to the list of primes from up the stack
                return primes               # Return this list down the stack
        

problemNumber = 600851475143            # The number specified by the problem
primes = getNextPrime(problemNumber)    # Recursively find all prime factors

print(max(primes))  # Display the highest prime factor
