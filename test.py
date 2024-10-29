from functools import cmp_to_key
import heapq

class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value})"
    def __str__(self):
        return 'sss'
a=MyClass(10)
print(a)