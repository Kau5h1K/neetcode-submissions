class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []
        res = [0] * len(nums)

        total = 1
        for i in range(len(nums)):
            total = total * nums[i-1] if i > 0 else 1
            pref.append(total)

        total = 1
        for j in range(len(nums) - 1, -1, -1):
            total = total * nums[j+1] if j < (len(nums) - 1) else 1
            suff.append(total)

        suff = suff[::-1]
        print(pref)
        print(suff)

        for k in range(len(nums)):
            res[k] = pref[k] * suff[k]

        return res