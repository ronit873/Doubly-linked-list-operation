class Solution:
    def pairwiseSwap(self, head):
        while head and head.next: 
            head.data, head.next.data, head = head.next.data, head.data, head.next.next