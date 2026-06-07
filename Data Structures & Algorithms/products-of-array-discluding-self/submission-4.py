class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        leftps = [1]*len(nums)
        rightps = [1]*len(nums)

        leftp = 1
        for i in range(len(nums)):
            leftp*=nums[i]
            leftps[i]=leftp
        
        rightp = 1
        for i in range(len(nums)-1,-1,-1):
            rightp*=nums[i]
            rightps[i]=rightp   

        res = []
        for k in range(len(nums)):
            prod = 1
            if k>0:
                prod*=leftps[k-1]
            
            if k<len(nums)-1:
                prod*=rightps[k+1]

            res.append(prod)
                
        return res
        # prod = 1
        # num_of_zeros = 0
        # for num in nums:
        #     if num == 0:
        #         num_of_zeros+=1
        #         if num_of_zeros>1:
        #             return [0]*len(nums)
        #     else:
        #         prod = prod*num
        
        # res = []
        # for num in nums:
        #     if num != 0 and num_of_zeros==1:
        #         res.append(0)
        #     elif num == 0:
        #         res.append(prod)
        #     else:
        #         res.append(prod//num)

        # return res

        