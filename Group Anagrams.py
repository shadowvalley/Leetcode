class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for word in strs:
            sorted_chars = sorted(word)
            sorted_word = ''.join(sorted_chars)
            if sorted_word not in store:
                store[sorted_word] = [word]
            else:
                store[sorted_word].append(word)
        
        return store.values()
