class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_list = []
        for num in nums_set:
            if num-1 not in nums_set:
                start_list.append(num)
        max_count = 0
        for num in start_list:
            count = 1
            num += 1
            while num in nums_set:
                count += 1
                num += 1
            max_count = max(max_count, count)
        
        return max_count