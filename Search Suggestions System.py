class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Step - 1 -> Sort the products list to bring all the words with the same prefix together
        products.sort()

        # Step - 2 -> Use 2 pointers to figure out the valid range
        l, r = 0, len(products) - 1

        result = []

        for i in range(len(searchWord)):
            char = searchWord[i]

            # Check if l and right are valid
            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1

            suggestedProducts = []
            remainingProductsLength = r - l + 1

            for j in range(min(remainingProductsLength, 3)):
                suggestedProducts.append(products[l + j])

            result.append(suggestedProducts)

        return result
