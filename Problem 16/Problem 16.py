### Project Euler
### Problem 16

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

# A simple approach is just to calculate 2^1000 and add the digits

exponent = 1000

twoToExponent = str(2**exponent) # Calculate number and convert to a string so we can easily iterate throuhg digits
sumOfDigits = 0 # variable holding the sum of digits

# Iterate through every digit and add it to the total
for digit in twoToExponent:
    sumOfDigits += int(digit)

# Display result
print(sumOfDigits)
# Solution: 1366
