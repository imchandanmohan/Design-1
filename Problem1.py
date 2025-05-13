'''
I used an array to store values, and before adding a new value to the hashset variable, 
I checked if it already existed; while removing, I iterated through the array, compared 
each element with the key, and if found, I popped the element and returned immediately to 
avoid index errors caused by the list shrinking.
'''

class MyHashSet(object):

    def __init__(self):
        self.hashset = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.hashset:
            self.hashset.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """

        for i in range(0,len(self.hashset)):
            if key == self.hashset[i]:
                popped_item = self.hashset.pop(i)
                return
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.hashset:
            return True
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

hs = MyHashSet()
key = 3
hs.add(1)
hs.add(2)
hs.add(3)
hs.add(4)
hs.add(5)
hs.remove(3)
hs.contains(4)
hs.contains(3)

