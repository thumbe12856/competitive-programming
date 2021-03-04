class Solution:
    def stoneGameIII(self, A):
        dp = [0] * (len(A) + 4)
        for i in range(len(A) - 1, -1, -1):
            dp[i] = max(sum(A[i: i + k]) - dp[(i + k)] for k in (1, 2, 3))
            print(dp)
        if dp[0] < 0:
            return "Bob"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Tie"


s = Solution()
# print(s.stoneGameIII([1,2,3,7]))
# print(s.stoneGameIII([1,2,3,-9]))
# print(s.stoneGameIII([1,2,3,6]))
# print(s.stoneGameIII([1,2,3,-1,-2,-3,7]))
print(s.stoneGameIII([-1,-2,-3]))
