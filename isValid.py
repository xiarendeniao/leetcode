#encoding=utf-8
'''
    栈
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length % 2 == 1: return False
        stack = list()
        for i in range(length):
            c = s[i]
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if not stack: return False
                if (c==')' and stack[-1]!='(') or (c==']' and stack[-1]!='[') or (c=='}' and stack[-1]!='{'):
                    return False
                stack.pop()
        return not stack

if __name__ == '__main__':
    obj = Solution()
    def func(x):
        rt = obj.isValid(x)
        print '%s -> %s' % (x,rt)
    func('{(())}')
    func('{[](())}')
    func('{[]())}')
    func('([)]')
