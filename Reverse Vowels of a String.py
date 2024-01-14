class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        for char in s:
            if char in vowels:
                stack.append(char)

        output = ""
        for char in s:
            if char not in vowels:
                output += char
            else:
                output += stack.pop()
        return output