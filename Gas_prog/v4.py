import random
# from scipy.constants import k
from scipy.constants import pi
# from scipy.constants import e
import numpy as np
import time
import os

random.seed()
    
N = 2


k = 1
sigma = 1
ep = 1
T = 1
m0 = 1
side = 6
side_p = side / 2
 
time = 0.001
period = 5
epoches = int(period / time)



def Maxvellv(v, T, mo):
    return (m0 / (2 * pi * k * T)) ** (3 / 2) * np.exp(- m0 * v ** 2 / (2 * k * T))

def Maxvellv_i(T, m0, v_m, m):
    flag = 0
    while flag == 0:
        v_i = v_m[random.randint(0, len(v_m) - 1)]
        m_i = m[random.randint(0, len(m) - 1)]
        if Maxvellv(v_i, T, m0) >= m_i:
            flag += 1
    return v_i

def Maxvell_v2(T, m0, n1, n2, N):
    m_max = (m0 / (2 * pi * k * T)) ** (3 / 2)
    v_max = (8 * k * T / m0) ** 0.5
    dv = 2 * v_max / n1
    dm = m_max / n2
    v_m = np.arange(-v_max, v_max + dv, dv)
    m = np.arange(0, m_max + dm, dm) 
    v = []
    for i in range(N):
        v_i = []
        for j in range(3):
            v_i.append(Maxvellv_i(T, m0, v_m, m))
        v.append(v_i)
    return v

def socm(v, N):
    v_x = np.zeros(N)
    v_y = np.zeros(N)
    v_z = np.zeros(N)
    
    for i in range(N):
        v_x[i] += v[i][0]
        v_y[i] += v[i][1]
        v_z[i] += v[i][2]
        
    v_x0 = np.mean(v_x)
    v_x -= v_x0 * np.ones(N)

    v_y0 = np.mean(v_y)
    v_y -= v_y0 * np.ones(N)
    
    v_z0 = np.mean(v_z)
    v_z -= v_z0 * np.ones(N)
    
    for i in range(N):
        v[i][0] = v_x[i]
        v[i][1] = v_y[i]
        v[i][2] = v_z[i]
    
    return v


def L(x, y, z, x_i, y_i, z_i):
    lenth_v = [x - x_i, y - y_i, z - z_i]
    lenth = (lenth_v[0] ** 2 + lenth_v[1] ** 2 + lenth_v[2] ** 2) ** (1 / 2)
    return (lenth, lenth_v)


def LocationIn(N, epoches):
    history_x = [[0 for i in range(epoches + 1)] for i in range(N)]
    history_y = [[0 for i in range(epoches + 1)] for i in range(N)]
    history_z = [[0 for i in range(epoches + 1)] for i in range(N)]


#     for i in range(N):
#         history_x[i][0] = 10 ** -3 * random.randint(-int(side_p * 10 ** 3), int(side_p * 10 ** 3))
#         history_y[i][0] = 10 ** -3 * random.randint(-int(side_p * 10 ** 3), int(side_p * 10 ** 3))
#         history_z[i][0] = 10 ** -3 * random.randint(-int(side_p * 10 ** 3), int(side_p * 10 ** 3))

#     history_x[0][0] = 2.0
#     history_y[0][0] = 2.0
#     history_z[0][0] = 2.0
#     history_x[1][0] = -2.0
#     history_y[1][0] = -2.0
#     history_z[1][0] = -2.0
    
    history_x[0][0] = 0
    history_x[1][0] = 2.7
    
    
    return (history_x, history_y, history_z)

def Energy(epoch):
    E_p = 0
    E_k = 0
    
    for n in range(N):
        x, y, z = history_x[n][epoch], history_y[n][epoch], history_z[n][epoch]
        for i in range(N):
            if i != n:
                x_i, y_i, z_i = history_x[i][epoch], history_y[i][epoch], history_z[i][epoch]
                print(x, y, z, x_i, y_i, z_i)
                if abs(x - (x_i + side)) <= side_p:
                    x_i = x_i + side
                elif abs(x - (x_i - side)) <= side_p:
                    x_i = x_i - side

                if abs(y - (y_i + side)) <= side_p:
                    y_i = y_i + side
                elif abs(y - (y_i - side)) <= side_p:
                    y_i = y_i - side

                if abs(z - (z_i + side)) <= side_p:
                    z_i = z_i + side
                elif abs(z - (z_i - side)) <= side_p:
                    z_i = z_i - side
                print(x, y, z, x_i, y_i, z_i)

                lenth = L(x, y, z, x_i, y_i, z_i)
                
#                 lenth = sorted([L(x, y, z, x_i, y_i, z_i), L(x, y, z, x_i + side, y_i, z_i), L(x, y, z, x_i - side, y_i, z_i), L(x, y, z, x_i, y_i + side, z_i), L(x, y, z, x_i, y_i - side, z_i), L(x, y, z, x_i, y_i, z_i + side), L(x, y, z, x_i, y_i, z_i - side)], key=lambda x: x[0])[0]
                if lenth[0] == 0:
                    print(lenth[1], n, i)
                E_p += 4 * ep * ((sigma / lenth[0]) ** 12 - (sigma / lenth[0]) ** 6)
            else:
                E_k += m0 / 2 * (v[i][0]**2 + v[i][1]**2 + v[i][2]**2)
    
    return E_k + E_p / 2



def Momentum(v):
    p_x = 0
    p_y = 0
    p_z = 0
    
    for i in range(N):
        p_x += v[i][0]
        p_y += v[i][1]
        p_z += v[i][2]
    
    p_x *= m0
    p_y *= m0
    p_z *= m0
    
    return [p_x, p_y, p_z]


def EnegyMomentumIn(epoches):
    history_E = [0 for i in range(epoches + 1)]
    history_dEE = [0 for i in range(epoches)]
    history_p = [[0 for i in range(epoches + 1)] for i in range(3)]
    
    history_E[0] = Energy(0)
    p_i = Momentum(v)
    history_p[0][0] = p_i[0]
    history_p[1][0] = p_i[1]
    history_p[2][0] = p_i[2]

    os.mkdir('C:/Users/Xiaomi/PhysModel/Gas/forovito')
    
    out = open('C:/Users/Xiaomi/PhysModel/Gas/forovito/E.txt', 'a')
    out.write("{} {}\n".format(0, history_E[0]))
    out.close()
    
    out = open('C:/Users/Xiaomi/PhysModel/Gas/forovito/p.txt', 'a')
    out.write("{} {} {} {}\n".format(0, history_p[0][0], history_p[1][0], history_p[2][0]))
    out.close()
    
#     print(len((history_E, history_p, history_dEE)))
    return (history_E, history_p, history_dEE)
    

def EnegyMomentum(epoch):
    history_E[epoch] = Energy(epoch)
    p_i = Momentum(v)
    history_p[0][epoch] = p_i[0]
    history_p[1][epoch] = p_i[1]
    history_p[2][epoch] = p_i[2]
    
    history_dEE[epoch - 1] = history_E[epoch] - history_E[epoch - 1] / history_E[epoch]
    
    out = open('C:/Users/Xiaomi/PhysModel/Gas/forovito/E.txt', 'a')
    out.write("{} {}\n".format(epoch, history_E[epoch]))
    out.close()
    
    out = open('C:/Users/Xiaomi/PhysModel/Gas/forovito/p.txt', 'a')
    out.write("{} {} {} {}\n".format(epoch, history_p[0][epoch], history_p[1][epoch], history_p[2][epoch]))
    out.close()

def forovito(epoch, N):
    out = open('C:/Users/Xiaomi/PhysModel/Gas/forovito/{}.xyz'.format(epoch), 'a')
    out.write("{}\n".format(N + 8))
    out.write("Lattice=\"1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0\" Properties=pos:R:3:velo:R:3 Time=0\n")
    out.write("{} {} {} {} {} {}\n".format(side_p, side_p, side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(side_p, side_p, -side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(side_p, -side_p, -side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(side_p, -side_p, side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(-side_p, -side_p, -side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(-side_p, -side_p, side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(-side_p, side_p, -side_p, 0, 0, 0))
    out.write("{} {} {} {} {} {}\n".format(-side_p, side_p, side_p, 0, 0, 0))
    for i in range(N):
        out.write("{} {} {} {} {} {}\n".format(history_x[i][epoch], history_y[i][epoch], history_z[i][epoch], v[i][0], v[i][1], v[i][2]))
    out.close()
    
    
def acceleration(n, epoch):
    a = [0, 0, 0]
    x, y, z = history_x[n][epoch - 1], history_y[n][epoch - 1], history_z[n][epoch - 1]
    for i in range(N):
        if i != n:
            x_i, y_i, z_i = history_x[i][epoch - 1], history_y[i][epoch - 1], history_z[i][epoch - 1]
 
            
            if abs(x - (x_i + side)) <= side_p:
                x_i = x_i + side
                
            elif abs(x - (x_i - side)) <= side_p:
                x_i = x_i - side
                
            if abs(y - (y_i + side)) <= side_p:
                y_i = y_i + side
            elif abs(y - (y_i - side)) <= side_p:
                y_i = y_i - side
                
            if abs(z - (z_i + side)) <= side_p:
                z_i = z_i + side
            elif abs(z - (z_i - side)) <= side_p:
                z_i = z_i - side
            
            lenth = L(x, y, z, x_i, y_i, z_i)
            
            
            
#             vari_x0 = [0, side, - side]
#             vari_y0 = [0, side, - side]
#             vari_z0 = [0, side, - side]
#             for vari_x in vari_x0:
#                 for vari_y in vari_y0:
#                     for vari_z in vari_z0:
#                         if (x - (x_i + vari_x)) ** 100 + (y - (y_i + vari_y)) ** 100 + (z - (z_i + vari_z)) ** 100 <= side / 2:
#                             lenth = L(x, y, z, x_i + vari_x, y_i + vari_y, z_i + vari_z)
                
            
    
#             lenth = sorted([L(x, y, z, x_i, y_i, z_i), L(x, y, z, x_i + side, y_i, z_i), L(x, y, z, x_i - side, y_i, z_i), L(x, y, z, x_i, y_i + side, z_i), L(x, y, z, x_i, y_i - side, z_i), L(x, y, z, x_i, y_i, z_i + side), L(x, y, z, x_i, y_i, z_i - side)], key=lambda x: x[0])[0]
            # lenth = L(x, y, z, x_i, y_i, z_i)

#             print(lenth, lenth[0])
            a_i =  - 24 * ep * sigma ** 6 * (lenth[0] ** -7 - 2 * sigma ** 6 * lenth[0] ** -13) / m0
            a_i_x = a_i * lenth[1][0] / lenth[0]
            a_i_y = a_i * lenth[1][1] / lenth[0]
            a_i_z = a_i * lenth[1][2] / lenth[0]
            a[0] += a_i_x
            a[1] += a_i_y
            a[2] += a_i_z
       
    return a

def step(epoch):
#     start_time = time.clock()
    for n in range(N):
        x, y, z = history_x[n][epoch - 1], history_y[n][epoch - 1], history_z[n][epoch - 1]
 
        a = acceleration(n, epoch)
        # print('1 ---- ', a, x, y, n, i)

#         print(a)
        
        # print('2 ---- ', v, v[n])

        x += v[n][0] * time + a[0] * time ** 2 / 2
        y += v[n][1] * time + a[1] * time ** 2 / 2
        z += v[n][2] * time + a[2] * time ** 2 / 2
        
        
        # print('2 ---- ', v, v[n])
#         print(v)
        v[n][0] += a[0] * time
        v[n][1] += a[1] * time
        v[n][2] += a[2] * time
#         print(v)
#         print()
        
        if abs(x) <= side_p:
            history_x[n][epoch] = x
            print('1x -- ', epoch, n, x, history_x[n][epoch], v[n][0])
        elif x < - side_p:
            history_x[n][epoch] = - (abs(x) % side_p) + side_p
            print('2x -- ', epoch, n, x, history_x[n][epoch], v[n][0])
        elif x > side_p:
            history_x[n][epoch] = x % side_p - side_p
            print('3x -- ', epoch, n, x, history_x[n][epoch], v[n][0])

        if abs(y) <= side_p:
            history_y[n][epoch] = y
#             print('1y -- ', epoch, n, history_y[n][epoch])
        elif y < side_p:
            history_y[n][epoch] = - (abs(y) % side_p) + side_p
#             print('2y -- ', epoch, n, y, history_y[n][epoch])
        elif y > side_p:
            history_y[n][epoch] = y % side_p - side_p
#             print('3y -- ', epoch, n, y, history_y[n][epoch])

        if abs(z) <= side_p:
            history_z[n][epoch] = z
#             print('1z -- ', epoch, n, history_z[n][epoch])
        elif z < side_p:
            history_z[n][epoch] = - (abs(z) % side_p) + side_p
#             print('2z -- ', epoch, n, z, history_z[n][epoch])
        elif z > side_p:
            history_z[n][epoch] = z % side_p - side_p
#             print('3z -- ', epoch, n, z, history_z[n][epoch])
        
#         print(history_x[1][:2], history_y[1][:2], history_z[1][:2])
#         print(history_x[2][:2], history_y[2][:2], history_z[2][:2])
    
    
    EnegyMomentum(epoch)

    forovito(epoch, N)
    
#     print("{} ---- {}".format(epoch, time.clock() - start_time))

        # print('3 ---- ', history_x, history_y, v, sep='\n')
        # print()

        
# start program
        
# v = Maxvell_v2(T, m0, 1000, 1000, N)
# # print(v)
# v = socm(v, N)
# # print(v)

v = [[1, 0, 0], [50, 0, 0]]

history_x, history_y, history_z = LocationIn(N, epoches)

history_E, history_p, history_dEE = EnegyMomentumIn(epoches)

forovito(0, N)

# print(history_E, history_p, v)


for i in range(1, epoches + 1, 1):
#     print(v)
    step(i)
#     print(v)
#     print()
    print(i)

# print(history_x, history_y, v, sep='\n')