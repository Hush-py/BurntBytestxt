import numpy as np
def lists(l1,l2):
    l11=l1[ : :-1]
    l22=l2[ : :-1]
    l33=[ ]
    arr1=np.array(l11)
    arr2=np.array(l22)
    arr3=arr1+arr2
    for i in arr3:
        l33.append(i)
        l3=l33[ : : -1] 
        return l3
lists(l1,l2) 
