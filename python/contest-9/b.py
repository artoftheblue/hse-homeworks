import sys

class CommonProperties:
    def __init__(self, data):
        self._data = data
        self.size = len(data)
        self.max_value = None
        self.min_value = None


class DictProperties:
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        temp_keys = [key for key in self.data]
        parsed = temp_keys + [self.data[key] for key in self.data]
        try:
            self.max_value = max(parsed)
            self.min_value = min(parsed)
        except TypeError:
            self.max_value = max(temp_keys)
            self.min_value = min(temp_keys)
        
        self.size = len(value)
        

class CustomList(CommonProperties):
    def __init__(self, data):
        super().__init__(data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.max_value = max(value)
        self.min_value = min(value)
        self.size = len(value)

    def __str__(self):
        return f"My CustomList data {self._data}"
    

class CustomDict(CommonProperties, DictProperties):
    def __init__(self, data):
        super().__init__(data)
        self.data = data

    def __str__(self):
        return f"My CustomDict data {self._data}"




my_dict = CustomDict({1: 2, 2: 3, 3: 4})
print(my_dict)
my_dict.data = {1: 100, 2: 200}
print(my_dict)
print(isinstance(my_dict, CommonProperties))
print(isinstance(my_dict, DictProperties))
print(isinstance(my_dict, dict))
print(my_dict.size)
print(my_dict.min_value)
print(my_dict.max_value)
