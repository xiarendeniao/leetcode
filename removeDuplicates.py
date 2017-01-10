#encoding=utf-8
'''
    遍历把不重复的从数组开头往后放
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0 or length == 1: return length
        count = 1
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
        return count

if __name__ == '__main__':
    obj = Solution()
    def func(x):
        s1 = str(x)
        rt = obj.removeDuplicates(x)
        print '%s -> %s, %s' % (s1, str(x), rt)
    func([1,2,3,4,5])
    func([])
    func([1])
    func([1,1,1,1])
    func([1,1,2])
    func([1,1,1,2])
