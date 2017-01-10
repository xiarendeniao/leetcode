#encoding=utf-8
'''
    穷举
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==None or needle==None: return -1
        lh, ln = len(haystack), len(needle)
        for i in range(lh-ln+1):
            found = True 
            for x in range(ln):
                if haystack[i+x] != needle[x]:
                    found = False
                    break
            if found: return i
        return -1

if __name__ == '__main__':
    obj = Solution()
    def func(x, aim):
        rt = obj.strStr(x,aim)
        print '%s %s -> %d' % (x, aim, rt)
    func('abcdefg', 'fg')
    func('', 'a')
    func('', '')
