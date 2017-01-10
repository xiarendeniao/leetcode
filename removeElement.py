#encoding=utf-8
'''
    遍历一遍把符合要求元素置换到数组最后面的位置上去，这个题目的暗示和针对性好强
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                #print 'i(%s) j(%s) nums[i](%s) nums[j](%s)' % (i, j, nums[i], nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                j = j - 1
            else:
                i = i + 1
        return min(i+1, j+1)

if __name__ == '__main__':
    obj = Solution()
    def func(x, aim):
        s1 = str(x)
        rt = obj.removeElement(x,aim)
        print '%s %d -> %s, %s' % (s1, aim, str(x), rt)
    func([1,2,3,4,5], 2)
    func([], 1)
    func([1], 1)
