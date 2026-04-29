# l = [1,2,3,21,5,6,21,34,5]
# arr = list(set(l))
# arr.sort()
# print(arr[2])


class Cal:
    
    def __init__(self, value):
        self.value = value
    
    def add(self):
        return f"Addition will be : {self.value * 2}"
    
cls = Cal(10)
result = cls.add()
print(result)