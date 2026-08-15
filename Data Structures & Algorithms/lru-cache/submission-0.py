class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def AddToFront(self,node:Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def RemoveNode(self,node:Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def RemoveFromEnd(self) -> Node:
        lru = self.tail.prev
        self.RemoveNode(lru)
        return lru
class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = Counter()
        self.capacity = capacity
        self.currentCapacity = 0
        self.doublyLinkedList = DoublyLinkedList()
    def get(self, key: int) -> int:
        if self.isKeyExist(key):
            node = self.hashmap[key]
            self.doublyLinkedList.RemoveNode(node)
            self.doublyLinkedList.AddToFront(node)
            return node.value
        return -1
    def isFull(self):
        return self.currentCapacity > self.capacity
    def isKeyExist(self,key):
        return key in self.hashmap
    def put(self, key: int, value: int) -> None:
        if self.isKeyExist(key):
            node = self.hashmap[key]
            node.value = value
            self.doublyLinkedList.RemoveNode(node)
            self.doublyLinkedList.AddToFront(node)
        else:
            node = Node(key,value)
            self.doublyLinkedList.AddToFront(node)
            self.hashmap[key] = node
            self.currentCapacity += 1
            if self.isFull():
                lruNode = self.doublyLinkedList.RemoveFromEnd()
                self.currentCapacity -= 1
                del self.hashmap[lruNode.key]
        
