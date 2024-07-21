class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        answer=[]
        heap=[]
        for i in range(k):
            heapq.heappush(heap , (-nums[i],i))
        answer.append(-heap[0][0])

        for i in range(k,n):
            heapq.heappush(heap , (-nums[i],i))
            while heap[0][1] <= i-k:
                heapq.heappop(heap)
            answer.append(-heap[0][0])
        return answer


        
