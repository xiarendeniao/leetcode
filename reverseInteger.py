#encoding=utf-8

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, x):
        if x == 0:
            return 0
            
        neg = 1
        if x < 0:
            neg, x = -1, -x
        
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x / 10
        
        reverse = reverse * neg
        # [-(2^31-1),2^31-1]:       [-2147483647,2147483647]
        # [-(1<<31),(1<<31)-1]:     [-2147483648,2147483647]
        #负数的补码能比正数表示得多一位
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse

if __name__ == '__main__':
    obj = Solution()
    def func(x):
        print '%s -> %s' % (x, obj.reverseInteger(x))
    func(123)
    func(-123)
    func(-1)
    func(1)
    func(0xFFFFFFFF)
