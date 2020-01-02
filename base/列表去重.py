# -*-coding:utf-8 -*-
'''
@Description: 列表去重示例
@Author: superz
@Date: 2020-01-02 21:53:22
@LastEditTime : 2020-01-02 21:57:46
'''

nums = [1, 2, 2, 3, 3, 3]
print("原列表数据："+str(nums))
nums2 = set(nums)
print("去重后的数据"+str(nums2))
