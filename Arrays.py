#Create an array
import numpy as np
ran_list = [1, 4, 7, 2, 9, 12, 56]
array = np.array(ran_list)

def size(array):
    return (len(array))

def is_empty(array):
    if size(array) == 0:
        return True
    else:
        return False

def at_index(index):
    return array[index]

# new_array = np.append(array, 7)
# print (new_array)









