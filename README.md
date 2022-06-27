# The-Greet-Bot
To greet the and welcome all, a robot made using Jetson Nano, Media pipe and CV2

Its a common tradition in India to greet and welcome all guests who come to your home, a party or literally anywhere. There is this one person, who always at the entrance ready to greet all guests and then welcome them. Why don't we create a robot that can imitate this greeting task !!
# What can the Robot do !
1. Recognize you
2. Give you a handshake
3. Give you a High-Five
4. Bless You !!!
# How can the Robot do this ?
Its quite simple, Let me show you the process of building the robot and programming the Jetson Nano.

At the Basic level, Lets split the tasks into 2: Programming and Hardware
## Hardware
#### Components you'll need:
1. Jetson Nano 4GB
2. 32GB (min) memory card
3. C270 Logitech Camera
4. 3 Servo Motors
5. Material to mount the servos on (I used PVC pipes)
6. Arduino Board
7. IR sensor
8. Connecting Wires

Connect the Servos and the sensor to the Arduino as shown here:
![Screenshot (20)](https://user-images.githubusercontent.com/65992357/175828704-bafcac5f-a674-455c-a1a4-a1a61372f699.png)
  
Connect the arduino and the webcam to the USB ports of the Jetson Nano
 

## Programming
For Programming you'll require these libraries first. We'll need to install them.
1. Mediapipe
2. pyfirmata
3. cv2
4. time

Use these links to know, how to download the required libraries
https://youtu.be/0TBeN0Kd9zM
https://forums.developer.nvidia.com/t/install-opencv-for-python3-in-jetson-nano/74042
https://roboticsbackend.com/control-arduino-with-python-and-pyfirmata-from-raspberry-pi/

Use the python program added to the repository and use a IDE of your choice to run the program.

##### Mediapipe Hand Tracking
The ability to understand the shape of the human hand and the motions are impaortant in our application. Various models available in Mediapipe is the Palm Detection model and Hard Landmarks model.
https://google.github.io/mediapipe/solutions/hands.html

#### Arduino
  Pyfirmata is used to control the Arduino board. Download the Arduino IDE on your Jetson or on your PC. Through the Arduino IDE, upload the Standard Firmata program.
  To access the Standard Firmata Program = File --> Examples --> Firmata --> Standard Firmata
  ![Screenshot (21)](https://user-images.githubusercontent.com/65992357/175873363-c7d83979-9179-4ec7-ab0e-74a2b73e7b38.png)

  
  After this we can program the Arduino through the Python Program

