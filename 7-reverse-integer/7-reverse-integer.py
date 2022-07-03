from collections import deque

class Solution:
    def reverse(self, x: int) -> int:
        stack = deque()
        ans = ''
        if x == 0:
            return 0
        for s in str(x):
            stack.append(s) 
        
        if stack[0] == '-':
            stack.append(stack.popleft())
        if stack[-1] == '0':
            stack.pop()
        for _ in range(len(stack)):
            ans += stack.pop()
        if (int(ans) <= -2**(31) or int(ans) >= 2**(31)-1):
            return 0
        else:
            return int(ans)
        