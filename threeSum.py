#encoding=utf-8
#https://leetcode.com/problems/3sum

'''
    排序后穷举第一个元素,第二和第三个元素从子列表的首尾往中间遍历:>目标值则第三个元素左移、<目标值则第三个元素右移
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rt = list()
        for x in range(0, len(nums)-2):
            if x and nums[x] == nums[x-1]: continue
            #print 'x(%s-%s)' % (x, nums[x])
            y, z, aim = x+1, len(nums)-1, 0-nums[x]
            while y < z:
                sum = nums[y] + nums[z] 
                if sum < aim:
                    y += 1
                    while y < z and nums[y] == nums[y-1]: y += 1
                elif sum > aim:
                    z -= 1
                    while y < z and nums[z] == nums[z+1]: z -= 1
                else:
                    #print 'x(%s-%s) y(%s-%s) z(%s-%s)' % (x, nums[x], y, nums[y], z, nums[z])
                    rt.append((nums[x], nums[y], nums[z]))
                    y += 1
                    z -= 1
                    while y < z and nums[y] == nums[y-1]: y += 1
                    while y < z and nums[z] == nums[z+1]: z -= 1
        return rt

if __name__ == '__main__':
    obj = Solution()
    def f(x):
        print '%s\t: %s' % (x, obj.threeSum(x))
    f([-1, 0, 1, 2, -1, -4])
    f([0,0,-1,-1,-9,1,8,1])
