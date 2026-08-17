#! /usr/bin/env python3
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
import cv2
import rospy
from std_msgs.msg import String

# ---------------- CONFIG ----------------
use_test_image = False   # 🔴 set False to use camera
test_image_path = "/home/ubuntu/Downloads/h.jpeg"    # 🔴 path to test image
camera_url = "http://10.201.102.32:8080/video"
# ----------------------------------------

print(1)
nodeName1 = 'vision_node'
topicName1 = 'vision_node'

print(2)
rospy.init_node(nodeName1, anonymous=True)
publisher1 = rospy.Publisher(topicName1, String, queue_size=1)
rate = rospy.Rate(30)

print(3)

detector_hand = HandDetector(
    staticMode=False,
    maxHands=2,
    modelComplexity=1,
    detectionCon=0.5,
    minTrackCon=0.5
)

detector = PoseDetector(
    staticMode=False,
    modelComplexity=1,
    smoothLandmarks=True,
    enableSegmentation=False,
    smoothSegmentation=True,
    detectionCon=0.5,
    trackCon=0.5
)

# ---------------- TEST FUNCTION ----------------
def get_frame(cap):
    """
    Returns (success, frame)
    Uses test image if camera is not available
    """
    if use_test_image:
        img = cv2.imread(test_image_path)
        if img is None:
            rospy.logerr("Test image not found!")
            return False, None
        return True, img
    else:
        return cap.read()
# ------------------------------------------------

cap = None
if not use_test_image:
    cap = cv2.VideoCapture("10.201.102.32:8080/video")
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # cap.set(cv2.CAP_PROP_FPS, 30)


print(4)

while not rospy.is_shutdown():
    try:
        success, img = get_frame(cap)
        if not success:
            continue

        img = cv2.resize(img, (920, 780))

        hands, img = detector_hand.findHands(img, draw=True)
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

        if len(lmList) > 5:
            x0, y0 = lmList[0][0], lmList[0][1]

            cv2.circle(img, (x0, y0), 5, (255, 0, 0), cv2.FILLED)

            msg = String()
            msg.data = f"{x0},{y0}"
            publisher1.publish(msg)

            print(msg.data)

        # Optional display for debugging
        cv2.imshow("Vision Test", img)

    except Exception as e:
        print("Error:", e)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    rate.sleep()

if cap is not None:
    cap.release()

cv2.destroyAllWindows()
