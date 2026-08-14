class Solution:
    def decodeString(self, s: str) -> str:
        
        res = ""
        num = 0
        stack = []

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = num*10+int(ch)

            elif ch == '[':
                stack.append([res, num])
                res = ""
                num = 0

            elif ch == ']':
                curr = stack.pop()
                res = curr[0] + (res * curr[1])
            
            else:
                res += ch        

        
        return res