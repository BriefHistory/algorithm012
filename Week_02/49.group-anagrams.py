#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
#主要是dict.get()函数的理解
#dict.get(key, default=None)
# 1. key -- 字典中要查找的键。
# 2. default -- 如果指定键的值不存在时，返回该默认值。


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())
""" class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values()) """


        
# @lc code=end

