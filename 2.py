import numpy as np
import math
def ro2(n, n2):
    res = 0
    for i in range(min(n, n2, k)):
        res += (ts[n - k + i][0] - ts[n2 - k + i][0]) ** 2 + (ts[n - k + i][1] - ts[n2 - k + i][1]) ** 2
    return res

N = 2000
a = 2
b = 1
result = 0
ts = []
delta_t = 0.01
ts = [[a * math.cos(i * delta_t), b * math.sin(i * delta_t)] for i in range(N)]
for k in range(10, 15):
    l = 1 / 128
    ro = []
    ro = [ro2(n,n2) for n in range(k, N) for n2 in range(k, N)]
    while l >= 1 / 1024:
        d = 0
        for n in range(len(ro)):
            result += np.heaviside(l**2 - ro[n], 0)
        result /= N**2
        d = math.log(result) / math.log(l)
        print('k =', round(k, 6), 'l =', round(l,6), 'c =', round(result,6), 'd =', round(d,6))
        print()
        l /= 2
