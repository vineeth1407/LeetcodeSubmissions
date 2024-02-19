class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def insertHead(self, node):
        head_nxt = self.head.next
        head_nxt.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = head_nxt
        self.size += 1
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
    def removeTail(self):
        last = self.tail.prev
        self.removeNode(last)
        return last
    
class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freq = defaultdict(DLL)
        self.min_freq = 0
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        freq = node.freq
        self.freq[freq].removeNode(node)
        if self.freq[freq].size == 0:
            del self.freq[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1       
        self.freq[node.freq].insertHead(node)
        self.cache[key] = node
        return node.val
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return 
        if self.cap == len(self.cache):
            deleted = self.freq[self.min_freq].removeTail()
            del self.cache[deleted.key]
        node = Node(key, value)
        self.cache[key] = node
        self.freq[1].insertHead(node)
        self.min_freq = 1
                
                
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)