#encoding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        rt = head
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    rt.next = l1
                    rt = rt.next
                    l1 = l1.next
                else:
                    rt.next = l2
                    rt = rt.next
                    l2 = l2.next
            elif not l1:
                rt.next = l2
                rt = rt.next
                l2 = l2.next
            elif not l2:
                rt.next = l1
                rt = rt.next
                l1 = l1.next
        return head.next

if __name__ == '__main__':
    obj = Solution()
    def f(l1, l2):
        L1 = l1 and ListNode(None) or None
        if L1:
            ptr = L1
            for e in l1:
                if ptr.val == None:
                    ptr.val = e
                else:
                    ptr.next = ListNode(e)
                    ptr = ptr.next

        L2 = l2 and ListNode(None) or None
        if L2:
            ptr = L2
            for e in l2:
                if ptr.val == None :
                    ptr.val = e
                else:
                    ptr.next = ListNode(e)
                    ptr = ptr.next

        RT = obj.mergeTwoLists(L1,L2)
        rt = list()
        ptr = RT
        while ptr:
            rt.append(ptr.val)
            ptr = ptr.next
        print '%s merge %s: %s' % (str(l1), str(l2), str(rt))
    f([1,2,3],[2,3,4])
    f([2,4,9],[2,4,7])
    f([],[2,3,4])
