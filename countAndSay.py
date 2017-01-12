#encoding=utf-8
'''
    https://leetcode.com/problems/count-and-say/
    1: 1
    2: 11       1个1
    3: 21       2个1
    4: 1211     1个2 1个1
    5: 111221   1个1 1个2 2个1
    6: 312211   3个1 2个2 1个1
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        lasts, i = None, 0
        while i < n: #两个while替换两个for..range()，leetcode排名从倒数47%提升到倒数%56.
            i += 1
            if lasts == None:
                lasts = '1'
            else:
                s = ''
                tlen, tchar, j, lens = 1, lasts[0], 1, len(lasts)
                while j < lens:
                    if lasts[j] == tchar:
                        tlen += 1
                    else:
                        s += '%d%s' % (tlen,tchar)
                        tlen, tchar = 1, lasts[j]
                    j += 1
                s += '%d%s' % (tlen,tchar)
                lasts = s
        return lasts 

if __name__ == '__main__':
    obj = Solution()
    def f(x):
        print '%s\t: %s' % (x, obj.countAndSay(x))
    f(2)
    for i in range(100):
        f(i)
