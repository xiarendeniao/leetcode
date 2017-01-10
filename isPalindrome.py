#encoding=utf-8

#整数翻转的延伸版本，如果后半截翻转结果(数字个数有单数和双数两种)跟前半截相等就说明对称的
#负数、个位数为零的直接False

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0): return False
        rev = 0
        while rev < x:
            rev = rev*10 + x%10
            x /= 10
        return (rev==x) or (rev/10==x)

if __name__ == '__main__':
    obj = Solution()
    def f(x):
        print '%d\t: %s' % (x, obj.isPalindrome(x))
    f(1234567654321)
    f(1234321)
    f(12344321)
    f(0)
    f(1)
    f(18909810)
    f(121212)
