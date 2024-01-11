class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    # Needs capacity, hashmap and DLL
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        # Get from map
        node = self.dict[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key is getting updated
        if key in self.dict:
            self.remove(self.dict[key])
        
        # if cache size is full
        if len(self.dict) == self.capacity:
            self.remove(self.tail.prev)

        # insert
        self.insert(ListNode(key, value))

    def remove(self, node: ListNode) -> None:
        # remove from map
        del self.dict[node.key]

        # remove from dll
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node: ListNode) -> None:
        # add into map
        self.dict[node.key] = node

        # add in DLL
        headnext = self.head.next
        self.head.next = node
        node.prev = self.head
        headnext.prev = node
        node.next = headnext

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)