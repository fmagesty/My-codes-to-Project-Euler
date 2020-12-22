# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

num = 13195
primeNums =[]

# finding prime numbers from 2 to 600851475143:
for n in range(2, int(math.sqrt(13195))):
    if num % n == 0:
        primeNums.append(n)



print('numeros: %s' % (primeNums))