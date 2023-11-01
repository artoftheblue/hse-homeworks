class InstanceSemaphore(type):
    __instance_dict__ = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance_dict__:
            cls.__instance_dict__[cls] = 0
        
        max_count = getattr(cls, '__max_instance_count__')
        if cls.__instance_dict__[cls] >= max_count:
            raise TypeError

        instance = super().__call__(*args, **kwargs)
        cls.__instance_dict__[cls] += 1
        return instance

class A(metaclass=InstanceSemaphore): 
    __max_instance_count__ = 2 
    
    def __init__(self, *args):
        pass

class B(metaclass=InstanceSemaphore): 
    __max_instance_count__ = 1
    
    def __init__(self, *args):
        pass

print(dir(A), dir(B))
a_one = A('one') 
a_two = A('two') 
b_one = B('one')
try:
    a_three = A('three')
except TypeError as e:
    print(e)
