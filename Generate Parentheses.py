class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate(0, 0, "", result, n)

        return result

    def generate(self, oc: int, cc: int, ds: str, ans:List[str], n: int):
        if len(ds) == n*2:
            ans.append(ds)
            return 

        if oc < n:
            self.generate(oc+1, cc, ds+"(", ans, n)
        
        if cc < oc:
            self.generate(oc, cc+1, ds+")", ans, n)