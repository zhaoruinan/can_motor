from neck_sim import neck_sim

sim = neck_sim()
sim.motor_set_speed(3,10)
for i in range(10000):
    sim.step()
sim.stop()