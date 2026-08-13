class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counter = [0] * 58
        curr_count = [0] * 58
        tset = set(t)

        for ch in t:
            counter[ord(ch) - ord('A')] += 1

        min_left, min_right = 0, len(s)+1
        left, right = 0, 0
        
        while right < len(s):
            curr_count[ord(s[right]) - ord('A')] += 1

            while left <= right and (curr_count[ord(s[left]) - ord('A')] > counter[ord(s[left]) - ord('A')]):
                curr_count[ord(s[left]) - ord('A')] -= 1
                left+=1
                
            if right-left < min_right-min_left and self.is_complete(curr_count, counter, tset):
                min_left, min_right = left, right
                curr_count[ord(s[left]) - ord('A')] -= 1
                left+=1

            right+=1
        
        return s[min_left:min_right+1] if min_right < len(s)+1 else ""
    
    def is_complete(self, curr_count, counter, tset):
        for ch in tset:
            if curr_count[ord(ch) - ord('A')] < counter[ord(ch) - ord('A')]:
                return False
        
        return True

                

