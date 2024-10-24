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
        #Edgecase Below
        if not head:
            return None
        #Define variables
        myDict = {}
        myList = []
        curr = head

        while curr:
            newNode = Node(curr.val)
            myDict[curr] = newNode
            if newNode.val not in myList:
                myList.append(newNode)
            curr = curr.next
        curr = head
        for item in myList:
            item.next = myDict.get(curr.next)
            item.random = myDict.get(curr.random)
            curr = curr.next
        return myList[0]
            
            