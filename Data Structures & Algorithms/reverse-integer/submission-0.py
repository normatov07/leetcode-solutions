class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_minus = x < 0
        x = abs(x)

        while x > 0:
            res = (res * 10) + (x % 10)
            x = x // 10 

        if res > 2147483648 or (res == 2147483648 and is_minus):
            return 0
            

        return res if not is_minus else -res