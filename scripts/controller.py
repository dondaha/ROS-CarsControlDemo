#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float32MultiArray

class Controller:
    def __init__(self):
        rospy.init_node('controller', anonymous=True)
        self.pub = rospy.Publisher('/command', Float32MultiArray, queue_size=1)
        self.ids = eval(rospy.get_param(rospy.get_name() + '/ids'))
        
        movement = [105.0, 1.0, 30.0] # [angle, direction, speed]
        self.data = []

        for id in self.ids:
            self.data += [int(id)] + movement
        rospy.loginfo("Controller started")
        while not rospy.is_shutdown():
            self.pub.publish(Float32MultiArray(data=self.data))
            rospy.sleep(0.1)
if __name__ == '__main__':
    try:
        Controller()
    except rospy.ROSInterruptException:
        pass