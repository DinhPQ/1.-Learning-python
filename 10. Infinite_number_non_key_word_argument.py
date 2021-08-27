#An *args parameter allows the  function to be called with an arbitrary number of non-keyword argument

#The term *args define the indifinite number of numbers as argument
def defi(*args):
    return sum(args) / len(args)

#Return the indefinite number that contain string value by return it in uppper case and sorted in alphabet
def defi(*args):
    args = [x.upper() for x in args]
    return sorted(args)