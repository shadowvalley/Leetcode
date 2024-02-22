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


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parans = []
        self.genParans(n, parans, [], 0, 0)
        return parans
    
    def genParans(self, n: int, parans: List[int], store: List[str], oc: int, cc: int):
        if len(store) == 2*n:
            parans.append(''.join(store))
            return

        if oc < n:
            store.append("(")
            self.genParans(n, parans, store, oc+1, cc)
            store.pop()

        if cc < oc:
            store.append(")")
            self.genParans(n, parans, store, oc, cc+1)
            store.pop()
