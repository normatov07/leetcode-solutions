class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counter = [0] * 58
        curr_count = [0] * 58
        s_codes = []
        tset = set()

        for ch in t:
            code = ord(ch) - ord('A')
            counter[code] += 1
            tset.add(code)
        
        for ch in s:
            s_codes.append(ord(ch) - ord('A'))

        min_left, min_right = 0, len(s)+1
        left, right = 0, 0
        
        while right < len(s):
            curr_count[s_codes[right]] += 1

            while left <= right and curr_count[s_codes[left]] > counter[s_codes[left]]:
                curr_count[s_codes[left]] -= 1
                left+=1
                
            if right-left < min_right-min_left and self.is_complete(curr_count, counter, tset):
                min_left, min_right = left, right
                curr_count[s_codes[left]] -= 1
                left+=1

            right+=1
        
        return s[min_left:min_right+1] if min_right < len(s)+1 else ""
    
    def is_complete(self, curr_count, counter, tset):

        for code in tset:
            if curr_count[code] < counter[code]:
                return False
        
        return True

                

