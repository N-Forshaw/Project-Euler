### Project Euler
### Problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Notes
# It isn't as simple as multiplying all the numbers from 1 to 20. Instead, all the unique prime factors need to be found. However, these may have to be repeated
# a few times (e.g. to be divisible by 9, the factor 3 must be included twice).

from math import sqrt

def checkIfPrime(n):
    # Checks whether n is prime
    if n == 1:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

def getPrimeFactors(n):
    # Get all the prime factors of n, including duplciates (e.g. 9 would return [3,3]). Do so recursively, finding the lowest prime factor, then
    # sending the remaining part up the stack
    if checkIfPrime(n):
        # Check whether n is itself prime, in which case the only prime factor is n. This is the top of the stack.
        return [n]
    else:
        for i in range(1,int(sqrt(n))+1):
            if (n % i) == 0:
                if checkIfPrime(i):
                    # If n is divisible by a prime, add that to the list and find the prime factors of the n / i
                    primeFactors = getPrimeFactors(n // i)
                    primeFactors.append(i)
                    return primeFactors

def mergePrimeFactors(mainList, newList):
    # Merge the list of prime factors of one number with an existing list. Add a factor to the main list only if it appears more in the new list than the old
    # First, check that lists aren't empty
    if len(newList) > 0:
        for i in newList:
            oldCount = mainList.count(i)
            newCount = newList.count(i)
            diff = newCount - oldCount
            if diff > 0:
                for j in range(0,diff):
                    mainList.append(i)

    return mainList



# Main Program

# Define range to check
lowBound = 2 # Start at 2 since 1 has no prime factors, and any number will be divisible by 1
upBound = 20

# Instantiate an empty list to hold factors
primeFactors = []

# Get a list of the necessary prime factors
for i in range(lowBound, upBound + 1):
    newList = getPrimeFactors(i)
    primeFactors = mergePrimeFactors(primeFactors, newList)

# Instantiate a variable to hold the solution. It should start at 1 since it will be multiplied by the corresponding factors.
solution = 1

for i in primeFactors:
    solution = solution * i

print(solution)
# Solution is 232792560




