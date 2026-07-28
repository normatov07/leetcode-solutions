class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
       
        def backtracking(i, currentSum):
            if i >= len(nums):
                return False

            if currentSum == (totalSum-currentSum):
                return True
            

            return backtracking(i+1, currentSum+nums[i]) or backtracking(i+1, currentSum)
        

        return backtracking(0, 0)
