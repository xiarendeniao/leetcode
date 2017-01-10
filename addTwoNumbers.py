#encoding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rt = ListNode(None)
        ptr = rt
        add = 0
        while True:
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            ptr.val = add%10
            add /= 10
            if not l1 and not l2 and add == 0: break
            ptr.next = ListNode(None)
            ptr = ptr.next
        return rt

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

        RT = obj.addTwoNumbers(L1,L2)
        rt = list()
        ptr = RT
        while ptr:
            rt.append(ptr.val)
            ptr = ptr.next
        print '%s+%s: %s' % (str(l1), str(l2), str(rt))
    f([1,2,3],[2,3,4])
    f([9,2,4],[2,7,4])
    f([],[2,3,4])
