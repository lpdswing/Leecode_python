'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''递归解法'''
        def gen(start, end):
            res = []
            if start > end:
                return [None]
            for i in range(start, end + 1):
                left_trees = gen(start, i - 1) # 左树范围必然小于i
                right_trees = gen(i + 1, end)  # 右树范围必然大于i

                for l in left_trees:
                    for r in right_trees:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        res.append(cur)
            return res

        return gen(1, n) if n else []


class Solution1:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''动态规划'''
        def dp_func(start, end):
            dp = {}
            if (start,end) not in dp:
                if start == end:
                    dp[start, end] = [TreeNode(start)]
                else:
                    lst = []
                    for root in range(start, end+1):
                        # start > end 为[None]
                        left = dp_func(start, root-1) if root-1>=start else [None]
                        right = dp_func(root+1,end) if root+1<=end else [None]
                        for i in left:
                            for j in right:
                                root_node = TreeNode(root)
                                root_node.left = i
                                root_node.right = j
                                lst.append(root_node)
                    dp[start, end] = lst
            return dp[start, end]
        return dp_func(1, n)