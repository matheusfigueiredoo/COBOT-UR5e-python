import rtde_receive

HOST = "" # adress ip

'''
Bloco de comentário

Text

Text

'''


rtde_r = rtde_receive.RTDEReceiveInterface(HOST)

actual_q = rtde_r.getActualQ()

print("a = ", actual_q)
