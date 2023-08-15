n = int(input())
# for i in range(n,1,-1):
#     x = str(chr(96+i))
#     a = i
#     print(x)
#     for j in range(i-1):
#         x1 = chr(95+n-j) + '-' + x + '-' + chr(95+n-j)
        
#     x1 = '-'*range(x1)
#     print(x1)
a = list()

for i in range(n,0,-1):
    b = str()
    for j in range(1,i):
        b+=chr(96+j)
    print(b)
    b1 = chr(96+i) + b[::-1]
    print(b1)