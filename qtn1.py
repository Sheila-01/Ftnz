#write a python function that takes a list and returns a new list with unique elements of the first list. Dont use list methods

def myList(*list):                                  #creating a function with multiple arguments
    # list = [2,4,5,6,7,3,7,2,4,1,2]
    newlist = set(myList)
    return newlist
myList(2,4,5,6,7,3,7,2,4,1,2)
print(newlist)
