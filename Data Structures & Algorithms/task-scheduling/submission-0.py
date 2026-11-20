import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1
        freq = list(freq_map.values())
        heapq.heapify_max(freq)
        cooldown = deque()
        
        t = 0
        while freq or cooldown:
            if cooldown and cooldown[0][0] == t:
                heapq.heappush_max(freq, cooldown.popleft()[1])
            highest_freq = 0
            if freq:
                highest_freq = heapq.heappop_max(freq)
                highest_freq -= 1
            if highest_freq:
                cooldown.append((t + n + 1, highest_freq))

            t += 1
        return t
