'''
Counting Subsets
'''

def main():
    n = 0
    with open("rosalind_sset.txt", 'r') as f:
        n = int(f.readline().strip())
    result = (2 ** n) % 1000000
    with open("solve.txt", 'w') as g:
        g.write(str(result))    
        
if __name__ == "__main__":
    main()
