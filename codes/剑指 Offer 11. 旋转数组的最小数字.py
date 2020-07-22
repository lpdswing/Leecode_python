'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''
from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        '''暴力解法'''
        return min(numbers)


class Solution1:
    def minArray(self, numbers: List[int]) -> int:
        '''最小值的前一个数一定大于它,否则就是第一个数最小'''
        for i in range(0,len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                return numbers[i+1]
        return numbers[0]


class Solution2:
    def minArray(self, numbers: List[int]) -> int:
        '''
        二分法,i,j,m为数组左右端点和中间端点, i<=m<j
        numbers[m] > numbers[j], m一定在左数组,旋转点在[m+1,j], i=m+1
        numbers[m] < numbers[j], m一定在右数组,旋转点在[i,m], j = m,
        numbers[m] = numbers[j], 无法判断m在哪,因此j=j-1,缩小范围
        :param numbers:
        :return:
        '''
        i, j = 0,len(numbers)-1
        while i<j:
            m = i + (j - i) >> 1  # 右移1表示除2
            if numbers[m] > numbers[j]:
                i = m+1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]
