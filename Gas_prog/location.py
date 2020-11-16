from constants import *
from random import randint
from tqdm.autonotebook import tqdm
import numpy as np



def location_init():
    loc = []
    for _ in tqdm(range(N)):
        while True:
            x = 10 ** -3 * randint(-int(side_p * 10 ** 3), int(side_p * 10 ** 3))
            y = 10 ** -3 * randint(-int(side_p * 10 ** 3), int(side_p * 10 ** 3))
            z = 10 ** -3 * randint(-int(side_p * 10 ** 3), int(side_p * 10 ** 3))
            for i in range(len(loc)):
                if (x - loc[i][0][1])**2 + (y - loc[i][1][1])**2 + (z - loc[i][2][1])**2 <= (side / 10)**2:
                    break
            break
        loc.append([[0, x, 0], [0, y, 0], [0, z, 0]])
    return np.array(loc)

def loc_fr(x, y, z, x_i, y_i, z_i):
    voc = []
    for t, t_i in [(x, x_i), (y, y_i), (z, z_i)]:
        if abs(t - t_i) <= side_p:
            pass
        elif abs(t - (t_i + side)) <= side_p:
            t_i = t_i + side
        elif abs(t - (t_i - side)) <= side_p:
            t_i = t_i - side
        voc.append(t_i)
    return (voc[0], voc[1], voc[2])

# def loc_fr1(t, t_i):
#     voc = []
#     for t, t_i in [(x, x_i), (y, y_i), (z, z_i)]:
#         if abs(t - t_i) <= side_p:
#             pass
#         elif abs(t - (t_i + side)) <= side_p:
#             t_i = t_i + side
#         elif abs(t - (t_i - side)) <= side_p:
#             t_i = t_i - side
#         voc.append(t_i)
#     return (voc[0], voc[1], voc[2])

def loc_side(x, y, z):
    voc = []
    for t in [x, y, z]:
        if abs(t) <= side_p:
            pass
        elif t < - side_p:
            t = - (abs(t) % side_p) + side_p
        elif t > side_p:
            t = t % side_p - side_p
    return (voc[0], voc[1], voc[2])

def loc_side1(t):
    if abs(t) <= side_p:
        pass
    elif t < - side_p:
        t = - (abs(t) % side_p) + side_p
    elif t > side_p:
        t = t % side_p - side_p
    return [0, t, 0]

def l(x, y, z, x_i, y_i, z_i):
    lenth_v = np.array([x - x_i, y - y_i, z - z_i])
    lenth = (lenth_v[0] ** 2 + lenth_v[1] ** 2 + lenth_v[2] ** 2) ** (1 / 2)
    return (lenth, lenth_v)

if __name__ == '__main__':
    pass
