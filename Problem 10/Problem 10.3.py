### Project Euler
### Problem 10.3 (Attempt 3)

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Notes
# Previous attempt took much too long, decided to give the sieve of Eratosthenes a try. I realise that using the .remove() method might be causing
# the program to take a long time, so instead I'll use the indexes to reference the number and the value to hold the number's value, which I'll set to
# 0 if not prime.

upperBound = 2000000
numbers = list(range(0,upperBound+1)) # By starting at 0, the index will match the number held at that index

i = 2 # First prime to check
while i < (upperBound+1):

    if numbers[i] != 0:

        # Remove multiples of i from the list (by setting them to 0)
        ni = 2*i # we want to keep i
        while ni < (upperBound+1):
            numbers[ni] = 0
            ni += i
            
    # Increment i
    i += 1

    # Since this will likely still take a while, add a progress printout
    if (i % (upperBound/100)) == 0:
        print(str(i // (upperBound/100)) + "%")

# Calculate and display the sum
print("Primes found, calculating sum")
# Fun note, normally a good idea to remove the diagnostic line that displays the list of what would be 2 million numbers before running 
sumOfPrimes = 0
for i in range(2,upperBound+1):
    sumOfPrimes += numbers[i]

print(sumOfPrimes)
# Solution: 142913828922
