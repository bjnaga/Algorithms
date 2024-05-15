import numpy as np

lst_non_repetatice = list(np.random.choice(100, 10))
print(lst_non_repetatice[0])
def selection_sort(lst):
    for x in range(len(lst)):
        low = x
        print("low value is ",low)
        print("adding ",lst[x]," to low in index ",x)
        for y in range(x+1,len(lst)):
            if lst[low] > lst[y]:
                low = y
        temp = lst[x]
        print("swapping ",lst[x], " with ",lst[low])
        lst[x]=lst[low]
        lst[low] = temp
        print(lst)
        print("\n")
    print("final sorted list is :",lst)
    return lst


print("Initial list is equal to : ",lst_non_repetatice)
selection_sort(lst_non_repetatice)
