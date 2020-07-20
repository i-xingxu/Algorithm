# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 打印所有节点
    def input(self):
        while 1:
            print(self.val)
            if self.next == None: break
            self = self.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(-1)
        tmp = temp
        while l1 and l2:
            if int(l1.val) <= int(l2.val):
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is None: tmp.next = l2
        if l2 is None: tmp.next = l1

        return temp.next


l1 = ListNode(3)
l1 = ListNode(2, l1)
l1 = ListNode(1, l1)
l2 = ListNode(4)
l2 = ListNode(2, l2)
l2 = ListNode(1, l2)
# l1.input()
# l2.input()
s = Solution()
t = s.mergeTwoLists(l1, l2)
while 1:
    print(t.val)
    if t.next == None: break
    t = t.next
