'''
Enumerating Gene Orders
'''

n = 0
arr = []

def solve(k):
    if k == n:
        for a in arr: print(a, end=" ")
        print()
        return

    for i in range(1, n+1):
        if i in arr: continue
        arr.append(i)
        solve(k+1)
        arr.pop()
        
def length(k):
    result = 1
    for i in range(k):
        result *= (i+1)
    print(result)
 
 
with open("rosalind_perm.txt") as f:
    n = int(f.readline())
    length(n)       
    solve(0)
