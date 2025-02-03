def IntPolSearch(list, x):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:

        # Find the mid point
        mid = idx0 + int(((float(idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0])))

        # Compare the value at mid point with search value
        if list[mid] == x:
            found = True  
            return found

        if list[mid] < x:
            idx0 = mid + 1
    return found

list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print (IntPolSearch(list, 30))
print (IntPolSearch(list, 110))