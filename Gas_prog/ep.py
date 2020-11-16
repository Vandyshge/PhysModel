from constants import *
from location import *


def energy(loc, v):
    E_p = 0
    E_k = 0
    for n in range(N):
        x, y, z = loc[n][0][1], loc[n][1][1], loc[n][2][1]
        for i in range(n + 1, N):
            E_p += e_p_i(x, y, z, loc[i][0][1], loc[i][1][1], loc[i][2][1])
        E_k += m0 / 2 * (v[n][0]**2 + v[n][1]**2 + v[n][2]**2)
    return E_k + E_p

def e_p_i(x, y, z, x_i, y_i, z_i):
	x_i, y_i, z_i = loc_fr(x, y, z, x_i, y_i, z_i)
	lenth = l(x, y, z, x_i, y_i, z_i)[0]
	return 4 * ep * ((sigma / lenth)**12 - (sigma / lenth)**6)

def momentum(v):  
    return m0 * np.sum(v, axis=0)