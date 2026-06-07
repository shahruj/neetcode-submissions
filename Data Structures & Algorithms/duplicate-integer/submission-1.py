# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         mapping = {}
#         for num in nums:
#             mapping[num]=mapping.get(num,0)+1
#             if mapping[num]>1:
#                 return True
#         return False























class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        includes = set()

        for n in nums:
            if n in includes:
                return True
            includes.add(n)
        
        return False

























