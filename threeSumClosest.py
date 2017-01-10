#encoding=utf-8

'''
    threeSum:排序后穷举第一个元素,第二和第三个元素从子列表的首尾往中间遍历:>目标值则第三个元素左移、<目标值则第三个元素右移
    比threeSum还简单些
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rt = None
        for x in range(0, len(nums)-2):
            y, z = x+1, len(nums)-1
            while y < z:
                sum = nums[x] + nums[y] + nums[z] 
                #print '%s+%s+%s=\t%s\trt(%s)' % (nums[x], nums[y], nums[z], sum, rt)
                if (rt == None) or (abs(rt-target) > abs(sum-target)):
                    rt = sum 
                if sum < target:
                    y += 1
                    while y < z and nums[y] == nums[y-1]: y += 1
                elif sum > target:
                    z -= 1
                    while y < z and nums[z] == nums[z+1]: z -= 1
                else:
                    break
        return rt

if __name__ == '__main__':
    obj = Solution()
    def f(x, target):
        print '%s,%s\t: %s' % (x, target, obj.threeSumClosest(x,target))
    f([-1, 2, 1, -4], 1)
    f([-4, -8, 10, 7], 10)
    f([0,2,1,-3], 1)
