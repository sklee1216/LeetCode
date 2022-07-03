class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        lst = []
        for start in range(len(s)):
            stack = []
            str = ''
            for c in s[start:len(s)+1]:
                    if c not in stack:
                        stack.append(c)
                        str += c
                    else:
                        break
            lst.append(len(str))
            
        return max(lst)
