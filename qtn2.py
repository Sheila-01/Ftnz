#writea a python program to print the even numbers from a given list. 

def Even(*number):                                           #creating a function with multiple arguments
    num = []
    for i in number:                                                    #looping through the numbers
        for i % 2 == 0:                                    #if number when divided by 2 remainder = 0
            num.append(i)
    return num

print("The Even numbers are:", Even(3,5,67,89,90,12,32,44,11)) 
    
