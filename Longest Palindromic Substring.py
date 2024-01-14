class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length palindrome
            l,r = i, i

            # Check if this substring is a palindrome
            while l>=0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
                
            # even length palindrome
            l,r = i, i+1

            # Check if this substring is a palindrome
            while l>=0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
                