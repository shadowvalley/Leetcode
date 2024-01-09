class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        maxLength = 0

        r = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxLength = max(maxLength, r-l+1)
            r+=1
        return maxLength
