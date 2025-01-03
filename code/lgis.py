'''
Longest Increasing Subsequence
'''

n = 0
arr = []
matrix1 = []
matrix2 = []
answer = ""

def increase(k):
    for _ in range(k):
        matrix1.append(1)
    
    max_length = 0
    
    for i in range(k):
        for j in range(i):
            if (arr[j] < arr[i]): 
                matrix1[i] = max(matrix1[j]+1, matrix1[i])
                if max_length < matrix1[i]: max_length = matrix1[i]
    nums = []
    for i in range(k):
        if matrix1[k-1-i] == max_length:
            nums.append(arr[k-1-i])
            max_length -= 1
            
    nums = nums[::-1]
    global answer
    answer += ' '.join(map(str, nums))
            
        
def decrease(k):
    for _ in range(k):
        matrix2.append(1)
    
    max_length = 0
    
    for i in range(k):
        for j in range(i):
            if (arr[j] > arr[i]): matrix2[i] = max(matrix2[j]+1, matrix2[i])
            if max_length < matrix2[i]: max_length = matrix2[i]
            
    nums = []
    for i in range(k):
        if matrix2[k-1-i] == max_length:
            nums.append(arr[k-1-i])
            max_length -= 1
            
    nums = nums[::-1]
    global answer
    answer += ' '.join(map(str, nums))
            
def solve(k):
    increase(k)
    global answer
    answer += '\n'
    decrease(k)


with open("rosalind_lgis.txt") as f:
    n = int(f.readline())
    X = f.readline().split(" ")
    arr = list(map(int, X))
    solve(n)

with open("solve.txt", 'w') as g:
    g.write(answer)
