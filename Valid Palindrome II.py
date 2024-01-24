class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(f"{s}")

        if s == s[::-1]:
            return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                # Check if removing s[l] or s[r] makes the remaining string a palindrome
                rem_string_left = s[:l] + s[l + 1:]
                rem_string_right = s[:r] + s[r + 1:]

                # since atmmost 1 deletion is allowed
                return self.isPalindrome(rem_string_left) or self.isPalindrome(rem_string_right)
            l += 1
            r -= 1
        return True
            