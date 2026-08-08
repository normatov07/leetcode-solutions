class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        res = 0
        for i in range(32):
            bin_left = (left >> i) & 1
            if bin_left != 1:
                continue

            remain = left % (1 << (i+1))
            diff = (1 << (i+1)) - remain
            if right - left < diff:
                res |= (1 << i)

        return res

