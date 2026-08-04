class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0

        for i in nums:
            if (i-1) not in nums:
                length = 1
                while(i+length) in nums:
                    length +=1 
                max_count = max(max_count, length)
        return max_count
                
