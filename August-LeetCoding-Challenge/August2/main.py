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
