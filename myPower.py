#encoding=utf-8
'''
    https://leetcode.com/problems/powx-n/
'''

import math

class Solution(object):
    def myPow_v1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        flag = False
        if n < 0: flag, n = True, -n
        rt = 1
        for i in range(n):
            rt *= x
        if flag: rt = 1/rt
        return rt

    def myPow_v2(self, x, n):
        return math.pow(x,n)

    def myPow_v3(self, x, n):
        def f(x, n):
            if n == 0: return 1
            half = f(x, n/2)
            if n & 1 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            return 1.0/f(x, -n)
        else:
            return f(x, n) 

if __name__ == '__main__':
    obj = Solution()
    
    def test(f):
        import time
        ut1 = time.time()
        obj.myPow = f
        for i in range(100):
            for j in range(100):
                obj.myPow(i, j)
        ut2 = time.time()
        print '%s: %s sec' % (f, ut2-ut1)

    test(obj.myPow_v1)
    test(obj.myPow_v2)
    test(obj.myPow_v3)
