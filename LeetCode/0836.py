'''
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。
'''

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        xl = [rec2[0],rec2[2]]
        yl = [rec2[1],rec2[3]]
        xs = [0,0]
        ys = [0,0]

        for i in [0,1]:
            if xl[i] < rec1[0]:
                xs[i] = 1
            elif xl[i] == rec1[0]:
                xs[i] = 2
            elif xl[i] > rec1[0] and xl[i] < rec1[2]:
                xs[i] = 3
            elif xl[i] ==rec1[2]:
                xs[i] = 4
            elif xl[i] > rec1[2]:
                xs[i] = 5

            if yl[i] < rec1[1]:
                ys[i] = 1
            elif yl[i] == rec1[1]:
                ys[i] = 2
            elif yl[i] > rec1[1] and yl[i] < rec1[3]:
                ys[i] = 3
            elif yl[i] ==rec1[3]:
                ys[i] = 4
            elif yl[i] > rec1[3]:
                ys[i] = 5

        if ys[0] >= 4 or xs[0] >= 4:
            return False
        if ys[1] <= 2 or xs[1] <= 2:
            return False

        for i in [0,1]:
            if xs[i] >= 2 and ys[i] >= 2:
                return True
        if xs[0] == 1 or xs[0]==2 or xs[0] ==3:
            if xs[1] >= 2 and ys[1] >= 2:
                return True

        return False











