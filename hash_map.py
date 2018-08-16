class MyHashMap:
    class Node:
        def __init__(self, key=-1, val=-1):
            self.val = val
            self.key = key
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 500000
        self.table = [self.Node()] * self.size
        
    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        pos = key%self.size
        p = self.table[pos]
        while p.next:
            p = p.next
            if key == p.key:
                p.val = value
                print('the key is existing, and covered in pos: ' + str(pos))
                return 
        p.next = self.Node(key, value)
        print('the key does not exist and is built in pos: ' + str(pos))
        
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        pos = key%self.size
        p = self.table[pos]
        while p.next:
            p = p.next
            if p.key == key:
                print('successfully get the value in pos: ' + str(pos))
                return p.val
        print('the key does not exist!')
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        pos = key%self.size
        p = self.table[pos]
        while p.next:
            q = p
            p = p.next
            if p.key == key:
                q.next = p.next
                print('the key is removed!')
                return
        print('the key does not exist!')

hashMap = MyHashMap()
hashMap.put(1, 1)         
hashMap.put(2, 2)       
hashMap.get(1)           
hashMap.get(3)            
hashMap.put(2, 1)        
hashMap.get(2);            
hashMap.remove(2)         
hashMap.get(2);            