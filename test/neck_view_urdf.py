from urdfpy import URDF
robot = URDF.load("/home/frank/Documents/can_motor/two_arm_neck/two_arm_neck.urdf")
for link in robot.links:
    print(link.name)
for joint in robot.joints:
    print('{} connects {} to {}'.format(joint.name, joint.parent, joint.child))
for joint in robot.actuated_joints:
    print(joint.name)

#fk = robot.link_fk(cfg={'shoulder_pan_joint' : 1.0})
#print(fk[robot.links[1]])