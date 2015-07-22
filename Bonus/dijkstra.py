# Finish PriorityQueueMap:
# insert(key, val, priority)
    # duplicates update the priority if the priority is less
# shift should give key, val, priority


# Lock in based on shortcuts.

def dijkstra(source):
    results = {}
    frontier = PriorityQueueMap()

    frontier.insert(source, None, 0)
    while len(frontier) > 0:
        v, e, c = frontier.shift() # based on priority queue
        result[v] = [e, c]
        for e2 in v.out_edges():
            v2 = e2.to_vertex
            c2 = c + e2.cost
            frontier.insert(v2, e2, c2)


results looks like this:

results = {
    "A": [None, 0],
    "C": [e2, 2],
    "B": [e4, 4],
    "D": [e3, 6],
    "E": [e7, 9]}
