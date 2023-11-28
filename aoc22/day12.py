with open("in.txt") as f:
    data = f.read().strip()
lines = data.split("\n")
lines = [[x for x in line] for line in lines]

from collections import deque

starts = []  # possible start points for P2
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            S = (i, j)
            lines[i][j] = "a"
            starts.append((i, j))
        elif lines[i][j] == "E":
            lines[i][j] = "z"
            end = (i, j)
        elif lines[i][j] == "a":
            starts.append((i, j))


def solution(graph, start, end, P2=False):
    if start == end:
        return 0
    node = start
    q = deque()
    v = []
    q.append([node, 0])
    v.append(node)
    if P2:  # clever way
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if graph[i][j] == "a":
                    q.append([(i, j), 0])
    while q:
        (i, j), dist = q.popleft()
        for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            newI = i + d[0]
            newJ = j + d[1]
            if 0 <= newI < len(graph) and 0 <= newJ < len(graph[newI]):
                if P2 and graph[newI][newJ] == "a":
                    # if a is needed for shortest path then it would be better to start at this a, so continue
                    continue
                if (newI, newJ) in v:
                    continue
                if ord(graph[newI][newJ]) <= ord(graph[i][j]) + 1:
                    if (newI, newJ) == end:
                        return dist + 1
                    q.append([(newI, newJ), dist + 1])
                    v.append((newI, newJ))
    return 100000


print("P1", solution(lines, S, end))

# print("P2", min(solution(lines, s, end, True) for s in starts))
print("P2", solution(lines, S, end, True))
