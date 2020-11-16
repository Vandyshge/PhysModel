from constants import *
from random import randint
import numpy as np


def Maxvellv(v):
    return (m0 / (2 * np.pi * k * T)) ** (3 / 2) * np.exp(- m0 * v ** 2 / (2 * k * T))

def Maxvellv_i(v_m, m):
    flag = 0
    while flag == 0:
        v_i = v_m[randint(0, len(v_m) - 1)]
        m_i = m[randint(0, len(m) - 1)]
        if Maxvellv(v_i) >= m_i:
            flag += 1
    return v_i

def Maxvell_v2(n1=1000, n2=1000):
    m_max = (m0 / (2 * np.pi * k * T)) ** (3 / 2)
    v_max = (8 * k * T / m0) ** 0.5
    dv = 2 * v_max / n1
    dm = m_max / n2
    v_m = np.arange(-v_max, v_max + dv, dv)
    m = np.arange(0, m_max + dm, dm) 
    v = []
    for i in range(N):
        v_i = []
        for j in range(3):
            v_i.append(Maxvellv_i(v_m, m))
        v.append(v_i)
    return np.array(v)

def socm(v):
    return v - np.array([np.mean(v, axis=0) for i in range(N)])

if __name__ == '__main__':
    # print(socm(Maxvell_v2()))
    pass