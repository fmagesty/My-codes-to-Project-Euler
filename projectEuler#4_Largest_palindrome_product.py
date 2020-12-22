# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
c = 999

palindrome = 9009

for a in range(100, 1000):
    for c in range(100, 1000):
        n = a * c
        print('%s * %s = %s.' % (a, c, n))
        if str(n)[0] == str(n)[-1] and str(n)[1] == str(n)[-2] and str(n)[2] == str(n)[-3]:
            print('%s * %s = %s, which is a palindrome!' % (a, c, n))
            if n >= palindrome:
                palindrome = n
print(palindrome)
print('Done.')