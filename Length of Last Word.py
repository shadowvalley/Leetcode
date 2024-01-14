class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      sanitised_string = s.strip()
      return len(sanitised_string.split()[-1])