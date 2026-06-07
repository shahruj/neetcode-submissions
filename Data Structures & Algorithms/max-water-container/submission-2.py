class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        maxVol = -1
        while left<right:
            vol = calVol(left,right,heights)
            maxVol = max(maxVol,vol)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        
            
        return maxVol

def calVol(left,right,heights):
    return min(heights[left],heights[right])*(right-left)