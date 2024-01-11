class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            rev = rev*10 + x % 10
            x //= 10
         
        if x == rev//10 or x == rev:
            return True
        return False