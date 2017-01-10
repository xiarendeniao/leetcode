#encoding=utf-8
'''
    递归,深度优先搜索
    有点麻烦，时间有限，暂时放弃
'''

class Solution:
     def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.rt = list()
        l = candidates
        l.sort()
        self.search(l, 0, target, [])
        return self.rt
    
     def search(self, l, start, target, rt):
        for i in range(start, len(l)):
            if l[i] > target:
                return
            elif l[i] == target:
                self.rt.append(rt+[l[i]])
            else:
                self.search(l, i+1, target-l[i], rt+[l[i]])

if __name__ == '__main__':
    obj = Solution()
    def func(x, aim):
        s1 = str(x)
        rt = obj.combinationSum(x, aim)
        print '%s %s-> %s' % (s1, aim, rt)
    func([1,2,3,4,5], 3)
    func([], 0)
    func([1], 1)
    func([1,11], 0)
    func([1,2,3], 2)
    func([1,2,10,20,30,11], 33)
    func([2,3,6,7], 7)
    func([10, 1, 2, 7, 6, 1, 5], 8)
