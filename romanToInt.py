#encoding=utf-8

'''
    1-I     2-II    3-III   4-IV    5-V     6-VI    7-VII   8-VIII      9-IX
    10-X    20-XX   30-XXX  40-XL   50-L    60-LX   70-LXX  80-LXXX     90-XC
    100-C   200-CC  300-CCC 400-CD  500-D   600-DC  700-DCC 800-DCCC    900-CM
    1000-M  2000-MM 3000-MMM
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '': return rt

        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        rt = d[s[-1]]
        index = len(s) - 2
        while index >= 0:
            if d[s[index]] >= d[s[index+1]]:
                rt += d[s[index]]
            else:
                rt -= d[s[index]]
            index -= 1
        return rt

if __name__ == '__main__':
    obj = Solution()
    def f(x):
        print '%s\t: %d' % (x, obj.romanToInt(x))
    f('I')
    f('IV')
    f('V')
    f('IX')
    f('X')
    f('XI')
    f('XIV')
    f('XL')
    f('XLIV')
    f('L')
    f('MCMXCIX')
    f('MMMCMXCIX')
