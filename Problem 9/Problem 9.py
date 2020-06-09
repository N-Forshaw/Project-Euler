### Project Euler
### Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Notes
# It would be cheating to go find that triplet and just calculate the product of course. We have the condition a < b < c and a + b + c = 1000, so by
# iterating through values of a and b, c is set. We check if a,b and c are a triplet and if so we find the product. This is a fairly brute force method
# so it could take some time.

tripletSum = 1000
flag = False

for a in range(1, tripletSum - 1):
    for b in range(a+1, tripletSum - a):
        c = tripletSum - a - b

        if (a**2 + b**2) == (c**2):
            product = a * b * c
            print(product)
            flag = True


        # Messy break statements to break out of for loops if solution is found. A better alternative would be to use a while loop instead of a for loop
        # but I'm taking a shortcut here since it is only a small program. 
        if flag:
            break

    if flag:
        break

# Solution is 31875000
