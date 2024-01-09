class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 !=0 :
            return False

        paranMapper = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for char in s:
            if char == '(' or char == "[" or char == "{":
                stack.append(char)
            else:
                if stack and stack[-1] == paranMapper[char]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False