import rtde_receive

HOST = "" # adress ip


rtde_r = rtde_receive.RTDEReceiveInterface(HOST)

actual_q = rtde_r.getActualQ()

print("a = ", actual_q)