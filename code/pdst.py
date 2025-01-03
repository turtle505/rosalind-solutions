```
Creating a Distance Matrix
```

def read_input(filename):
    dna = []
    with open(filename) as f:
        line = f.readline()
        while True:
            dna_string = ""
            while True:
                line = f.readline()
                if not line: break
                if line[0] == '>': break
                dna_string += line.strip()
            dna.append(dna_string)
            if not line: break
            
    return len(dna), dna
        
def distance_matrix(n, matrix):
    dist = [[0]*n for _ in range(n)]
    length = len(matrix[0])

    for i in range(n):
        for j in range(n):
            if i == j: continue
            w = 0
            for k in range(length):
                if matrix[i][k] != matrix[j][k]:
                    w += 1
            dist[i][j] = w / length
            
    return dist

def make_solve(m):
    answer = ""
    for i in range(len(m)):
        answer += ' '.join(map(str, m[i])) + '\n'
    with open("solve.txt", 'w') as g:
        g.write(answer)
        

def main():
    n, matrix = read_input("rosalind_pdst.txt")
    dist = distance_matrix(n, matrix)
    make_solve(dist)
    
    
if __name__ == "__main__":
    main()
