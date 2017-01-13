#encoding=utf-8
'''
    https://leetcode.com/problems/zigzag-conversion/

    1       5       9
    2   4   6   8   10
    3       7       11  -> 1,5,9,2,4,6,8,10,3,7,11
    

    1           7           13
    2       6   8       12  14
    3   5       9   11      15
    4           10          16
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if lens <= numRows or numRows <= 2: return s
        loop = (numRows - 1) * 2
        rt, index = '', 0
        for i in range(numRows):
            interval = loop - 2 * i
            print 'loop(%s) line(%s) interval(%s)' % (loop, i, interval)
            j = i
            while j < lens:
                rt += s[j]
                index += 1
                if interval<loop and interval>0 and j+interval<lens and index<lens:
                    rt += s[j+interval]
                    index += 1
                j += loop
        return rt

if __name__ == '__main__':
    obj = Solution()
    def func(s, numRows):
        rt = obj.convert(s, numRows)
        print '%s %s -> %s' % (s, numRows, rt)
    func('PAYPALISHIRING', 3)           #PAHNAPLSIIGYIR
    func('ABCDEFGHIJKLMNOP', 3)         #AEIMBDFHJLNPCGKO
    func('ABCDEFGHIJKLMNOPQRSTUV', 4)   #AGMSBFHLNRTCEIKOQUDJPV

