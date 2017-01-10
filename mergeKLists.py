#encoding=utf-8
'''
    mergeTwoLists的升级版，两两归并，最后合成一个
'''

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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None
        length = len(lists)
        if length == 1:
            return lists[0]
        elif length == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            return self.mergeTwoLists(self.mergeKLists(lists[:length/2]),self.mergeKLists(lists[length/2:]))

if __name__ == '__main__':
    obj = Solution()
    def f(ls):
        LS = list()
        for l in ls:
            L = l and ListNode(None) or None
            if L:
                ptr = L
                for e in l:
                    if ptr.val == None:
                        ptr.val = e
                    else:
                        ptr.next = ListNode(e)
                        ptr = ptr.next
            LS.append(L)

        RT = obj.mergeKLists(LS)
        rt = list()
        ptr = RT
        while ptr:
            rt.append(ptr.val)
            ptr = ptr.next
        print '%s: %s' % (str(ls), str(rt))
    f(([1,2,3],[2,3,4],[2,4,9],[2,4,7]))
    f(([],[2,3,4],[3,10,100]))
