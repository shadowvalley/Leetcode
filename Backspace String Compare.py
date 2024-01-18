class Solution:
    def create_stack(self, s: str, stack: List[str]):
        for char in s:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()
   
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        self.create_stack(s, stack_s)
        self.create_stack(t, stack_t)

        s_string = ''.join(stack_s)
        t_string = ''.join(stack_t)
        
        return s_string == t_string