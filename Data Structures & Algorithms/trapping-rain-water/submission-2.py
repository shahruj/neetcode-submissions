class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        leftmax = height[left]
        rightmax = height[right]
        water = 0
        while left < right:
            # print(leftH,rightH,water, leftmax, rightmax)
            if leftmax > rightmax:
                print("movedright")
                right-=1
                rightmax = max(rightmax,height[right])
                water += rightmax-height[right]
            else:
                print("movedleft")
                left+=1
                leftmax = max(leftmax,height[left])
                water += leftmax-height[left]
        
        return water


            