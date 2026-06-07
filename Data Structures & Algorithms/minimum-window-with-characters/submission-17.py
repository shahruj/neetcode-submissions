class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        have = {}
        if s == t:
            return t
        if len(t)>len(s):
            return ""

        for i in range(len(t)):
            need[t[i]] = need.get(t[i],0)+1

        left = 0
        required =  len(need)
        formed = 0
        minimum_val = float("inf")
        minimum = ""
        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c,0)+1

            if c in need and have[c] == need[c]:
                formed+=1
            
            while formed == required:
                if minimum_val>len(s[left:right+1]):
                    minimum_val, minimum = len(s[left:right+1]),s[left:right+1]

                have[s[left]]-=1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed-=1
                left +=1    



        if minimum_val ==  float("inf"):
            return ""

        return minimum
