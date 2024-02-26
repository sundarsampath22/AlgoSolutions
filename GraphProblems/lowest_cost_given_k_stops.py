from collections import defaultdict

#Given an array of flights (such that flights[0][0] represents the inbound vertex, flights[0][1] represents the outbound vertex, and flights[0][1] represents the cost of the edge)
#Find the cheapest path between the src vertex and the destination vertex (if no such path exists return -1) 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Construct graph using adjacency list
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        # Initialize memoization dictionary to track minimum cost to reach each node
        memo = {}

        # Perform DFS with memoization and cycle detection
        def dfs(node, stops):
            # Base case: we've reached the destination
            if node == dst:
                return 0

            # Check if we've already computed the minimum cost for this node within the given number of stops
            if (node, stops) in memo:
                return memo[(node, stops)]

            # If we exceed the number of stops allowed, return infinity
            if stops < 0:
                return float('inf')

            # Explore neighbors and compute the minimum cost
            min_cost = float('inf')
            for neighbor, cost in graph[node]:
                min_cost = min(min_cost, cost + dfs(neighbor, stops - 1))

            # Memoize the result
            memo[(node, stops)] = min_cost

            return min_cost

        # Find the minimum cost using DFS
        min_cost = dfs(src, k)

        return min_cost if min_cost != float('inf') else -1