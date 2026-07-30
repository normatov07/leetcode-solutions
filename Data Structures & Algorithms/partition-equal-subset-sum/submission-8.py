class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        dp = [[False] * (target+1) for i in range(len(nums))]
        dp[0][0] = True

        for i in range(1, len(nums)):
            for t in range(target+1):
                if t >= nums[i]:
                    dp[i][t] =  dp[i-1][t] or dp[i-1][t-nums[i]]
                else:
                    dp[i][t] =  dp[i-1][t]

        # print(dp)
        return dp[-1][-1]
