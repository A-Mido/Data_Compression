
class HeapNode():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

        def __lessthan__(self, other):
            return self.freq < other.freq

        def __equal__(self, other):
            if (other == None):
                return False
            if (not isinstance(other, HeapNode)):
                return False
            return self.freq == other.freq
            
