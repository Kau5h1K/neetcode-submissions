class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 52
            for c in s:
                if 'a' <= c <= 'z':
                    count[ord(c) - ord('a')] += 1
                elif 'A' <= c <= 'Z':
                    count[26 + ord(c) - ord('A')] += 1
            res[tuple(count)].append(s)
        return list(res.values())