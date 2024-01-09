class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        states = [0]*26

        for char in s:
            states[ord(char) - ord('a')] += 1

        for char in t:
            states[ord(char) - ord('a')] -= 1
            if states[ord(char) - ord('a')] < 0:
                return False

        return False if any(value != 0 for value in states) else True
        