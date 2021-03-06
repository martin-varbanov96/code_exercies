
N, M, X, Y = tuple(map(int, input().split(" ")))

current_time = 0
costs = {i : 9999 for i in range(1, N+1)}
costs[X] = 0
parents = {}

city_map = {i : {} for i in range(1, N+1)}
for j in range(M):
    A, B, T, K = tuple(map(int, input().split(" ")))
    city_map[A][B] = (T, K)
    city_map[B][A] = (T, K)
print(city_map)



def search(source, target, graph, costs, parents):
    nextNode = source
    while(nextNode != target):
        for neighbor in graph[nextNode]:
            next_train_in = costs[nextNode] % graph[nextNode][neighbor][1]
            time_to_neighbor = graph[nextNode][neighbor][0] + next_train_in + costs[nextNode]
            if time_to_neighbor < costs[neighbor]:
                costs[neighbor] = time_to_neighbor
                parents[neighbor] = nextNode
            del graph[neighbor][nextNode]

        del costs[nextNode]
        nextNode = min(costs, key=costs.get)
        
    return parents



def backpedal(source, target, searchResult):
    node = target
    
    backpath = [target]
    
    path = []
    
    while node != source:
        
        backpath.append(searchResult[node])
        
        node = searchResult[node]
        
    for i in range(len(backpath)):
        
        path.append(backpath[-i - 1])
        
    return path

result = search(X, Y, city_map, costs, parents)

# print('parent dictionary={}'.format(result))

size = sum(backpedal(X, Y, result))
if(size <= 0):
    print("-1")
else:
    print(size)