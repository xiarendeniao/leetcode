#encoding=utf-8

'''
    1-I     2-II    3-III   4-IV    5-V     6-VI    7-VII   8-VIII      9-IX
    10-X    20-XX   30-XXX  40-XL   50-L    60-LX   70-LXX  80-LXXX     90-XC
    100-C   200-CC  300-CCC 400-CD  500-D   600-DC  700-DCC 800-DCCC    900-CM
    1000-M  2000-MM 3000-MMM
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1:{1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'},
             2:{1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'},
             3:{1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'},
             4:{1:'M', 2:'MM', 3:'MMM'}}
        index = 1
        rt = ''
        while num > 0:
            digit = num%10
            if digit != 0: rt = d[index][digit] + rt
            num = num/10
            index += 1
        return rt

if __name__ == '__main__':
    obj = Solution()
    def f(x):
        print '%d\t: %s' % (x, obj.intToRoman(x))
    f(1)
    f(4)
    f(5)
    f(9)
    f(10)
    f(11)
    f(14)
    f(40)
    f(44)
    f(50)
    f(1999)
    f(3999)
    
