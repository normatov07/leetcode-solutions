class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, k

        while right < len(arr):
            if abs(x-arr[left]) <= abs(x-arr[right]) and arr[left] != arr[right]:
                break
            
            left+=1
            right+=1

        return arr[left:right]