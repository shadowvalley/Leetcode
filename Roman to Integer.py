class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {}
        dict['I'] = 1
        dict['V'] = 5
        dict['X'] = 10
        dict['L'] = 50
        dict['C'] = 100
        dict['D'] = 500
        dict['M'] = 1000

        intRepre = dict[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if dict[s[i]] < dict[s[i+1]]:
                intRepre -= dict[s[i]]
            else:
                intRepre += dict[s[i]]
            
        return intRepre
