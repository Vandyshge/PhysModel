from constants import *
from location import *
from output import *
from ep import *
import numpy as np


    
def acceleration(loc):
    a = np.zeros((N, 3))
    for n in range(N):
        x, y, z = loc[n][0][1], loc[n][1][1], loc[n][2][1]
        for i in range(n + 1, N):
            if i != n:
                x_i, y_i, z_i = loc_fr(x, y, z, loc[i][0][1], loc[i][1][1], loc[i][2][1])
                lenth = l(x, y, z, x_i, y_i, z_i)
                a_i =  (- 24 * ep * sigma**6 * (lenth[0]**(-7) - 2 * sigma**6 * lenth[0]**(-13)) / m0) * lenth[1] / lenth[0]
                a[n] += a_i
                a[i] += - a_i
    return a

def step(epoch, loc, v):
    # global a1
    # a1 = a
    a = acceleration(loc)
    # print(a[0, 0])
    # print(a == a1)
    # print(np.shape(loc))
    # print(np.shape(v))
    # print(loc)
    # print()
    # print(loc[:, :, 1])
    loc[:, :, 0] = loc[:, :, 1] + v * dt + a * dt**2 / 2
    v += a * dt
    # print(loc, v, sep='\n')
    # print()
    loc = np.array([[loc_side1(i[0]) for i in l] for l in loc])
    # print(loc[0, 0, 1])
    # print(loc, v, sep='\n')
    return loc, v

if __name__ == '__main__':
    pass