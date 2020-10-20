import kinpy as kp

chain = kp.build_chain_from_urdf(open("/home/frank/Documents/can_motor/two_arm_neck/two_arm_neck.urdf").read())
print(chain)