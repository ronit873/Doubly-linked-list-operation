class Solution:
    def isCircular(self, head):
        temp=head
        first=head
        
        if temp.next is None:
            return False
            
        while temp.next is not None:
            if temp.next == first:
                return True
            temp=temp.next
        return False