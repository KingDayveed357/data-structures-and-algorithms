class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key:int):
        return key % self.size

    def add(self, key:int):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key:int):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key:int):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        return key in bucket