from collections import OrderedDict

class Cache:
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def fetch(self, address):
        if address in self.cache:
            self.cache.move_to_end(address)
            return self.cache[address]
        return None

    def store(self, address, data):
        if len(self.cache) >= self.size:
            self.cache.popitem(last=False)
        self.cache[address] = data


class MultiLevelCache:
    def __init__(self, l1_size, l2_size):
        self.l1 = Cache(l1_size)
        self.l2 = Cache(l2_size)

    def fetch(self, address):
        data = self.l1.fetch(address)
        if data is None:
            data = self.l2.fetch(address)
            if data:
                self.l1.store(address, data)
        return data

    def store(self, address, data):
        self.l1.store(address, data)
        self.l2.store(address, data)
