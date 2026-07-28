class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        dp = defaultdict(set)

        if totalSum % 2:
            return False
        
        target = totalSum / 2

        def backtracking(i, currentSum):
            if 0 == currentSum:
                return True
            
            if i >= len(nums):
                return False

            if currentSum in dp[i]:
                return False

            dp[i].add(currentSum)

            return backtracking(i+1, currentSum-nums[i]) or backtracking(i+1, currentSum)
        

        return backtracking(0, target)
