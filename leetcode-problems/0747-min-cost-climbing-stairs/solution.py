class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #[x] ways: x --> top, top
        #[x,y] ways: x --> top, y --> top, x --> y --> top | 3
        #[x,y,z] ways: x --> z --> top, x --> y --> z --> top, y --> z --> top, y --> top
        dp = [0] * len(cost)
        
        n = len(cost)
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        for i in range(n-2):
            dp[n-3-i] = cost[n-3-i] + min(dp[n-2-i], dp[n-1-i])
        return(min(dp[0], dp[1]))
