class ExtendedList(list):
    def __init__(self, array):
        super().__init__(array)
        self._size = len(self)

    def insert(self, index, item):
        super().insert(index, item)
        self._size += 1

    def append(self, item):
        super().append(item)
        self._size += 1

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            temparray = []
            for item in other:
                temp += 1
                temparray.append(item)
                
            super().extend(temparray)
            self._size += temp
            
    @property
    def reversed(self):
        return self[::-1]

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, value):
        self[-1] = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value > self.size:
            self += [None] * (value - self.size)
            self._size = value
        if value < self.size:
            self[:] = self[:value]
            self._size = value
