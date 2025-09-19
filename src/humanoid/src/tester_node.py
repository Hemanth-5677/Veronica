#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_vision(data):
    rospy.loginfo("Received eye_data: %s" % data.data)

def callback_voice(data):
    rospy.loginfo("Received voice_data: %s" % data.data)



def listener():
    rospy.init_node('python_listener', anonymous=True)
    rospy.Subscriber('voice_serial', String, callback_voice)
    rospy.Subscriber('vision_serial', String, callback_vision)

    rospy.spin()

if __name__ == '__main__':
    listener()
