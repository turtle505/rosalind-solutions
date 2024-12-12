'''
Mortal Fibonacci Rabbits
'''

def fibd(n, k):
    age = [1] + [0] * (k-1)
    for i in range(3, n+1):
        age = [sum(age[1:])] + age[:n-1]
    return sum(age)


with open("rosalind_fibd.txt") as f:
    X = f.readline().split(" ")
    n, k = map(int, X)
    print(fibd(n, k))
