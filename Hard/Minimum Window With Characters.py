class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        char_map_t = {}
        for char in t:
            if char in char_map_t:
                char_map_t[char] += 1
            else:
                char_map_t[char] = 1

        
        left = 0
        min_length = float('inf')
        min_window = ""
        char_map_s = {}

        for right in range(len(s)):
            char_map_s[s[right]] = char_map_s.get(s[right], 0) + 1

            
            while all([char in char_map_s and char_map_s[char] >= count for char, count in char_map_t.items()]):
               
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]

                
                char_map_s[s[left]] -= 1
                left += 1

        return min_window
