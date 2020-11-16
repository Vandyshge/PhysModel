from constants import *
import os

def create_folder(name_folder):
    os.mkdir('C:/Users/Xiaomi/PhysModelNew/output/forovito{}'.format(name_folder))

def output_enegy(name_folder, epoch, E): 
    out = open('C:/Users/Xiaomi/PhysModelNew/output/forovito{}/E.txt'.format(name_folder), 'a')
    out.write("{} {}\n".format(epoch, E))
    out.close()
    
def output_momentum(name_folder, epoch, p):
    out = open('C:/Users/Xiaomi/PhysModelNew/output/forovito{}/p.txt'.format(name_folder), 'a')
    out.write("{} {} {} {}\n".format(epoch, p[0], p[1], p[2]))
    out.close()
   
def forovito(name_folder, epoch, loc, v):
    out = open('C:/Users/Xiaomi/PhysModelNew/output/forovito{}/{}.xyz'.format(name_folder, epoch), 'a')
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
        out.write("{} {} {} {} {} {}\n".format(loc[i][0][1], loc[i][1][1], loc[i][2][1], v[i][0], v[i][1], v[i][2]))
    out.close()
