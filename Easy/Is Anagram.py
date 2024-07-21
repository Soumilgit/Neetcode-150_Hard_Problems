class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sos=sorted(s)
        sot=sorted(t)
        return sos == sot
        
        
