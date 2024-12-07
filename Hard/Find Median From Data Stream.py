import heapq

class MedianFinder:

    def __init__(self):
       
        self.lower_half = []  
        self.upper_half = []  

    def addNum(self, num: int) -> None:
        
        if not self.lower_half or num < -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def findMedian(self) -> float:
        
        if len(self.lower_half) == len(self.upper_half):
            return (-self.lower_half[0] + self.upper_half[0]) / 2.0
        elif len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        else:
            return self.upper_half[0]
