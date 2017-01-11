#encoding=utf-8
#https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.func(nums1, nums2, n/2+1)
        else:
            left = self.func(nums1, nums2, n/2)
            right = self.func(nums1, nums2, n/2+1)
            #print('left(%s) right(%s)' % (left, right))
            return (left+right)/2.0

    def func(self, A, B, k):
        #归并A+B，得到X。目标是查找X[k-1]
        if len(A) == 0: return B[k-1]
        if len(B) == 0: return A[k-1]
        if k == 1: return min(A[0], B[0])
        if k == len(A) + len(B): return max(A[-1], B[-1])

        if len(A) >= k/2: a = A[k/2-1]
        else: a = None
        if len(B) >= k/2: b = B[k/2-1]
        else: b = None

        #如果len(A)<k/2，B[k/2-1]肯定会落在X[0:k-2]这个区间,所以可以排除B[0:k/2-1]了
        if a == None:
            return self.func(A, B[k/2:], k-k/2)
        if b == None:
            return self.func(A[k/2:], B, k-k/2)

        #len(A)>=k/2 len(B)>=k/2
        #如果A[k/2-1]<B[k/2-1], A[k/2-1]肯定会落在X[0:k-2]这个区间,所以可以排除A[0:k/2-1]了
        if a <= b:
            return self.func(A[k/2:], B, k-k/2)
        if a > b:
            return self.func(A, B[k/2:], k-k/2)
            

if __name__ == '__main__':
    obj = Solution()
    print obj.findMedianSortedArrays([1, 3],[2])
    print obj.findMedianSortedArrays([1, 2],[3, 4])
