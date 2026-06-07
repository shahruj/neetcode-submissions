# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         mapping = {}

#         for k in range(0,len(strs)):
#             sorted_s = "".join(sorted(strs[k]))
#             if sorted_s not in mapping:
#                 mapping[sorted_s] = []
#             mapping[sorted_s].append(k)
        
#         output = []
#         for map in mapping:
#             result = [strs[i] for i in mapping[map]]
#             output.append(result)
        
#         return output


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            mapping[tuple(count)].append(s)

        return list(mapping.values())