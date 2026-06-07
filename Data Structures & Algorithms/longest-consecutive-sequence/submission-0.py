class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for i in range(0,len(nums)):
            if nums[i]-1 not in num_set:
                val = nums[i]
                length = 1
                while val+1 in num_set:
                    length+=1
                    val+=1

                longest = max(length,longest)
        
        return longest

            








        