class Solution:
    def intersectPoint(self, head1, head2):
        
        s = set()
        while head1:
            s.add(head1)
            head1 = head1.next
        
        while head2:
            if head2 in s:
                return head2
            head2 = head2.next

