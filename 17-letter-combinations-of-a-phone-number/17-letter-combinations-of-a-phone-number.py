class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2':['a','b','c'],
               '3': ['d','e','f'],
               '4': ['g','h','i'],
               '5': ['j','k','l'],
               '6': ['m','n','o'],
               '7': ['p','q','r','s'],
               '8': ['t','u','v'],
               '9': ['w','x','y','z']}
        
        lst = []
        s = ''
        
        n = len(digits)
        
        if n == 0: return []
        
        elif n == 1:
            for i in dict[digits]:
                lst.append(i)
            return lst
        elif n == 2:
            for i in dict[digits[0]]:
                for j in dict[digits[1]]:
                    lst.append(i+j)
            return lst
        elif n == 3:
            for i in dict[digits[0]]:
                for j in dict[digits[1]]:
                    for k in dict[digits[2]]:
                        lst.append(i+j+k)
            return lst
        else:
            for i in dict[digits[0]]:
                for j in dict[digits[1]]:
                    for k in dict[digits[2]]:
                        for z in dict[digits[3]]:
                            lst.append(i+j+k+z)
            return lst
            
                    
            
        