### Project Euler
### Problem 10.2 (Attempt 2)

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Notes
# Previous attempt took much too long, decided to give the sieve of Eratosthenes a try.

primes = [2]
upperBound = 2000000
numbers = list(range(3,upperBound,2))

# Get primes from first segment
p = 3
while len(numbers) > 0:
    # Add next prime to list
    primes.append(p)

    # Remove multiples of p from segment
    np = p
    while np < upperBound:
        if np in numbers:
            numbers.remove(np)
        np += p

    # Move to next prime
    if len(numbers) > 0:
        p = numbers[0]

    # Since this will likely still take a while, add a progress printout
    print(str(len(numbers)) + ' numbers left')

# Calculate and display the sum
print("Primes found, calculating sum")
sumOfPrimes = 0
for i in primes:
    sumOfPrimes += i

print(sumOfPrimes)
