'''
Este código retorna a posição atual do robô.

O retorno será um vetor de 6 posições, onde cada uma representa uma junta do braço.

'''


import rtde_receive

HOST = "" # adress ip

rtde_r = rtde_receive.RTDEReceiveInterface(HOST)

actual_q = rtde_r.getActualQ()

print("a = ", actual_q)
