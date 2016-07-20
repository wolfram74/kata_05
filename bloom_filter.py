class BloomFilter():
    def __init__(self):
        size = 10**6
        self.bit_map = [0 for i in range(10*size)]
        self.hash_iterations = 5
        self.items = 0

    def includes(self, string):
        check = self.hash_indices(string)
        boolean = True
        for index in check:
            boolean = (boolean and bool(self.bit_map[index]))
        return boolean

    def add(self, string):
        bins = self.hash_indices(string)
        for index in bins:
            self.bit_map[index] = 1
        self.items += 1
        return True

    def hash_indices(self, string):
        bits = len(self.bit_map)
        indices = []
        for salt in range(self.hash_iterations):
            seed = string + str(salt)
            indices.append( hash(seed) % bits )
        return indices
