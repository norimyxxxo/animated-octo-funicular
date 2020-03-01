import math
lst = [float(a) for a in input().split(',')]
print(lst)
if lst[6] == 1:
    n = (lst[0] * lst[0] - lst[2] * lst[2]) / (lst[3] * lst[3] * lst[0] * lst[0] - lst[1] * lst[1] * lst[2] * lst[2])
    m = (1 - n * lst[1] * lst[1]) / (lst[0] * lst[0])
    print("a = ", math.sqrt(1/m), "b = ", math.sqrt(1/n))
elif lst[6] == 2:
    n = (lst[0] * lst[0] - lst[2] * lst[2]) / (lst[1] * lst[1] * lst[2] * lst[2] - lst[3] * lst[3] * lst[0] * lst[0])
    m = (1 + n * lst[1] * lst[1]) / (lst[0] * lst[0])
    print("a = ", math.sqrt(1/m), "b = ", math.sqrt(1/n))
elif lst[6] == 3:
    if (lst[0] != 0 and lst[1] != 0):
        print("p = ", lst[1] * lst[1] / (2 * lst[0]))
    else:
        print("p = ", lst[3] * lst[3] / (2 * lst[2]))
       
