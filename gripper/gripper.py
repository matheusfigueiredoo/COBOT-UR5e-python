import rtde_io

HOST = "" # ip adress

rtde_io_ = rtde_io.RTDEIOInterface(HOST)



# Fechamento do gripper

'''
Os argumentos do método representam os seguintes comandos:

rtde_io_.setToolDigitalOut(bit desejado, setar ou resetar)

bit desejado = 0 ou 1

setar ou resetar = True ou False

'''
rtde_io_.setToolDigitalOut(0, False) # "False" reseta 0
rtde_io_.setToolDigitalOut(1, True)  # "True" seta 1

# open the gripper
rtde_io_.setToolDigitalOut(1, False) # Reseta 1
rtde_io_.setToolDigitalOut(0, True)  # Seta 0
