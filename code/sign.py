'''
Enumerating Oriented Gene Orderings
'''

n = 0
arr = []
result = []
answer = ""

def solve1(k):
    if k == n:
        result.append(arr[:])
        return
    
    for i in range(1, n+1):
        if i in arr: continue
        arr.append(i)
        solve1(k+1)
        arr.pop()
        
def solve2(k, nums):
    global answer
    if k == n:
        answer += ' '.join(map(str, arr)) + '\n'
        return
    
    arr.append(nums[k])
    solve2(k+1, nums)
    arr.pop()
    arr.append(-1*nums[k])
    solve2(k+1, nums)
    arr.pop()
    
    
def sign():
    global answer
    solve1(0)
    answer += str(len(result)*(2**n)) + '\n'
    for perm in result:
        solve2(0, perm)

with open("rosalind_sign.txt") as f:
    X = f.readline()
    n = int(X)
    sign()

with open("solve.txt", 'w') as g:
    g.write(answer)
