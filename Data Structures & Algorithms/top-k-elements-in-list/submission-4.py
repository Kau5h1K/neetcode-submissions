class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        
        freqToNum = [[] for _ in range(len(nums) + 1)]
        for num, freq in numToFreq.items():
            freqToNum[freq].append(num)

        res = []
        for i in range(len(freqToNum) - 1, 0, -1):
            for j in freqToNum[i]:
                res.append(j)
                if len(res) == k:
                    return res