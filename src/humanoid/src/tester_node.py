#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received data: %s" % data.data)

def listener():
    rospy.init_node('python_listener', anonymous=True)
    rospy.Subscriber('arduino_data', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
