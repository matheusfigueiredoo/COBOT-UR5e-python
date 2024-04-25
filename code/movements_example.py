import rtde_control
import rtde_io
import time

HOST = "" # ip adress

rtde_io_ = rtde_io.RTDEIOInterface(HOST)
rtde_c = rtde_control.RTDEControlInterface(HOST)


base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]

a = [-4.076599899922506, -0.7863095563701172, 1.3410056273089808, -2.090026994744772, -1.4898093382464808, -2.235628906880514]

b = [-4.059603039418356, -0.7164358657649537, 1.383453671132223, -2.2590977154173792, -1.5111663977252405, -2.1496413389789026]

# moviments sequency

rtde_c.moveJ(base)
time.sleep(1)
rtde_c.moveJ(a)
time.sleep(1)
rtde_c.moveJ(b)
rtde_io_.setToolDigitalOut(1, True)
time.sleep(1)
rtde_c.moveJ(a)
rtde_c.moveJ(base)