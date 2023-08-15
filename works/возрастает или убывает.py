def check_sequence(lst = list):
    set_lst = list(set(lst))
    if set_lst==lst:
        return 1
    elif set_lst == list(reversed(lst)):
        return -1
    return 0

check_sequence([1, 2, 3])
check_sequence([3, 2, 1]) 
check_sequence([1, 2, 1]) 
check_sequence([1, 1, 2])