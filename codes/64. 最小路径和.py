'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

'''
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        动态规划
        逐步构造i,j的最小值
        边界分为i==0,j==0,i,j都不等于0
        '''
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    continue
                elif i==0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                elif j==0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]