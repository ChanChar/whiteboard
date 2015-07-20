class HashSet:
    def __init__(self):
        self.buckets = [[]] * 8
        self.count = 0

    def __contains__(self, val):
        bucket = self.__find_bucket(val)
        return val in bucket

    def insert(self, val):
        if val in self:
            return False

        if self.count + 1 // len(self.buckets) > 1:
            self.__resize()

        bucket = self.__find_bucket(val)
        bucket.append(val)
        self.count += 1

    def remove(self, val):
        if val not in self:
            raise KeyError('Value not found')

        bucket = self.__find_bucket(val)
        bucket.delete(val)
        self.count -= 1

    def __find_bucket(self, val, buckets=None):
        if buckets is None:
            buckets = self.buckets
        return buckets[self.__hashify(val) % len(buckets)]

    def __hashify(self, val):
        return hash(val)

    def __resize(self):
        new_buckets = [[]] * len(self.buckets) * 2

        for bucket in self.buckets:
            for item in bucket:
                new_bucket = self.__find_bucket(item, new_buckets)
                new_bucket.append(val)

        self.buckets = new_buckets
