import random
from scipy.constants import k
from scipy.constants import pi
from scipy.constants import e
import numpy as np

random.seed()
    
N = 20
 
sigma = 1
ep = 1
T = 273
m0 = 10 ** -18
side = 1000
side_p = int(side / 2)
 
time = 0.01
epoches = 300

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


    for i in range(N):
        history_x[i][0] = random.randint(-side_p, side_p)
        history_y[i][0] = random.randint(-side_p, side_p)
        history_z[i][0] = random.randint(-side_p, side_p)
    
    return (history_x, history_y, history_z)

def Energy(epoch):
    E_p = 0
    E_k = 0
    
    for n in range(N):
        x, y, z = history_x[n][epoch], history_y[n][epoch], history_z[n][epoch]
        for i in range(N):
            if i != n:
                x_i, y_i, z_i = history_x[i][epoch], history_y[i][epoch], history_z[i][epoch]

                lenth = sorted([L(x, y, z, x_i, y_i, z_i), L(x, y, z, x_i + side, y_i, z_i), L(x, y, z, x_i - side, y_i, z_i), L(x, y, z, x_i, y_i + side, z_i), L(x, y, z, x_i, y_i - side, z_i), L(x, y, z, x_i, y_i, z_i + side), L(x, y, z, x_i, y_i, z_i - side)], key=lambda x: x[0])[0]
                if lenth[0] == 0:
#                     print(lenth[1], n, i)
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
        p_z += v[i][1]
    
    p_x *= m0
    p_y *= m0
    p_z *= m0
    
    return [p_x, p_y, p_z]


def EnegyMomentumIn(epoches):
    history_E = [0 for i in range(epoches + 1)]
    history_p = [[0 for i in range(epoches + 1)] for i in range(3)]
    
    history_E[0] = Enegy(0)
    history_p[0][0] = Momentum(v)[0]
    history_p[1][0] = Momentum(v)[1]
    history_p[2][0] = Momentum(v)[2]

    out = open('C:/0.LaLaLand/0.Физтех/Gas/E.txt', 'a')
    out.write("{} {}".format(0, history_E[0]))
    out.close()
    
    out = open('C:/0.LaLaLand/0.Физтех/Gas/p.txt', 'a')
    out.write("{} {} {} {}".format(0, history_p[0][0], history_p[0][1], history_p[0][2]))
    out.close()
    
    return (history_E, history_p)
    

def EnegyMomentum(epoch):
    history_E[epoch] = Energy(epoch)
    history_p[epoch] = Momentum(v)
    
    out = open('C:/0.LaLaLand/0.Физтех/Gas/E.txt', 'a')
    out.write("{} {}\n".format(epoch, history_E[epoch]))
    out.close()
    
    out = open('C:/0.LaLaLand/0.Физтех/Gas/p.txt', 'a')
    out.write("{} {} {} {}\n".format(epoch, history_p[epoch][0], history_p[epoch][1], history_p[epoch][2]))
    out.close()

def forovito(epoch):
    out = open('C:/0.LaLaLand/0.Физтех/Gas/forovito/{}.xyz'.format(epoch), 'a')
    out.write("4096\n")
    out.write("Lattice=\"1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0\" Properties=pos:R:3:velo:R:3 Time=0\n")
    for i in range(N):
        out.write("{} {} {} {} {} {}\n".format(history_x[i][epoch], history_y[i][epoch], history_z[i][epoch], v[i][0], v[i][1], v[i][2]))
    out.close()


v = Maxvell_v2(T, m0, 1000, 1000, N)
# print(v)
v = socm(v, N)
# print(v)

history_x, history_y, history_z = LocationIn(N, epoches)

history_E, history_p = EnegyMomentumIn(epoches)

forovito(0)

# print(history_E, history_p, v)


def acceleration(n, epoch):
    a = [0, 0, 0]
    x, y, z = history_x[n][epoch - 1], history_y[n][epoch - 1], history_z[n][epoch - 1]
    for i in range(N):
        if i != n:
            x_i, y_i, z_i = history_x[i][epoch - 1], history_y[i][epoch - 1], history_z[i][epoch - 1]
 
            lenth = sorted([L(x, y, z, x_i, y_i, z_i), L(x, y, z, x_i + side, y_i, z_i), L(x, y, z, x_i - side, y_i, z_i), L(x, y, z, x_i, y_i + side, z_i), L(x, y, z, x_i, y_i - side, z_i), L(x, y, z, x_i, y_i, z_i + side), L(x, y, z, x_i, y_i, z_i - side)], key=lambda x: x[0])[0]
            # lenth = L(x, y, z, x_i, y_i, z_i)

            # print(lenth, lenth[0])
            a_i = 24 * ep * sigma ** 6 * (lenth[0] ** -7 - 2 * sigma ** 6 * lenth[0] ** -13) / m0
            a_i_x = a_i * lenth[1][0] / lenth[0]
            a_i_y = a_i * lenth[1][1] / lenth[0]
            a_i_z = a_i * lenth[1][2] / lenth[0]
            a[0] += a_i_x
            a[1] += a_i_y
            a[2] += a_i_z
       
    return a


def step(epoch):
    for n in range(N):
        x, y, z = history_x[n][epoch - 1], history_y[n][epoch - 1], history_z[n][epoch - 1]
 
        a = acceleration(n, epoch)
        # print('1 ---- ', a, x, y, n, i)

        # print('2 ---- ', v, v[n])

        x += v[n][0] * time
        y += v[n][1] * time
        z += v[n][2] * time
        
        # print('2 ---- ', v, v[n])
 
        v[n][0] += a[0] * time
        v[n][1] += a[1] * time
        v[n][2] += a[2] * time
 
        
        if abs(x) <= side_p:
            history_x[n][epoch] = x
#             print('1x -- ', epoch, n, history_x[n][epoch])
        elif x < 0:
            history_x[n][epoch] = x + side
#             print('2x -- ', epoch, n, x, history_x[n][epoch])
        else:
            history_x[n][epoch] = x - side
#             print('3x -- ', epoch, n, x, history_x[n][epoch])

        if abs(y) <= side_p:
            history_y[n][epoch] = y
#             print('1y -- ', epoch, n, history_y[n][epoch])
        elif y < 0:
            history_y[n][epoch] = y + side
#             print('2y -- ', epoch, n, y, history_y[n][epoch])
        else:
            history_y[n][epoch] = y - side
#             print('3y -- ', epoch, n, y, history_y[n][epoch])

        if abs(z) <= side_p:
            history_z[n][epoch] = z
#             print('1z -- ', epoch, n, history_z[n][epoch])
        elif z < 0:
            history_z[n][epoch] = z + side
#             print('2z -- ', epoch, n, z, history_z[n][epoch])
        else:
            history_z[n][epoch] = z - side
#             print('3z -- ', epoch, n, z, history_z[n][epoch])
        
#         print(history_x[1][:2], history_y[1][:2], history_z[1][:2])
#         print(history_x[2][:2], history_y[2][:2], history_z[2][:2])
    
    
    history_E, history_p = EnegyMomentum(epoch)

    forovito(epoch)



for i in range(1, epoches + 1, 1):
    step(i)