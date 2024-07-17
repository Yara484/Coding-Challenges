"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Using a hashmap
        mymap = {None:None}
        # First Pass - Creating copy nodes and storing its values in a hashmap
        curr = head
        while curr:
            copy_node = Node(curr.val)
            mymap[curr] = copy_node
            curr = curr.next

       # Second Pass - Adding next and random connections
        curr = head    
        while curr:
            new_node = mymap[curr]
            new_node.next = mymap[curr.next]
            new_node.random = mymap[curr.random]
            curr = curr.next

        return mymap[head]