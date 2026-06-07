class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        left = 0
        maxlen = 1
        for right in range(1,len(s)+1):
            substring =  s[left:right]
            maxlen = max(maxlen,len(substring))
            print("len",maxlen, substring, left, right)
            if right < len(s):
                if s[right] in substring:
                    while s[right] in substring:
                        left+=1
                        substring = s[left:right]
            # print("last",substring[left:right], left,right)
        return maxlen



        