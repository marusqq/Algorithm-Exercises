class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_count = 7000
        self.buckets = []
        for _ in range(0, self.bucket_count):
            self.buckets.append(Bucket())

    def print_hash_set(self):
        for bucket in self.buckets:
            if bucket.get_value():
                print('Bucket =', bucket.get_value())
        return

    def add(self, key: int) -> None:
        for bucket in self.buckets:
            if bucket.get_value() == []:
                bucket.add(key)
                return
        return

    def remove(self, key: int) -> None:
        for bucket in self.buckets:
            if bucket.get_value() == key:
                bucket.remove()
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """

        for bucket in self.buckets:
            if bucket.get_value() == key:
                return True

        return False
        
class Bucket:

    def __init__(self):
        self.bucket = []
        return

    def add(self, key):
        self.bucket = key
        return

    def get_value(self):
        return self.bucket

    def remove(self):
        self.bucket = []
        return




