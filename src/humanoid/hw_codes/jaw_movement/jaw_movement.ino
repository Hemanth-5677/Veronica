#include <ros.h>
#include <Wire.h>
#include <std_msgs/String.h>
#include <Adafruit_PWMServoDriver.h>
String x = "";
int jaw = 0;
ros::NodeHandle nh;
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVOMIN  140 // minimum pulse length count (out of 4096)
#define SERVOMAX  520 // maximum pulse length count (out of 4096)
void callbackFunction(const std_msgs::String &msg);

// Subscribers and Publishers
std_msgs::String status_msg;
ros::Publisher arduino_pub("voice_serial", &status_msg);
ros::Subscriber<std_msgs::String> voice("voice_node", &callbackFunction);
// Hardware pins and variables
const int analogInPin = A0;
int trimval;
int switchval = 0;
static uint32_t curr = millis();

void setup() {
  Serial.begin(57600);
  Serial.println("8 channel Servo test!");
  pinMode(analogInPin, INPUT);
  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
  delay(10);
  
  nh.initNode();
  nh.subscribe(voice);
  nh.advertise(arduino_pub);
  pwm.setPWM(0, 0, 200);
  pwm.setPWM(1, 0, 200);
  delay(100);
}

// Optional helper function to set servo pulse length (not used in this example)
void setServoPulse(uint8_t n, double pulse) {
  double pulselength;
  pulselength = 1000000;   // 1,000,000 us per second
  pulselength /= 60;       // 60 Hz
  Serial.print(pulselength); Serial.println(" us per period"); 
  pulselength /= 4096;     // 12 bits of resolution
  Serial.print(pulselength); Serial.println(" us per bit"); 
  pulse *= 1000000;        // convert to us
  pulse /= pulselength;
  Serial.println(pulse);
}

void loop() {
  // Publish movement status message
  char buf[15];
  snprintf(buf, sizeof(buf), "%d ", jaw);
  status_msg.data = buf;
  arduino_pub.publish(&status_msg);
  nh.spinOnce();
  //delay(10);  // Publish every 100 ms, adjust as needed
}

// Drive jaw servo on channel 6
void set_jaw_location(int angle) {
  int pulse = map(angle, 0, 15, 200, 580);
  int trim = analogRead(A0);
  trim = map(trim, 320, 580, -20, 20);
  int adj = constrain(pulse + trim, 130, 370);
  pwm.setPWM(0, 0, pulse);
  pwm.setPWM(1, 0, pulse);
}




void callbackFunction(const std_msgs::String &msg) {
  String str = String(msg.data);
  x = str;
  int dat[3] = {0, 0, 0};
  int start = 0;
  int idx;
  for (int i = 0; i < 3; i++) {
    // Find comma or end of string
    idx = str.indexOf(',', start);
    if (idx == -1 || i == 4) {
      // Last field: go to end of string
      dat[i] = str.substring(start).toInt();
      break;
    }
    // Extract substring between start and idx
    dat[i] = str.substring(start, idx).toInt();
    start = idx + 1;
  }
  set_jaw_location(dat[2]);
  jaw = dat[2];
}
