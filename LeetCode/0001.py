'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
#class Solution:
def twoSum( nums, target):
    b = []
    for i in range(0, len(nums)):
        if nums[i]*2 < target:
            continue
        for j in range(0,len(nums)):
            if i == j :
                continue
            if nums[i]+nums[j] == target:
                b.append(i)
                b.append(j)
                return b
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

if __name__ =='__main__':
    nums = [2,7,11,15]
    target = 14
    print(twoSum( nums,target))