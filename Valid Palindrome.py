class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitised_string = s.strip()
        fresh = ""
        for char in s:
            if char.isalnum():
                fresh += char.lower()

        return fresh == fresh[::-1]