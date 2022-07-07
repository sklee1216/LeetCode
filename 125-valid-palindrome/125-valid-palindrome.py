from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        stack = deque()
        
        for c in s:
            if c.isalpha() or c.isnumeric():
                stack.append(c.lower())
                
        while stack and len(stack) > 1:
            a = stack.popleft()
            b = stack.pop()
            if a == b: 
                continue
            else:
                return False
        return True
                      