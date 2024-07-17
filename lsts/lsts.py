class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append((key, value))

    def get(self, key):
        address = self._hash(key)
        if self.data[address]:
            for kvp in self.data[address]:
                if kvp[0] == key:
                    return kvp[1]
        return None

# Example usage
myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))  # Output: 10000
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))  # Output: 9
