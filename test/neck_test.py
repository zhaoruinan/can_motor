import ikpy
import numpy as np
import ikpy.utils.plot as plot_utils

my_chain = ikpy.chain.Chain.from_urdf_file("../two_arm_neck/neck.urdf")
real_frame = my_chain.forward_kinematics([0,0,0,0] )
target_position = real_frame[:3, 3]
import matplotlib.pyplot as plt
fig, ax = plot_utils.init_3d_figure()
my_chain.plot(my_chain.inverse_kinematics(target_position), ax, target=target_position)
plt.xlim(-0.1, 0.1)
plt.ylim(-0.1, 0.1)
plt.show()