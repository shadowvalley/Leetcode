class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find the shortest string
        sorted_strs = sorted(strs, key = len)
        shortest_string = sorted_strs[0]
        
        lcp_found = True
        lcp = ""
        for i,char in enumerate(shortest_string):
            alphabet = shortest_string[i]
            for j in range(1, len(sorted_strs)):
                if sorted_strs[j][i] != alphabet:
                    lcp_found = False
            
            if lcp_found:
                lcp += alphabet
        return lcp
        