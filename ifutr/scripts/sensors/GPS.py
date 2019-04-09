#!/usr/bin/env python
from time import sleep

import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import PoseStamped
from ifutr.msg import Pozyx_Pose





class Fake_GPS(object):

    def __init__(self):
        self.r = rospy.Rate(5)
        self.pub = rospy.Publisher('/mavros/mocap/pose', PoseStamped, queue_size=10)
        self.sub = rospy.Subscriber('/pose', PoseStamped, self.poseCallback)
        self.gps = PoseStamped()


    def poseCallback(self, msg):
        self.gps = msg
        #print(self.gps)


    def run(self):
        while not rospy.is_shutdown():
            self.gps.header.stamp = rospy.Time.now()
            self.gps.header.frame_id = 'map'
            #self.pose.pose.position.x = position.x
            #self.pose.pose.position.y = position.y
            #self.pose.pose.position.z = position.z
            #self.gps.pose.position.x = 1.5
            #self.gps.pose.position.y = 1.5
            #self.gps.pose.position.z = 1.5
            self.gps.pose.orientation.w = 1.0
            self.pub.publish(self.gps)
            self.r.sleep()


def initialize():
    rospy.init_node('Fake_GPS', anonymous=False)



if __name__ == "__main__":
    initialize()
    g = Fake_GPS()
    g.run()
