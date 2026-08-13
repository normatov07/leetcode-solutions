class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counter = [0] * 58
        currCount = [0] * 58
        totalCount = 0
        tset = set(t)

        for ch in t:
            totalCount += 1
            counter[ord(ch) - ord('A')] += 1

        minLeft, minRight = 0, len(s)+1
        left, right = 0, 0

        
        while right < len(s):
            currCount[ord(s[right]) - ord('A')] += 1
            # print(left,right, currCount[ord(s[left]) - ord('A')], counter[ord(s[left]) - ord('A')], s[left])
            while left <= right and (currCount[ord(s[left]) - ord('A')] > counter[ord(s[left]) - ord('A')]):
                currCount[ord(s[left]) - ord('A')] -= 1
                left+=1
                
            if right-left < minRight-minLeft and self.isComplete(currCount, counter, tset):
                minLeft, minRight = left, right
                currCount[ord(s[left]) - ord('A')] -= 1
                left+=1

            right+=1
        
        return s[minLeft:minRight+1] if minRight < len(s)+1 else ""
    
    def isComplete(self, currCount, counter, tset):

        for ch in tset:
            if currCount[ord(ch) - ord('A')] < counter[ord(ch) - ord('A')]:
                return False
        
        return True

                

