#encoding=utf-8

'''
    方案1: beats 16.83 or python submissions.
        从前往后遍历，找到跟当前字符相等的字符后判定两字符之间的子串是否Palindrome

    方案2:
        从前往后遍历，对于每个字符判断它左右是否对称

    貌似方案2效率更好一些
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ax, ay, maxlen, slen = 0, 0, 1, len(s)
        for i in range(slen):
            for j in range(i+1, slen):
                if s[i] != s[j]: continue
                left, right = i, j
                while left <= right and s[left] == s[right]: 
                    left += 1
                    right -= 1
                if left > right:
                    tlen = j - i + 1
                    if tlen >= maxlen:
                        ax, ay, maxlen = i, j, tlen
        return s[ax:ay+1]

if __name__ == '__main__':
    obj = Solution()
    def f(s):
        print '%s\t-> %s' % (s, obj.longestPalindrome(s))
    f('babad')
    f('badababad')
    f('cbbd')
        
