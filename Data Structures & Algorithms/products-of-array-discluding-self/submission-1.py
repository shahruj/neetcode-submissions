class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_of_zeros = 0
        for num in nums:
            if num == 0:
                num_of_zeros+=1
                if num_of_zeros>1:
                    return [0]*len(nums)
            else:
                prod = prod*num
        
        res = []
        for num in nums:
            if num != 0 and num_of_zeros==1:
                res.append(0)
            elif num == 0:
                res.append(prod)
            else:
                res.append(prod//num)



        return res

        