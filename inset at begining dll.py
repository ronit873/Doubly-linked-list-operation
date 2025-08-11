class Solution:
    def addNode(self, head, p, x):
        curr = head
        node = Node(x)
        count = 0
        while(curr):
            if count == p:
                if curr.next:
                    node.next = curr.next
                    curr.next.prev = node
                curr.next = node
                node.prev = curr
                return head
            count += 1
            curr = curr.next