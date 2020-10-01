def selectsort(alist):
    for i in range(0,len(alist)):
        min = alist[i]
        minpos = i
        for x in range(i,len(alist)):
            if min > alist[x]:
                min = alist[x]
                minpos = x
        alist[minpos],alist[i] = alist[i], alist[minpos]
    return alist

print(selectsort([4,2,1,0]))

selectsort([7,2,6,1,4,8,6,5,7,3,9])