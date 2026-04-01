class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        sorted_counts = sorted(counts, key = lambda x: counts[x], reverse = True)
        return sorted_counts[:k]