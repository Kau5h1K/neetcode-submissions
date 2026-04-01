class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_amt = 0
        while L < R:
            min_height = min(heights[L], heights[R])
            amt = (R - L)*min_height
            max_amt = max(max_amt, amt)

            if heights[L] == min_height:
                L += 1
            else:
                R -= 1
            
        return max_amt