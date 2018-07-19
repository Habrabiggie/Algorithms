"""
Which cells should the horse go through, to get from d4 to f2 most quickly?

1) We reduce the problem to the graph
2) We go around the width from one point to another

"""

letter = 'abcdefgh'
numbers = '12345678'

graph = dict()
for l in letter:
    for n in numbers:
        graph[l + n] = set()

def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)

for i in range(8):
    for j in range(8):
        v1 = letter[i] + numbers[j]
        v2 = ''
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letter[i + 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letter[i - 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letter[i + 1] + numbers[j + 2]
            add_edge(v1, v2)

        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letter[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

from collections import deque
distances = {v: None for v in graph}
parents = {v: None for v in graph}

start_vertex = 'd4'
end_vertex = 'f7'

distances[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if  distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]
    print('Shortest way: ', path[:: - 1])