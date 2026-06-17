class HashTable():
    def __init__(self):
        self.collection = {}
    def hash(self, s):
        return sum([ord(i) for i in s])
    def add(self, key, value):
        hashed=self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed]={}
        self.collection[hashed][key]=value
    def remove(self, key):
        hashed=self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]
        else:
            pass
    def lookup(self, key):
        hashed=self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]
        else:
            return None

