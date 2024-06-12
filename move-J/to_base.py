'''
Este código executa o robô colocando em uma posição de base, definida manualmente.
'''

import rtde_control
import time

HOST = "" # ip adress

rtde_c = rtde_control.RTDEControlInterface(HOST)

# posição vertical
home = [-8.408223287403871e-06, -1.5707289909153879, -5.28501404915005e-05, -1.5707760683947818, -9.838734762013246e-06, -5.547200338185121e-06]

# posição definida manualmente no modo 'free way' pelo PolyScope
base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]

# execução do robô
rtde_c.moveJ(home)
time.sleep(2)
rtde_c.moveJ(base)