'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''双指针解法 时间O(n),空间O(1)'''
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]


class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''字典法 O(n)'''
        hash={}
        for i in range(len(numbers)):
            if target-numbers[i] in hash:
                return [hash[target-numbers[i]],i+1]
            if numbers[i] not in hash:
                hash[numbers[i]]=i+1


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''二分法,时间复杂度 O(n*log(n))'''
        n = len(numbers)
        for i in range(n):
            l,r = i + 1, n - 1
            while l <= r:
                mid = (l+r)//2
                if numbers[mid] + numbers[i] == target:
                    return [i+1, mid+1]
                elif numbers[mid] + numbers[i] < target:
                    l = mid + 1
                else:
                    r = mid - 1

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    print(Solution1().twoSum(nums,9))