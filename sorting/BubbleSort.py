import numpy as np 

lst_non_repetative = list(np.random.choice(100, 10))
print("values insde a list are : ",lst_non_repetative)

def BubbleSort(lst):
    for x in range(len(lst)-1):
        for y in range(len(lst)-1):
            if lst[y]<lst[y+1]:
                lst[y],lst[y+1]=lst[y+1],lst[y]
    print(lst)
    return lst
BubbleSort(lst_non_repetative)