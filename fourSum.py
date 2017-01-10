#encoding=utf-8
'''
    threeSum: 排序后穷举第一个元素,第二和第三个元素从子列表的首尾往中间遍历:>目标值则第三个元素左移、<目标值则第三个元素右移
    threeSum的外层再加一个穷举
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        rt = list()
        for x in range(0, length-3):
            if x and nums[x] == nums[x-1]: continue
            for y in range(x+1, length-2):
                if y!=x+1 and nums[y]==nums[y-1]: continue
                z, a, aim = y+1, length-1, target-nums[x]-nums[y]
                while z < a:
                    sum = nums[z] + nums[a]
                    if sum < aim:
                        z += 1
                        while z < a and nums[z] == nums[z-1]: z += 1
                    elif sum > aim:
                        a -= 1
                        while z < a and nums[a] == nums[a+1]: a -= 1
                    else:
                        rt.append((nums[x], nums[y], nums[z], nums[a]))
                        z += 1
                        a -= 1
                        while z < a and nums[z] == nums[z-1]: z += 1
                        while z < a and nums[a] == nums[a+1]: a -= 1
        return rt
        

if __name__ == '__main__':
    obj = Solution()
    def f(x, aim):
        print '%s %s\t: %s' % (x, aim, obj.fourSum(x,aim))
    f([1, 0, -1, 0, -2, 2], 0)
    f([-1, 0, 1, 2, -1, -3, -4], 0)
    f([0,0,-1,-1,-9,1,8,1], 9)
