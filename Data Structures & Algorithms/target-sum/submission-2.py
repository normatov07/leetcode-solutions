class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtracking(i, current_sum):
            
            if i >= len(nums):
                return int(target==current_sum)

            if (i, current_sum) in dp:
                return dp[(i, current_sum)]

            dp[(i, current_sum)] = backtracking(i+1, current_sum+nums[i]) + backtracking(i+1, current_sum-nums[i])

            return dp[(i, current_sum)]

        return backtracking(0,0)