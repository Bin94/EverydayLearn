class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a<0 and b>0:
            if (-1)*a > b:


        while(b!=0):
            c = a&b
            a = a^b
            b = c<<1
        return a

if __name__ == '__main__':
    s = Solution()
    a =-1
    b =1
    print(s.getSum(a,b))

