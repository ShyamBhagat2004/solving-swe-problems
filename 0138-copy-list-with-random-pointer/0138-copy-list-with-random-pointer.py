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
        def createNode(x: int, next: 'Node' = None, random: 'Node' = None):
            return Node(x, next, random)
        myDict = {}
        curr = head
        myList = []

        if not head:
            return None

        while curr:
            newNode = createNode(curr.val)
            myDict[curr] = newNode #Map new node to its copy
            if newNode.val not in myList:
                myList.append(newNode)
            curr = curr.next

        curr = head

        #Second pass
        for newNode in myList:
            newNode.next = myDict.get(curr.next)
            newNode.random = myDict.get(curr.random)
            curr = curr.next
        return myList[0]