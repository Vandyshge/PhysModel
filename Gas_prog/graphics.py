import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from constants import *

# def hist_e_in():
# 	return []

# def hist_p_in():
# 	return []

# def hist_e_append(voc_E, E):
# 	return voc_E.append(E)

# def hist_p_append(voc_p, p):
# 	return voc_p.append(p)

def graphic_E(voc_E, name_folder):
	voc_time = np.arange(0, sec + dt, dt)
	fig, ax = plt.subplots()
	ax.plot(voc_time, np.array(voc_E))
	ax.set(xlabel='time', ylabel='E',
	       title='Полная энергия системы')
	ax.grid()
	fig.savefig('C:/Users/Xiaomi/PhysModelNew/output/forovito{}/E.png'.format(name_folder))
	plt.show()

def graphic_p(voc_p, name_folder):
	voc_time = np.arange(0, sec + dt, dt)
	voc_p = np.sqrt(np.sum(np.array(voc_p)**2, axis=1))
	fig, ax = plt.subplots()
	ax.plot(voc_time, voc_p)
	ax.set(xlabel='time', ylabel='p',
	       title='Полный импульс системы')
	ax.grid()
	fig.savefig('C:/Users/Xiaomi/PhysModelNew/output/forovito{}/p.png'.format(name_folder))
	plt.show()