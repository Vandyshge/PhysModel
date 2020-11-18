from trance import *
from location import *
from velosity import *
from output import *
from graphics import *
from tqdm.autonotebook import tqdm
import numpy as np

if __name__ == '__main__':
    name_folder = input('Введите название папки: ')
    create_folder(name_folder)
    loc = location_init()
    v = socm(Maxvell_v2())
    # loc = np.array([[[0, 0.6, 0], [0, 0, 0], [0, 0, 0]], [[0, -0.6, 0], [0, 0, 0], [0, 0, 0]]], dtype = float)
    # v = np.array([[-5, 0, 0], [5, 0, 0]], dtype = float)

    E, p = energy(loc, v), momentum(v)

    output_enegy(name_folder, 0, E)
    output_momentum(name_folder, 0, p)
    voc_E, voc_p, voc_ep_E = [E], [p], []
    forovito(name_folder, 0, loc, v)
    E_1 = E
    # a = np.zeros((N, 3))
    for epoch in tqdm(range(1, epoches + 1)):
        loc, v = step(epoch, loc, v)
        E, p = energy(loc, v), momentum(v)
        ep_E = (E - E_1) / E
        output_enegy(name_folder, epoch, E)
        output_momentum(name_folder, epoch, p)
        output_ep_enegy(name_folder, epoch, ep_E)
        forovito(name_folder, epoch, loc, v)
        voc_E.append(E)
        voc_p.append(p)
        voc_ep_E.append(ep_E)
        E_1 = E


    graphic_ep_E(voc_ep_E, name_folder)
    graphic_E(voc_E, name_folder)
    graphic_p(voc_p, name_folder)