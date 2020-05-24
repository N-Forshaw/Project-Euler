### Project Euler
### Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Notes
# There are ~900 3 digit numbers, so 900^2 combinations. However by starting from the top down I can minimse how many I need to check. That being said,
# There's a lot less 6 digit palimdromes (999^2 = 998001, so all products of 3 digit numbers will have max 6 digits). The palindrome will also be less
# than 999^2, so the highest possible palindrome is 997799, then 996699 etc, and so on.

from math import sqrt

def generatePalindrome(a, b, c):
    # Returns the number with digits abccba
    number = (100000 * a) + (10000 * b) + (1000 * c) + (100 * c) + (10 * b) + a
    return number

def checkDivis(n):
    # Checks whether or not n is divisible by 2 3-digit numbers
    for i in range(100,int((sqrt(n)+1))):
        # Check every number up to the square root of n (any number greater than sqrt(n) would have a corresponding factor less than sqrt(n))
        if (n % i) == 0:
            # n is divisible by i. Return true if n/i is 3 digits
            if 100 <= (n // i) < 1000:
                return True

    # If nothing found, return false
    return False

# Main Loop

# Iterate through the digits from 997799 downwards until a suitable palindrome is found

foundSoln = False
firstDigit = 9
secondDigit = 9
thirdDigit = 7

while not foundSoln:

    # Generate the next palindrome
    currentPalindrome = generatePalindrome(firstDigit, secondDigit, thirdDigit)

    # Check this palindrome's divisibility
    if checkDivis(currentPalindrome):
        # If divisible by a 3 digit number, we've found our solution
        foundSoln = True
    else:
        # If not, we need to decrease the digits, starting from the third digit, and adjusting the second and first when the next has become 0
        if thirdDigit != 0:
            thirdDigit -= 1
        else:
            # If third digit = 0, reset to 9 and decrease 2nd digit
            thirdDigit = 9
            if secondDigit != 0:
                secondDigit -= 1
            else:
                # If second digit also = 0, reset second digit to 9 and decrease first digit
                secondDigit = 9
                if firstDigit != 1:
                    firstDigit -= 1
                else:
                    # If third and second digits are 0, and first digit is 1, we've reached the lowest 6 digit palindrome (100001)
                    # and not found a palindrome.
                    print("Failed to find solution")

# Once a solution has been found, display it
print(currentPalindrome)

# Solution : 906609
