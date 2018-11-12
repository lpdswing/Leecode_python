# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index,num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = index
            else:
                return [d[n],index]



# 29 / 29 个通过测试用例
# 状态：通过
# 执行用时：48 ms
# 提交时间：3 分钟之前




if __name__ == '__main__':
    l = [2,7,11,15]
    print(Solution().twoSum(l,9))