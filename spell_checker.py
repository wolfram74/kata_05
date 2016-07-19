from bloom_filter import BloomFilter

class SpellChecker():
    def __init__(self):
        self.dictionary = BloomFilter()
        dictionary = open('/usr/share/dict/words', 'r')
        for word in dictionary:
            self.dictionary.add(word.strip())

    def valid(self, string):
        return self.dictionary.includes(string)


