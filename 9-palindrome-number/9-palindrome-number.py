from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        n = len(x)
        queue = deque()
        stack = []
        strs1 = ''
        strs2 = ''
        for s in x:
            queue.append(s)
            stack.append(s)
        for _ in range(n):
            strs1 += queue.popleft()
            strs2 += stack.pop()
        if strs1 == strs2:
            return True
        else:
            return False
            
            