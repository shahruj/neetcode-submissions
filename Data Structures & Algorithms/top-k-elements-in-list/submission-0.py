class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        sorted_items = [k for k, v in sorted(freq.items(), key=lambda x: x[1])]
        return (sorted_items[-k:])

        