#An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments

#To define the function with the key word argument - The result will be the dictionary type of input
def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))

#To print the result is 9
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=9))