'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''滑动窗口'''
        lst = []  # 存储不重复字符串
        max_len = 0 # 当前最大长度
        res = 0  # 结果
        for i in range(len(s)):
            if not s[i] in lst:
                lst.append(s[i])
                max_len += 1

            else:
                index = lst.index(s[i])
                lst = lst[index + 1:]   # 删除重复字符串前的字符
                lst.append(s[i])
                max_len = len(lst)
            if max_len > res:
                res = max_len
        return res
