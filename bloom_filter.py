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
        places = len(str(bits))
        hash_size = len(str(abs(hash(string))))
        spots_per_hash = hash_size//places
        hashes_needed = 1 + self.hash_iterations // spots_per_hash
        indices = []
        for loop in range(hashes_needed):
            seed = string + str(loop)
            hash_string = str(abs(hash(seed)))
            for spot in range(spots_per_hash):
                index_str = hash_string[spot*places:(spot+1)*places]
                indices.append(int(index_str)%bits)
        return indices
