class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dp(i, j):
            # If already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern finished
            if j == len(p):
                return i == len(s)

            # Check current match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' (look ahead)
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two choices:
                # 1. Skip "x*" → dp(i, j+2)
                # 2. Use it (if match) → dp(i+1, j)
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)