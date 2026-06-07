class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        comparison = {}
        count = {}
        if len(s1)>len(s2):
            return False
        for k in range(len(s1)):
            comparison[s1[k]] = comparison.get(s1[k],0)+1
            count[s2[k]] = count.get(s2[k],0)+1
        
        for right in range(len(s1),len(s2)+1):
            
            substring = s2[left:right]
            # print(s2[left],s2[right],substring, count)
            if len(substring) >= len(s1) and count == comparison:
                return True
            else:
                count[s2[left]]-=1
                if count[s2[left]] == 0:
                    del count[s2[left]]
                left+=1
            if right<=len(s2)-1:
                count[s2[right]] = count.get(s2[right],0)+1


        return False

        