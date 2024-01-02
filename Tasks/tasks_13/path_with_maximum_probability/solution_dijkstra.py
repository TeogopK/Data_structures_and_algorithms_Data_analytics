from heapq import heappop, heappush
    
class Solution:
    def dijkstra(self, start, end, V, graph,):
        distances = [0] * V
        distances[start] = 1
        
        pq = [(-1, start)]
        
        while pq:
            total_weight, current = heappop(pq)
            total_weight = -total_weight
                        
            if current == end:
                return distances[end]

            for neighb, added_weight in graph[current]:
                new_weight = total_weight * added_weight
                
                if new_weight > distances[neighb]:
                    distances[neighb] = new_weight
                    heappush(pq, (-new_weight, neighb))
        
        return 0

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {v: set() for v in range(n)}
        
        for i, path in enumerate(edges):
            x, y = path
            w = succProb[i]
            graph[x].add((y, w))
            graph[y].add((x, w))

        return self.dijkstra(start_node, end_node, n, graph)
