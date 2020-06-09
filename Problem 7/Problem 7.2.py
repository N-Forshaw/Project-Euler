### Project Euler
### Problem 7.2 (2nd attempt)

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

#Notes
# The previous approach took far too long. What I will try this time to to iterate from 7 upwards in steps of 2 (i.e. only check odd numbers),
# and check the next number for divisibility by all the previously identified primes. If it is not divisible by any, it itself is a prime. I continue
# until I find the nth prime.

nthPrime = 10001
oddPrimes = [3,5,7] # Since we're checking only odd numbers, no point checking if divisible by 2.
nextNum = 9

# Iterate until the list of oddPrimes is equal to nthPrime - 1 (the -1 accounting for 2)
while len(oddPrimes) < (nthPrime - 1):
    flag = False

    # Iterate through odd primes until a divisor is found or all primes are checked. Could just check the latter with a for loop, but using
    # a while loop allows the loop to be exited earlier without use of a messy 'break'. 
    i = 0
    while (i < len(oddPrimes)) and not flag:
        
        if nextNum % oddPrimes[i] == 0:
            # If Divisible by a prime
            flag = True # Raise the flag that it is not prime
            
        i += 1 # Increase counter

    
    if not flag:
        # if nextNum is prime, add it to the list
        oddPrimes.append(nextNum)

    nextNum += 2 # Check the next number

print(oddPrimes[-1]) # The nth prime will be the last prime in the list.
# Solution is 104743
