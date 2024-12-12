'''
Rabbits and Recurrence Relations
'''

def fib(n, k):
    dp = [0, 1, 1]
    for i in range(3, n+1):
        dp.append(k*dp[i-2] + dp[i-1])   
    return dp[n]


with open("rosalind_fib.txt") as f:
    X = f.readline().split(" ")
    n, k = map(int, X)
    print(fib(n, k))
