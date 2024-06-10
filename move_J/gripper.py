import rtde_io

HOST = "" # ip adress

rtde_io_ = rtde_io.RTDEIOInterface(HOST)



# close the gripper
rtde_io_.setToolDigitalOut(0, False)
rtde_io_.setToolDigitalOut(1, True)

# open the gripper
rtde_io_.setToolDigitalOut(1, False)
rtde_io_.setToolDigitalOut(0, True)