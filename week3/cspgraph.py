def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve(v, graph, m, color):
    if v == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            if solve(v + 1, graph, m, color):
                return True
            color[v] = 0
    return False

n = int(input("enter the number of edges"))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("enter the number of colours"))
color = [0] * n

if solve(0, graph, m, color):
    for i in range(n):
        print(color[i], end=" ")
else:
    print("No solution")
