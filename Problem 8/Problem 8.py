### Project Euler
### Problem 8

#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

number = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# Notes
# Of course, any number multiplied by 0 is 0. Thus the consequtive digits must not contain a 0. By splitting this number into series of digits excluding
# the digit 0, we can narrow down the parts of the number that need to be checked.

# Define a function to check a number (given as a string) to find the greatest product of n consecutive digits
def checkChunk(chunk, n):
    highestProduct = 1

    for i in range(0, len(chunk)-n+1):
        product = 1
        for j in range(i, n+i):
            product = product * int(chunk[j])

        if product > highestProduct:
            highestProduct = product

    return highestProduct

# Remove the \n characters
number = number.replace('\n','')

# Split the number into segments not containing the digit 0, and ignore any chunks to small to have the desired product length.
numberChunks = number.split('0')
productLength = 13

for i in numberChunks:
    if len(i) < productLength:
        numberChunks.remove(i)

# Now check all the remaining chunks and note the highest product.
highestProduct = 0

for i in numberChunks:
    chunkHighestProduct = checkChunk(i, productLength)

    if chunkHighestProduct > highestProduct:
        highestProduct = chunkHighestProduct

print(highestProduct)
# Solution: 23514624000
# It is worth noting that the same result is found almost as quickly (I can't tell any difference in speed) by just passing the whole number through the function
# However, if we had a much larger number or requried a much larger product this approach would make more of a difference.
