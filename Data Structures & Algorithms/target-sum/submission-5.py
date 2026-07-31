class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dict = defaultdict(int)
            for index, count in dp.items():
                next_dict[index+num] += count
                next_dict[index-num] += count
            dp = next_dict
        
        return dp[target] if target in dp else 0