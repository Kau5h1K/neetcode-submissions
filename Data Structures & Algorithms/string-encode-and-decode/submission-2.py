# My Solution

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sep = "<SEP>"
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        
        encoded_str_sizes = ",".join(sizes)
        encoded_str_values = "".join(strs)
        return encoded_str_sizes + sep + encoded_str_values


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sep = "<SEP>"
        decoded_str_sizes = s.split(sep)[0]
        decoded_str_values = s.split(sep)[1]

        decoded_strs = []
        index = 0
        for size in decoded_str_sizes.split(','):
            decoded_strs.append(decoded_str_values[index: index + int(size)])
            index = index + int(size)
        return decoded_strs
