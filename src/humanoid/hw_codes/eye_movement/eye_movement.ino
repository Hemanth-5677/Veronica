#include <ros.h>
#include <Wire.h>
#include <std_msgs/String.h>
#include <Adafruit_PWMServoDriver.h>

int jaw = 0;
ros::NodeHandle nh;
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  140
#define SERVOMAX  520

void callbackFunction(const std_msgs::String &msg);

// Publishers/Subscribers
std_msgs::String status_msg;
ros::Publisher arduino_pub("vision_serial", &status_msg);
ros::Subscriber<std_msgs::String> vision("merger_node", &callbackFunction);

int x = 0;
int y = 0;
int trimval;
int switchval = 0;
static uint32_t curr;

void setup() {
  curr = millis();
  Serial.begin(57600);
  Serial.println("Eye System Start");

  pwm.begin();
  pwm.setPWMFreq(60);
  delay(10);

  nh.initNode();
  nh.subscribe(vision);
  nh.advertise(arduino_pub);
}
//
//void loop() {
//  char buf[10];
//  snprintf(buf, sizeof(buf), "%d,%d", x, y);
//  status_msg.data = buf;
//  arduino_pub.publish(&status_msg);
//  nh.spinOnce();
//}
void loop() {
  static unsigned long lastPub = 0;

  if (millis() - lastPub > 33) {   // ~30 Hz
    char buf[16];
    snprintf(buf, sizeof(buf), "%d,%d", x, y);
    status_msg.data = buf;
    arduino_pub.publish(&status_msg);
    lastPub = millis();
  }

  nh.spinOnce();
}

// ================== SERVO CONTROL ==================
void set_location(int x ,int y){

  int lexpulse;
  int rexpulse;
  int leypulse;
  int reypulse;

  int uplidpulse;
  int lolidpulse;
  int altuplidpulse;
  int altlolidpulse;

  // 👁 Eye horizontal (X axis)
  lexpulse = map(x, 920, 0, 220, 440);
  rexpulse = lexpulse;

  // 👁 Eye vertical (Y axis)
  leypulse = map(y, 780, 0, 250, 500);
  reypulse = map(y, 780, 0, 400, 280);

  trimval = analogRead(A2);
  trimval = map(trimval, 320, 580, -40, 40);

  // 🔥 Eyelids (calibrated values)

  uplidpulse = map(y, 780, 0, 310, 440);
  uplidpulse -= (trimval - 40);
  uplidpulse = constrain(uplidpulse, 300, 440);

  lolidpulse = map(y, 780, 0, 330, 220);
  lolidpulse += (trimval / 2);
  lolidpulse = constrain(lolidpulse, 220, 330);

  altuplidpulse = map(y, 780, 0, 370, 240);
  altuplidpulse = constrain(altuplidpulse, 240, 370);

  altlolidpulse = map(y, 780, 0, 300, 430);
  altlolidpulse = constrain(altlolidpulse, 300, 430);

  // Apply eye movement
  pwm.setPWM(0, 0, lexpulse);
  pwm.setPWM(1, 0, leypulse);

  // 👁 Blink every 2 seconds
  if(millis() - curr >= 2000){
    pwm.setPWM(2, 0, 440);
    pwm.setPWM(3, 0, 220);
    pwm.setPWM(4, 0, 240);
    pwm.setPWM(5, 0, 430);
    delay(100);

    pwm.setPWM(2, 0, uplidpulse);
    pwm.setPWM(3, 0, lolidpulse);
    pwm.setPWM(4, 0, altuplidpulse);
    pwm.setPWM(5, 0, altlolidpulse);
    curr = millis();
  }
}

// ================== ROS CALLBACK ==================
void callbackFunction(const std_msgs::String &msg) {
  String str = String(msg.data);

  int dat[2] = {0, 0};
  int start = 0;
  int idx;

  for (int i = 0; i < 2; i++) {
    idx = str.indexOf(',', start);
    if (idx == -1 || i == 1) {
      dat[i] = str.substring(start).toInt();
      break;
    }
    dat[i] = str.substring(start, idx).toInt();
    start = idx + 1;
  }

  set_location(dat[0], dat[1]);
  x = dat[0];
  y = dat[1];
}
