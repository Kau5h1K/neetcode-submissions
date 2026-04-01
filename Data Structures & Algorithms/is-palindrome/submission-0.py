class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-z0-9]', '', s.lower())

        L, R = 0, len(cleaned_s) - 1
        while (L < R):
            if cleaned_s[L] != cleaned_s[R]:
                return False
            L += 1
            R -= 1
        return True
