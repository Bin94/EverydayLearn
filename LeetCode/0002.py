'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l1
        flag = False
        while l1.next and l2.next:
            l1.val = l1.val + l2.val
            if flag:
                l1.val += 1
                flag = False
            if l1.val >= 10:
                l1.val -= 10
                flag = True
            if l1.next == None:
                break
            if l2.next == None:
                break
            l1 = l1.next
            l2 = l2.next
        if flag:
            l1.val += 1
            flag = False
        if l1.val >= 10:
            l1.val -= 10
            flag = True
        l1 = l1.next
        l2 = l2.next

        if l2.next:
            l1.next = l2.next
            l1 = l1.next
        while l1.next:
            if flag:
                l1.val += 1
                flag = False
            if l1.val >= 10:
                l1.val -= 10
                flag = True
            l1 = l1.next
        return l3

if __name__ == '__main__':
    x = ListNode(2)
    y = ListNode(4)
    l1 = x
    x.next = y
    x = x.next
    y = ListNode(3)
    x.next = y
    

