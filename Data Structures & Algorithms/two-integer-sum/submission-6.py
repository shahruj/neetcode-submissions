class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(0,len(nums)):
            value = nums[i]
            if (target - value) in seen:
                return [seen[target-value],i]
            
            seen[value] = i       

        return []