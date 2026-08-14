class Solution:
    def decodeString(self, s: str) -> str:
        
        res = ""
        stack = []

        for i, ch in enumerate(s):
            if ch.isdigit():
                if i > 0 and s[i-1].isdigit():
                    stack[-1][0] += ch
                else:
                    stack.append([ch, ""])                
            elif ch == ']':
                current = stack.pop()
                if stack:
                    stack[-1][1] += current[1] * int(current[0])
                else:
                    res += current[1] * int(current[0])
            elif ch == '[':
                continue
            elif not stack:
                res += ch
            else:
                stack[-1][1] += ch             

        
        return res