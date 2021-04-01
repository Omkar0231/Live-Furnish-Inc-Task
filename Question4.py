#Question 4
import random
mylist = [1,2,3,4,5,6,7,8,9,0]

def pick_random_number(mylist):
    size = len(mylist)
    while size:
        index = random.randrange(size)
        elem = mylist[index]
        mylist.append(mylist.pop(index))
        size = size - 1
        print(elem)
        
pick_random_number(mylist)
print(mylist)
