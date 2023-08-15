def any_duplicates(square):
    # ваше решение
    sort_square = [j for i in square for j in i]
    return sorted(sort_square) != [1,2,3,4,5,6,7,8,9]
print(any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]])) 