class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            
            for j in range (i+1,n):
                if nums[i]==nums[j]:
                    return True
        return False
         
