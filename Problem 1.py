### Project Euler
### Problem 1

### If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

### Find the sum of all the multiples of 3 or 5 below 1000.

# Define a function to sum all multiples of an integer n in a range

def sumMults(n, start=0, end=1000):
    total = 0
    number = 0
    while number < end:
        total += number
        number += n

    return total

# Main program
result = sumMults(3) + sumMults(5) - sumMults(15)
print(result)
        
