#encoding=utf-8
'''
  先找出正数第N个节点，然后把这个区间往后移，触碰到结尾时区间头部就是目标节点
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        r = head
        for _ in range(n):
            r = r.next
        if not r: return head.next
        l = head
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head

if __name__ == '__main__':
    obj = Solution()
    def f(l1, n):
        L1 = l1 and ListNode(None) or None
        if L1:
            ptr = L1
            for e in l1:
                if ptr.val == None:
                    ptr.val = e
                else:
                    ptr.next = ListNode(e)
                    ptr = ptr.next

        RT = obj.removeNthFromEnd(L1,n)
        rt = list()
        ptr = RT
        while ptr:
            rt.append(ptr.val)
            ptr = ptr.next
        print '%s %s: %s' % (str(l1), n, str(rt))
    f([1,2,3,4,5], 2)
    f([9,2,4], 1)
    f([2,3,4], 3)
