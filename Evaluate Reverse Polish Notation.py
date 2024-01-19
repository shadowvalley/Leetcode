class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                second_ele = int(stack.pop())
                first_ele = int(stack.pop())

                if token == "+":
                    ans = first_ele + second_ele
                elif token == "-":
                    ans = first_ele - second_ele
                elif token == "*":
                    ans = first_ele * second_ele
                elif token == "/":
                    ans = first_ele / second_ele
                
                stack.append(ans)
        
        return int(stack.pop())
