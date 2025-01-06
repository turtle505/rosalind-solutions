'''
Ordering Strings of Varying Length Lexicographically
'''

def read_input(filename):
    alphabets = []
    nums = 0
    with open(filename) as f:
        alphabets = list(f.readline().strip().split(" "))
        nums = int(f.readline().strip())
            
    return nums, alphabets

n = 0        
arr = []
result = []

def solve(k, matrix):
    if k == n:
        result.append(arr[:])
        return
    
    for i in matrix:
        arr.append(i)
        if arr[:k] not in result: result.append(arr[:k])
        solve(k+1, matrix)
        arr.pop()
        
def make_solve(m):
    answer = ""
    for i in range(1, len(result)):
        answer += ''.join(map(str, result[i])) + '\n'
    with open("solve.txt", 'w') as g:
        g.write(answer)
        

def main():
    global n
    n, matrix = read_input("rosalind_lexv.txt")
    solve(0, matrix)
    make_solve(result)
    
        
if __name__ == "__main__":
    main()
