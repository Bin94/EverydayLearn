'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

注意：不要使用任何内置的库函数，如  sqrt。
'''
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        if num ==0:
            return True
        else:
            return False

s = Solution()
print(s.isPerfectSquare(199*199))