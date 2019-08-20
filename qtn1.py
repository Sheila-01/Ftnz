#write a python function that takes a list and returns a new list with unique elements of the first list. Dont use list methods
def myList(list):                                  #creating a function 
    newlist = []
    for i in list:
        if i not in newlist:
            i.append(newlist)
    return i
print(myList(2,6,7,8,90,23,45))
