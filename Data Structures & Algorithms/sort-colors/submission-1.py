class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums)-1
        cursor = 0
        
        while cursor <= right:
            
            if nums[cursor] == 0:
                while left < cursor and nums[left] == 0:
                    left+=1
                nums[left], nums[cursor] = nums[cursor], nums[left]
                left+=1
            elif nums[cursor] == 2:
                while right > cursor and nums[right] == 2:
                    right-=1
                nums[right], nums[cursor] = nums[cursor], nums[right]
                right-=1
                continue
            
            cursor+=1
