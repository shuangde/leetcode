# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        num1 = int(self.getStr(l1))
        num2 = int(self.getStr(l2))
        sum = num1 + num2
        res = ListNode(sum%10)
        sum /= 10
        p = res
        while sum:
            tmp = ListNode(sum%10)
            sum /= 10
            p.next = tmp;
            p = tmp
        return res
    
    def getStr(self, l): 
        res = ""
        while l:
            res += str(l.val)
            l = l.next
        return res[-1:0:-1] + res[0]
