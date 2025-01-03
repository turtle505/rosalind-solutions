'''
Enumerating k-mers Lexicographically
'''

n = 0
alphabets = []
arr = []
answer = ""

def solve(k):
    if k == n:
        global answer
        answer += ''.join(arr) + '\n'
        return
    
    for i in alphabets:
        arr.append(i)
        solve(k+1)
        arr.pop()


with open("rosalind_lexf.txt") as f:
    alphabets = f.readline().strip().split(" ")
    n = int(f.readline())
    solve(0)
    

with open("solve.txt", 'w') as g:
    g.write(answer)
