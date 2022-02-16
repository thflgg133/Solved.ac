import sys
import heapq
INF = sys.maxsize

def dijkstar(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)
        
        if distance[now] < cost:
            continue
        
        for next_node, weight in graph[now]:
            next_cost = cost + weight
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost     
                heapq.heappush(heap, (next_cost, next_node))        


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1) 

for _ in range(M):
    c1, c2, cost = map(int, sys.stdin.readline().split())
    graph[c1].append((c2, cost))    

start, end = map(int, sys.stdin.readline().split())

dijkstar(start)

print(distance[end])