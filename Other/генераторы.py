import random
def randoms(min, max, n):
    for _ in range(n):
        yield random.randint(min, max)

random_sequest = randoms(1,10,1000000007)

for i in random_sequest:
    print(i)

lists = [1,2,3,4,5,6,7,8,9]
list_scr = [i for i in lists]
print