class Bucket:
    
    def __init__(self):
        self.bucket = []

    def check(self, hash_key):
        for b in self.bucket:
            if hash_key == b:
                return True
        return False

    def remove(self, hash_key):
        for i, b in enumerate(self.bucket):
            if hash_key == b:
                del self.bucket[i]

    def change(self, hash_key):
        
        exists = False

        for i, b in enumerate(self.bucket):
            if hash_key == b:
                exists = True
                self.bucket[i] = hash_key
                break

        if not exists:
            self.bucket.append(hash_key)

class MyHashSet:

    def __init__(self):
        self.key_space = 4196
        self.hash_table = []

        for _ in range(0, self.key_space):
            self.hash_table.append(Bucket())

    def remove(self, remove):
        hash = self.calculate_hash(remove)
        self.hash_table[hash].remove(remove)

    def add(self, add):
        hash = self.calculate_hash(add)
        self.hash_table[hash].change(add)

    def contains(self, key):
        hash = self.calculate_hash(key)
        return self.hash_table[hash].check(key)

    def calculate_hash(self, key):
        return key % self.key_space
