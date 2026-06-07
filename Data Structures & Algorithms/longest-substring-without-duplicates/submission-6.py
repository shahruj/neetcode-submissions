class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in win:
                win.remove(s[left])
                left += 1
            
            win.add(s[right])
            maxlen = max(maxlen, right - left + 1)

        return maxlen
        
        # left = 0
        # maxlen = 1
        # for right in range(1,len(s)+1):
        #     substring =  s[left:right]
        #     maxlen = max(maxlen,len(substring))
        #     print("len",maxlen, substring, left, right)
        #     if right < len(s):
        #         if s[right] in substring:
        #             while s[right] in substring:
        #                 left+=1
        #                 substring = s[left:right]
        # return maxlen






        