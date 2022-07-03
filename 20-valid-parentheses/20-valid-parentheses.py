class Solution:
    def isValid(self, s):
        dict = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in s:
            if i in dict:
                stack.append(i)
            elif i == ')':
                if not stack: return False
                elif stack[-1] == '(': stack.pop()
                else: return False
            elif i == '}':
                if not stack: return False
                elif stack[-1] == '{': stack.pop()
                else: return False
            else:
                if not stack: return False
                elif stack[-1] == '[': stack.pop()
                else: return False
        
        if not stack:
            return True
        else:
            return False