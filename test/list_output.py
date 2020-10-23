import time
def search():
    time.sleep(2)
    pos_list = [[0,0],[0,4000],[7500,4000],[7500,0]]
    for pos in pos_list:
        #motor1.angle_set(pos[0])
        #motor2.angle_set(pos[1])
        print(pos[0],pos[1])
        time.sleep(5)
search()