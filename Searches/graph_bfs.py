from collections import deque
def bfs(source, max_distance):
    queue = deque([[source, 0]])
    result = []

    while len(queue) > 0:
        vertex, distance = queue.popleft()
        result.append(vertex)
        for e in vertex.out_edges:
            if e.to_vertex not in seen:
                queue.append([e.to_vertex, distance + 1])
            seen[e.to_vertex] = True

    # to return counts we can use another loop to check distance and increment another value.
    return result

# O(|v| + |e|) determine time complexity based on vertices and edges
