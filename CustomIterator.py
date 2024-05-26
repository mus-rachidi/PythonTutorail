class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
    
# Creating an instance of the custom iterator
my_iterable = MyIterator(1, 5)

# Implicit Call: Typically, you don't call __iter__ and __next__ directly. 
#                Instead, they are used implicitly by Python when you use a loop or other iteration context.

# for element in my_iterable:
#     print(element)  # This implicitly calls __iter__ and __next__

# Explicit Call: You can explicitly call these methods if you need finer control over the iteration process.

iterator = my_iterable.__iter__()  # Explicitly calling __iter__
print(iterator.__next__())  # Explicitly calling __next__
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
