class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = True
        left, right = 0, len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif res:
                l, r = left+1, right
                while l < r:
                    if s[l] != s[r]:
                        res = False
                        break
                    l += 1
                    r -=1

                if res == True:
                    return res

                right -= 1
            else:
                return False
               
        return True
            
           