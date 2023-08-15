import copy

list1 = [1, [2, 3]]
list2 = copy.copy(list1)

list2[0] = 10
list2[1].append(4)

print(list1)  # Output: [1, [2, 3, 4]]
print(list2)  # Output: [10, [2, 3, 4]]




list10 = [1, [2, 3]]
list20 = copy.deepcopy(list10)

list20[0] = 10
list20[1].append(4)

print(list10)  # Output: [1, [2, 3]]
print(list20)  # Output: [10, [2, 3, 4]]
