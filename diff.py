def big_diff(array):
    print(array)
    min = array[0]
    max = array[0]
    for no in array:
        if no < min:
            min = no
        elif no > max:
            max = no
    diff=max-min
    return print(diff)


big_diff([10, 3, 5, 6])
big_diff([7, 2, 10, 9])
big_diff([2, 10, 7, 2])