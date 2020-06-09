### Project Euler
### Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

#Notes
# I'm not a mathematician but I'm pretty sure predicting primes is a difficult thing. The first method that comes to mind is to start with a list of numbers
# that I suspect contains the 100001st prime (2 to 10001^2 may be a good initial guestt), and iterate, removing all multiples of the next item in the list.
# This does seem like something that will take a while but I have no better ideas at present.

# This method took long enough to run that I added progress printouts, I fully acknowledge that there are likely more efficient ways to go about this.

nthPrime = 10001                # Prime we're searchnig for
upperBound = (nthPrime ** 2)  # Highest number being checked
primes = [2]                   # List of all primes checked thus far
nextPrime = 3                 # Next prime being checked

numList = list(range(3, upperBound+1,2)) # Get a list of all the numbers that could be the nth prime. To start, we neglect all of the even numbers.


# Iterate until we find the prime or run out of numbers
while (len(primes) < nthPrime) and (len(numList) > 0):

    # Check the next prime, removing every multiple (including itself, so it doesn't get checked again) from the list of possible numbers
    for i in numList:
        if i % nextPrime == 0:
            numList.remove(i) # Remove the number if a multiple

    # Add the prime just checked to the list of checked primes
    primes.append(nextPrime)

    # The next prime will be the lowest number (first term) in the list of possible numbers. We of course need to check that there are numbers left.
    if len(numList) > 0:
        nextPrime = numList[0]

    if len(primes) % 100 == 0:
        print("Progress: " + str(len(primes)//100) + "%")

# Once done, display the result
if len(primes) == nthPrime:
    # We found the nth prime
    print(primes[-1])
else:
    # We didn't find the nth prime
    print("Prime not found")
