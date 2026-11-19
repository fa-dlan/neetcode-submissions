from _heapq import heappop
import heapq

class MedianFinder:
    # 2 scenario
    # bigger than smallest right, and else
    # if len left == len right - 1 shift left
    # if len left == len right + 2 shift right
    # if odd: left[0]
    # if even: (left[0] + right[0]) / 2

    def __init__(self):
       self.left = []
       self.right = []
       self.median = 0

    def addNum(self, num: int) -> None:
        # insert num
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush_max(self.left, num)
        
        # adjust pq lengths
        # transfer to left
        if len(self.left) == len(self.right) - 1:
            heapq.heappush_max(self.left,
                heapq.heappop(self.right)
            )
        # transfer to right
        elif len(self.left) == len(self.right) + 2:
            heapq.heappush(self.right,
                heapq.heappop_max(self.left)
            )
        
        # if even:
        if len(self.left) == len(self.right):
            self.median = (self.left[0] + self.right[0]) / 2
        # if odd:
        else:
            self.median = self.left[0]
        # print(num, self.left, self.right, self.median)


    def findMedian(self) -> float:
        return self.median