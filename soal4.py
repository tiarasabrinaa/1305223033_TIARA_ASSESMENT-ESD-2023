def duplikat(array):
    set_array = set()
    for elemen in array:
        if elemen in set_array:
            return True
        set_array.add(elemen)
    return False

array = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18,  20, 17, 19]
print(array, ":", duplikat(array))