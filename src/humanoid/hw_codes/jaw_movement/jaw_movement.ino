#include <ros.h>
#include <Wire.h>
#include <std_msgs/String.h>
#include <Adafruit_PWMServoDriver.h>

// ================= ROS =================
ros::NodeHandle nh;
std_msgs::String status_msg;
ros::Publisher arduino_pub("voice_serial", &status_msg);
void callbackFunction(const std_msgs::String &msg);
ros::Subscriber<std_msgs::String> voice("voice_node", &callbackFunction);

// ================= PCA9685 =================
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// ================= JAW CONFIG =================
int jaw = 0;

// 👇 calibrated values (from your test)
int jawClosed = 345;
int jawOpen   = 450;

// mirrored servo offsets (keep 0 unless needed)
int servo0Offset = 0;
int servo1Offset = 0;

// safety limits
#define SERVO_MIN 130
#define SERVO_MAX 580

// ================= STARTUP CLEAN =================
void disableServos() {
  pwm.setPWM(0, 0, 0);
  pwm.setPWM(1, 0, 0);
}

// ================= JAW CONTROL =================
// CH0 = mirrored
// CH1 = normal
void setJawPulse(int pulse) {

  pulse = constrain(pulse, jawClosed, jawOpen);

  int pulse1 = pulse + servo1Offset;
  int pulse0 = jawClosed + (jawOpen - pulse) + servo0Offset;

  pulse0 = constrain(pulse0, SERVO_MIN, SERVO_MAX);
  pulse1 = constrain(pulse1, SERVO_MIN, SERVO_MAX);

  pwm.setPWM(0, 0, pulse0);
  pwm.setPWM(1, 0, pulse1);
}

// ================= SETUP =================
void setup() {
  Serial.begin(57600);
  Serial.println("ROS Jaw Controller Started");

  pwm.begin();
  pwm.setPWMFreq(60);
  delay(50);

  disableServos();
  delay(100);

  // start closed
  setJawPulse(jawClosed);

  nh.initNode();
  nh.subscribe(voice);
  nh.advertise(arduino_pub);
}

// ================= LOOP =================
void loop() {
  char buf[10];
  snprintf(buf, sizeof(buf), "%d", jaw);
  status_msg.data = buf;
  arduino_pub.publish(&status_msg);

  nh.spinOnce();
}

// ================= ROS CALLBACK =================
void callbackFunction(const std_msgs::String &msg) {

  String str = String(msg.data);

  // expecting: v1,v2,jaw
  int dat[3] = {0, 0, 0};
  int start = 0;
  int idx;

  for (int i = 0; i < 3; i++) {
    idx = str.indexOf(',', start);
    if (idx == -1 || i == 2) {
      dat[i] = str.substring(start).toInt();
      break;
    }
    dat[i] = str.substring(start, idx).toInt();
    start = idx + 1;
  }

  // map jaw command (0–15 → pulse range)
  int pulse = map(dat[2], 0, 15, jawClosed, jawOpen);
  setJawPulse(pulse);

  jaw = dat[2];
}
