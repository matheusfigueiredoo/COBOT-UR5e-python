'''
Este código coloca o robô na posição de dormir. 

Geralmente, ele é executado antes de desligar o robô.
'''


import rtde_control
import time

HOST = "" # ip adress

rtde_c = rtde_control.RTDEControlInterface(HOST)

# posição vertical
home = [-8.408223287403871e-06, -1.5707289909153879, -5.28501404915005e-05, -1.5707760683947818, -9.838734762013246e-06, -5.547200338185121e-06]

# posição de dormir
to_sleep = [1.5707809925079346, -2.1891002990770403e-05, -2.8274474143981934, -1.8849736652769984, 3.141608715057373, 1.5708245038986206]

# mover robô para as posições dadas acima
rtde_c.moveJ(home)
time.sleep(2)
rtde_c.moveJ(to_sleep)