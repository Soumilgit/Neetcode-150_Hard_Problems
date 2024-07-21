class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        heights.append(0)
        stack = [-1]

        jawab = 0
        for i in range(n+1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                
                jawab = max(jawab, h * w)
            stack.append(i)
        heights.pop()
        return jawab

        
