class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.myDict = {}
        self.capacity = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

        

    def get(self, key: int) -> int:
        if key in self.myDict:
            self.remove(self.myDict[key])
            self.insert(self.myDict[key])
            return self.myDict[key].val
        return -1
       
        

    def put(self, key: int, value: int) -> None:

        if key in self.myDict:
            self.remove(self.myDict[key])
        self.myDict[key] = ListNode(key, value)
        self.insert(self.myDict[key])

        if len(self.myDict) > self.capacity:
            #remove from LL and remove from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.myDict[lru.key]

        #remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
        

    #insert node at right most position 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)