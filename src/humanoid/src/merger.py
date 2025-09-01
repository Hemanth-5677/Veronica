#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

latest1 = "0,0"    # default or initial values
latest2 = "0,0,0"

def cb1(msg):
    global latest1
    # Expect msg.data like "x,y"
    latest1 = msg.data.strip()

def cb2(msg):
    global latest2
    # Expect msg.data like "0,0,z"
    latest2 = msg.data.strip()

def main():
    global latest1, latest2

    rospy.init_node('merger_node', anonymous=True)
    rospy.Subscriber('message_publisher_1', String, cb1)
    rospy.Subscriber('message_publisher_2', String, cb2)
    pub = rospy.Publisher('merged_data', String, queue_size=10)

    rate = rospy.Rate(20)  # 20 Hz loop

    while not rospy.is_shutdown():
        # Combine the two strings
        merged = f"{latest1},{latest2}"
        msg = String(data=merged)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    main()
