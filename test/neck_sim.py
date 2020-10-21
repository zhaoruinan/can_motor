import pybullet as p
import time
import pybullet_data
class neck_sim():
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        p.setTimeStep(1/200)
        self.maxForce = 100  #Newton
        self.neck = p.loadURDF("../two_arm_neck/neck.urdf")
        numJoints = p.getNumJoints(self.neck)
        print(numJoints)
    def motor_set_speed(self,node,speed):
        targetVel = speed
        if node == 3:
            p.setJointMotorControl(self.neck, 2, p.VELOCITY_CONTROL, targetVel, self.maxForce)
        if node ==5:
            p.setJointMotorControl(self.neck, 1, p.VELOCITY_CONTROL, targetVel, self.maxForce)
    def stop(self):
        p.disconnect(self.physicsClient)
    def step(self):
        p.stepSimulation()
        time.sleep(1 / 200)