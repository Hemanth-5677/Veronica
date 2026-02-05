#include <ros.h>
#include <Wire.h>
#include <std_msgs/String.h>
#include <Adafruit_PWMServoDriver.h>

int jaw = 0;
ros::NodeHandle nh;
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  140 // minimum pulse length count (out of 4096)
#define SERVOMAX  520 // maximum pulse length count (out of 4096)
void callbackFunction(const std_msgs::String &msg);

// Subscribers and Publishers
std_msgs::String status_msg;
ros::Publisher arduino_pub("vision_serial", &status_msg);
ros::Subscriber<std_msgs::String> vision("merger_node", &callbackFunction);
// Hardware pins and variables
int x =0;
int y =0;
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
  nh.subscribe(vision);
  nh.advertise(arduino_pub);
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
  char buf[10];
  snprintf(buf, sizeof(buf), "%d,%d", x, y);
  status_msg.data = buf;
  arduino_pub.publish(&status_msg);
  nh.spinOnce();
  //delay(10);  // Publish every 100 ms, adjust as needed
}

void set_location(int x ,int y){
  int lexpulse;
  int rexpulse;
  
  int leypulse;
  int reypulse;
  
  int uplidpulse;
  int lolidpulse;
  int altuplidpulse;
  int altlolidpulse;
      lexpulse = map(x,780, 30, 220, 440);
      rexpulse = lexpulse;
  
      switchval = digitalRead(2);
      
      
      leypulse = map(y, 450,0, 250, 500);
      reypulse = map(y, 450,0, 400, 280);
  
    trimval = analogRead(A2);
      trimval=map(trimval, 320, 580, -40, 40);
       uplidpulse = map(y, 450,0, 400, 280);
          uplidpulse -= (trimval-40);
            uplidpulse = constrain(uplidpulse, 280, 400);
       altuplidpulse = 680-uplidpulse;
  
       lolidpulse = map(y, 450,0, 410, 280);
         lolidpulse += (trimval/2);
           lolidpulse = constrain(lolidpulse, 280, 400);      
       altlolidpulse = 680-lolidpulse;
   
      
        pwm.setPWM(0, 0, lexpulse);
        pwm.setPWM(1, 0, leypulse);
        
        if(millis()-curr >=2000){
        pwm.setPWM(2, 0, 400);
        pwm.setPWM(3, 0, 240);
        pwm.setPWM(4, 0, 240);
        pwm.setPWM(5, 0, 400);
        delay(100);
        pwm.setPWM(2, 0, uplidpulse);
        pwm.setPWM(3, 0, lolidpulse);
        pwm.setPWM(4, 0, altuplidpulse);
        pwm.setPWM(5, 0, altlolidpulse);
        curr = millis();
        }
  
  
   Serial.println(trimval);
}


void callbackFunction(const std_msgs::String &msg) {
  String str = String(msg.data);
  
  int dat[2] = {0, 0};
  int start = 0;
  int idx;
  for (int i = 0; i < 2; i++) {
    // Find comma or end of string
    idx = str.indexOf(',', start);
    if (idx == -1 || i == 1) {
      // Last field: go to end of string
      dat[i] = str.substring(start).toInt();
      break;
    }
    // Extract substring between start and idx
    dat[i] = str.substring(start, idx).toInt();
    start = idx + 1;
  }

  // dat[0]=x, dat[1]=y, dat[2]=v2, dat[3]=v3, dat[4]=z
  set_location(dat[0], dat[1]);
  x = dat[0];
  y = dat[1];
}
