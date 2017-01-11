#encoding=utf-8
'''
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Given a string, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    print 'input:%s' % s
    #有效字符串的起点(索引)，有效字符串的最大程度，输入串的长度
    validIndex, maxlen, length = 0, 0, len(s)
    poses = dict() #已遍历的字符对应的最新索引
    for index in range(length):
        c = s[index]
        if c in poses and poses[c] >= validIndex:
            print '1 maxlen(%s) validIndex(%s) index(%s) char(%s)' % (maxlen, validIndex, index, c)
            maxlen = max(maxlen, index-validIndex)
            validIndex = poses[c] + 1
        poses[c] = index
    print '2 maxlen(%s) validIndex(%s) length(%s)' % (maxlen, validIndex, length)
    return max(maxlen, length-validIndex)

lengthOfLongestSubstring('abcabcbb')
lengthOfLongestSubstring('bbb')
lengthOfLongestSubstring('')
lengthOfLongestSubstring('pwwkew')
