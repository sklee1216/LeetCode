class Solution:
    def getRow(self, rowIndex):
        ans = [[1]*n for n in range(1,rowIndex+2)]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans[rowIndex]