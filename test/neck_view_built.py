import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.setTimeStep(1/200)
husky = p.loadURDF("/home/frank/Documents/can_motor/two_arm_neck/two_arm_neck.urdf")
numJoints = p.getNumJoints(husky)
print(numJoints)
p.setJointMotorControl2(husky, 2, p.POSITION_CONTROL, 0)
p.setJointMotorControl2(husky, 1, p.POSITION_CONTROL, 1.57)
""" for joint in range(numJoints):
  print(p.getJointInfo(husky, joint))
targetVel = 10  #rad/s
maxForce = 100  #Newton

for joint in range(0, 2):
  p.setJointMotorControl(husky, joint, p.VELOCITY_CONTROL, targetVel, maxForce)
for step in range(300):
  p.stepSimulation()

targetVel = -10
for joint in range(0, 3):
  p.setJointMotorControl(husky, joint, p.VELOCITY_CONTROL, targetVel, maxForce)
for step in range(400):
  p.stepSimulation() """
for i in range(10000):
    p.stepSimulation()
    time.sleep(1 / 200)
p.getContactPoints(husky)

p.disconnect()

p.disconnect(physicsClient)
