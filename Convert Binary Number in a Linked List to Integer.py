# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# 2 solutions

#FIRST SOLUTION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        while head:
            n = n << 1
            n += head.val
            head = head.next

        return n


#SECOND SOLUTION
        
#         if head==None:
#             return
        
#         number_binary = ""
        
#         while head!=None:
#             number_binary+=str(head.val)
#             head=head.next
#         number_binary = int(number_binary)
        
#         decimal, i = 0,0
#         while number_binary!=0:
#             dec = number_binary%10
#             decimal+=dec*(2**i)
#             number_binary = number_binary//10
#             i+=1
#         return decimal
