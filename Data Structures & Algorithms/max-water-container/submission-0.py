class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1

        val = 0

        while start<end:
            area = min(heights[start],heights[end])*(end-start)
            val = max(val,area)
            if heights[start] <= heights[end]:
                start+=1
            else:
                end-=1
        return val

        