#! /usr/bin/env python3
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
import cv2
# publisher part of the code that publishes the reqired angle as well as the coefficients that we calculated
'''
Note: We can calculate coefficient in real time aswell using a more sophesticated feed forward network than simple linear regression
'''


import rospy 
from humanoid.msg import Coordinates
from std_msgs.msg import String

print(1)
nodeName1 = 'vision_node'
topicName1= 'vision_node'

print(2)
rospy.init_node(nodeName1, anonymous=True)
publisher1 = rospy.Publisher(topicName1,String,queue_size=1)
rate = rospy.Rate(30)
x=0

print(3)
# Machine-Learning part of the code to implement simple regression 
cap = cv2.VideoCapture("http://192.168.137.116:8080/video")
detector_hand = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
print(4)
while not rospy.is_shutdown():
    fingers1=[]
    fingers2=[]
    try:
        success, img = cap.read()
        hands, img = detector_hand.findHands(img, draw=True)
        img=cv2.resize(img,(920,780))
        x=0
        y=0
        print(5)
        center1=[]
            # Initialize the PoseDetector class with the given parameters
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)
        if len(lmList)>5:
            center = bboxInfo["center"]
            # Information for the first hand detected
            # hand1 = hands[0]  # Get the first hand detected
            # lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
            # bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
            # center1 = hand1['center']  # Center coordinates of the first hand
            print(center1)
            # handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")
            # print(center1)
            cv2.circle(img, (lmList[0][0], lmList[0][1]), 5, (255, 0, 0), cv2.FILLED)
            # Count the number of fingers up for the first hand
            # fingers1 = detector_hand.fingersUp(hand1)
            # print(f'\033[0;34mH1 = \033[0;33m{fingers1.count(1)}', end=" ")  # Print the count of fingers that are up

            # Calculate distance between specific landmarks on the first hand and draw it on the image
            # length, info, img = detector_hand.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),scale=10)

            # print(info)  # New line for better readability of the printed output
            # print(" ")  # New line for better readability of the printed output
            msg= String()
            infos=""
            m = f'{lmList[0][0]},{lmList[0][1]}'
            msg.data=m
            print(m)
            publisher1.publish(msg)
    except:
        pass
    # img = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    # Display the image in a window
    # img = cv2.rectangle(img, (100,250),(400,600), color=(255,255,255), thickness=2)
    # img = cv2.rectangle(img, (600,250),(900,600), color=(255,255,255), thickness=2)
    #cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # theta = int(input("enter the ange that you wnat to rotate the bot with : "))
    rate.sleep()
    fingers1=[None]
    x+=1
cap.release()
