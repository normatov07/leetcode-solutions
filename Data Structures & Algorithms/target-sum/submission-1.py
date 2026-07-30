class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        # dp = defaultdict(set)

        def backtracking(i, current_sum):
            
            nonlocal count
            
            if i >= len(nums):
                count+= target==current_sum
                return

            # if current_sum in dp[i]:
            #     return
            
            # dp[i].add(current_sum)

            backtracking(i+1, current_sum+nums[i])
            backtracking(i+1, current_sum-nums[i])
        
        backtracking(0,0)

        return count