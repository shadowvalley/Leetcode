class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = []
        if not digits:
            return store 

        self.number_to_letter_mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        store = []
        self.backtrack(digits, 0, store, [])
        return store 

    def backtrack(self, digits, cur_idx, store, dummy):
        # when to break recursion
        if cur_idx == len(digits):
            store.append(''.join(dummy))
            return 
        
        for char in self.number_to_letter_mappings[digits[cur_idx]]:
            dummy.append(char)
            self.backtrack(digits, cur_idx+1, store, dummy)
            dummy.pop()
        
