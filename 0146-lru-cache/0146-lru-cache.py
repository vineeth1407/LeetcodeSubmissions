class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.look_up = {}
     
    def add_node(self,key,value):
        temp = self.head.next
        new_node = Node(data=(key,value))
        new_node.next = temp
        self.head.next = new_node
        new_node.prev = self.head
        temp.prev= new_node
        return new_node
    def delete_node(self,node):
        prev = node.prev
        nextt = node.next
        prev.next = nextt
        nextt.prev = prev
        
        

    def get(self, key: int) -> int:
        #print(self.look_up.keys())
        if key in self.look_up:
            node = self.look_up[key]
            #print(node.data)
            value = node.data[1]
            self.delete_node(node)
            new_node = self.add_node(key,value)
            self.look_up[key] = new_node
            return value
            
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.look_up:
            node = self.look_up[key]
            self.delete_node(node)
            del self.look_up[key]
            new_node = self.add_node(key,value)
            self.look_up[key] = new_node
            
        else:
            if len(self.look_up) < self.capacity:
                new_node = self.add_node(key,value)
            else:
                delnode = self.tail.prev
                del_key = delnode.data[0]
                del self.look_up[del_key]
                self.delete_node(self.tail.prev)
                new_node = self.add_node(key,value)
                
            #print("before",new_node.data)
            
            self.look_up[key]= new_node
            #print("after",self.look_up)
                
                
                
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)