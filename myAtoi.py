#encoding=utf-8

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        maxint = 1 << 31
        length, sign, index, rt = len(str), 1, 0, 0
        if str[0] == '+':
            index += 1
        elif str[0] == '-':
            index += 1
            sign = -1
        for index in range(index, length):
            if str[index] < '0' or str[index] > '9':
                break
            rt = rt*10 + int(str[index])
            #print '---', str[index], rt
            if rt >= maxint:
                break
        rt *= sign
        maxint = maxint - 1
        if rt >= maxint:
            return  maxint
        if rt < maxint * -1:
            return maxint * -1 - 1
        return rt

if __name__ == '__main__':
    obj = Solution()
    def f(s):
        print '%s\n: %d' % (s, obj.myAtoi(s))
    f('0')
    f('1234567')
    f('-1234567891011')
    f('')
