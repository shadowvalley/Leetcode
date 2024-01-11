class Solution:
    def reverse(self, x: int) -> int:
        max = 2**31-1
        min = -1*2**31

        # get sign
        sign = True
        if x < 0:
            sign = False
            x = abs(x)
        reversed = 0
        while x > 0:
            reversed = reversed * 10 + x%10

            if reversed < min or reversed > max:
                return 0
            x //= 10

        return -reversed if sign == False else reversed
