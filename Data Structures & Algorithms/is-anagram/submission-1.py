class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            smap[s[i]] = smap.get(s[i],0)+1
            tmap[t[i]] = tmap.get(t[i],0)+1
        
        if smap == tmap:
            return True
        else:
            return False

            
