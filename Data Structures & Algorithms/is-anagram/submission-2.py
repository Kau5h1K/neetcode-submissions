class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}
        for i in s:
            if i in s_counter.keys():
                s_counter[i] += 1
            else:
                s_counter[i] = 1

        for j in t:
            if j in t_counter.keys():
                t_counter[j] += 1
            else:
                t_counter[j] = 1

        if set(s_counter.keys()) == set(t_counter.keys()):
            for i in s_counter.keys():
                if s_counter[i] == t_counter[i]:
                    return True
                else:
                    return False
        else:
            return False