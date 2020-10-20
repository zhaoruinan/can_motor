import ikpy
import numpy as np
import ikpy.utils.plot as plot_utils
my_chain = ikpy.chain.Chain.from_urdf_file("/home/frank/Documents/can_motor/two_arm_neck/two_arm_neck.urdf")
real_frame = my_chain.forward_kinematics([2.0,0.0])
print(real_frame)
import matplotlib.pyplot as plt
fig, ax = plot_utils.init_3d_figure()
my_chain.plot([2.0,0.0], ax, target=real_frame[:3, 3])
plt.xlim(-0.1, 0.1)
plt.ylim(-0.1, 0.1)
plt.show()
