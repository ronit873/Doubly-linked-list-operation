class Solution:
    def delete_node(self, head, x):
        
        if head is None:
            return None
        
        temp = head
        count = 1
        
        while temp:
            if count == x:
                
                if temp.prev is None:
                    head = temp.next
                    if head: 
                        head.prev = None
                    return head
                
                
                elif temp.next is None:
                    temp.prev.next = None
                    return head
                
            
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return head
                    
            count += 1
            temp = temp.next
        
        return head  