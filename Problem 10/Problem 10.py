### Project Euler
### Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Notes
# At first I went to copy the code from problem 5 to use the function to check the first million odd numbers, sum them, and add 2. However, I think a
# faster approach would be the one used for problem 7, since it requires less divisors to be checked. The difference is that instead of finding all the
# primes up until the 10001st, I'm finding all the primes up until the number 2 million.

upperBound = 2000000
oddPrimes = [3,5,7] # Since we're checking only odd numbers, no point checking if divisible by 2.
nextNum = 9

# Iterate until we exceed the upper bound
while nextNum < upperBound:
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

# Now we want the sum of these primes. Start with 2 (since this is not in the list) and then add all of the odd primes onto it.
sumOfPrimes = 2

for i in oddPrimes:
    sumOfPrimes += i

print(sumOfPrimes)
