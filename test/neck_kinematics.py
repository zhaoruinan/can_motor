import ikpy
import numpy as np
my_chain = ikpy.chain.Chain.from_urdf_file("../two_arm_neck/neck.urdf")
def tf_neck2cam(theta1,theta2):
    real_frame = my_chain.forward_kinematics([0,theta1,theta2,0] )
    target_position = real_frame[:3, 3]
    return real_frame