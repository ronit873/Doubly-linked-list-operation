class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def split(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        if middle:
            middle.prev = None
        return middle

    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        
        if first.data <= second.data:
            result = first
            result.next = self.merge(first.next, second)
            if result.next:
                result.next.prev = result
        else:
            result = second
            result.next = self.merge(first, second.next)
            if result.next:
                result.next.prev = result
        
        result.prev = None
        return result
    
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        second = self.split(head)
        first = self.mergeSort(head)
        second = self.mergeSort(second)
        return self.merge(first, second)

    def sort_doubly(self, head):
        return self.mergeSort(head)


def print_list(head):
    temp = head
    last = None
    while temp:
        print(temp.data, end=" ↔ ") if temp.next else print(temp.data)
        last = temp
        temp = temp.next
    
    
    while last:
        print(last.data, end=" ↔ ") if last.prev else print(last.data)
        last = last.prev