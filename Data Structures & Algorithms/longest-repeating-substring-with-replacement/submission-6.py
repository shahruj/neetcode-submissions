class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 

        count =  {}
        maxfreq = 0

        res = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            maxfreq = max(maxfreq,count[s[right]])
            while (right-left)+1 - maxfreq > k:
                count[s[left]]-=1
                left+=1
            
            res = max(res,right-left+1)


        return res