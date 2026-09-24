from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        states = [0] * numCourses
        neighbors = {}
        for a, b in prerequisites:
            if b not in neighbors:
                neighbors[b] = [a]
            else:
                neighbors[b].append(a)
        
        def is_possible(numCourses, prerequisites):
            def is_dag_from_node(node):
                if states[node] == 1:
                    return False
                elif states[node] == 2:
                    return True
                states[node] = 1
                if node in neighbors:
                    for neighbor in neighbors[node]:
                        if not is_dag_from_node(neighbor):
                            return False
                states[node] = 2
                return True

            for node in range(numCourses):
                if states[node] == 0:
                    if not is_dag_from_node(node):
                        return False
            return True
        
        if not is_possible(numCourses, prerequisites):
            return []

        out = deque()
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                if node in neighbors:
                    for neighbor in neighbors[node]:
                        dfs(neighbor)
                out.appendleft(node)

        for node in range(numCourses):
            dfs(node)
            
        return list(out)
        