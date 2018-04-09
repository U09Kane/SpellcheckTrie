
from math import sqrt

# ===== Prime or Not Prime ================================================== #

''' Given a number determine whether it is prime, perferably in O(log(n))'''

p = int(input().strip()) # p is an array of integers
for a0 in range(p):
    n = int(input().strip())
    
    if n == 1:
        print("Not prime")
        has_ans = True

    else:
        has_ans = False

    divisor = 2
    while divisor <= sqrt(n) and not has_ans:
        has_ans = False

        if n % divisor == 0:
            has_ans = True
            print("Not prime")

        divisor += 1
    if not has_ans:
        print("Prime")

# ===== Fibonacci =========================================================== #

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# ===== Davis' Staricase ==================================================== #

'''Davis can jump 1, 2, or 3 steps of a starcase at a time? How many ways can 
he traverse a staricase of length 'n'? Use memoization to get linear time
complexity
'''

def num_jumps(n, memo={}):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = num_jumps(n-1, memo) + num_jumps(n-2, memo) + num_jumps(n-3, memo)
        return memo[n]

# ===== Lonely Integer ====================================================== #

'''Find and list all unique integers in an array of integers 'a'. '''

def lonely_integer(a):
    have_seen = {}
    for i in a:
        if i not in have_seen:
            have_seen[i] = True
        else:
            del have_seen[i]
    for key in have_seen.keys():
        return key