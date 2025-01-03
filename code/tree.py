'''
Completing a Tree
'''


from collections import deque

def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = [[0] * n for _ in range(n)]
        for line in f:
            a, b = map(int, line.strip().split())
            matrix[a-1][b-1] = 1
            matrix[b-1][a-1] = 1
    return n, matrix


def count_connected_components(n, matrix):
    visited = [False] * n
    component_count = 0

    for start_node in range(n):
        if visited[start_node]:
            continue
        
        component_count += 1
        queue = deque([start_node])
        visited[start_node] = True

        while queue:
            current = queue.popleft()
            for neighbor in range(n):
                if matrix[current][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    return component_count


def main():
    n, matrix = read_input("rosalind_tree.txt")
    components = count_connected_components(n, matrix)
    print(components - 1)


if __name__ == "__main__":
    main()
