from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        
       
        l_max, r_max = 0, 0
        
       
        trapped_water = 0
        
        
        while l <= r:
            
            if r_max <= l_max:
                
                trapped_water += max(0, r_max - height[r])
                
                r_max = max(r_max, height[r])
                
                r -= 1
            else:
               
                trapped_water += max(0, l_max - height[l])
               
                l_max = max(l_max, height[l])
                
                l += 1
        
        return trapped_water
