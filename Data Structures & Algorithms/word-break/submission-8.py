class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return 1
            
            if dp[i] >= 0:
                return dp[i]

            for w in wordDict:
                if len(w)+i <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dfs(i+len(w))
                    if dp[i] == 1:
                        return 1

            return 0

        return bool(dfs(0))

            
