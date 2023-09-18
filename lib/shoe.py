class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size  = size

    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else: 
            print("size must be an integer")

    def get_size(self):
        return self._size
    
    size = property(get_size, set_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")