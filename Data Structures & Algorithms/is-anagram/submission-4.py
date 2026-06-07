# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        # smap = {}
        # tmap = {}
        # if len(s)!=len(t):
        #     return False
        # for i in range(0,len(s)):
        #     smap[s[i]] = smap.get(s[i],0)+1
        #     tmap[t[i]] = tmap.get(t[i],0)+1
        
        # if smap == tmap:
        #     return True
        # else:
        #     return False

            


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for c in s:
            s_map[c] = s_map.get(c,0)+1
        
        for c in t:
            t_map[c] = t_map.get(c,0)+1
            if t_map[c] > s_map.get(c,float('inf')):
                return False

        if s_map == t_map:
            return True
        else:
            return False

























