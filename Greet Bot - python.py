import cv2
import mediapipe as mp
import time
import pyfirmata

board = pyfirmata.ArduinoMega('Enter the port name here')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()
s1 = board.get_pin('d:9:s')
s2 = board.get_pin('d:10:s')
s3 = board.get_pin('d:8:s')
dpin=board.get_pin('d:5:i')

s2.write(100)



class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image

    def positionFinder(self,image, handNo=0, draw=True):
        lmlist = []


        def move_servo(a,b,c):

            s2.write(b)
            s3.write(c)
            s1.write(80)
            inp = dpin.read()
            if (inp== False) and (a==2):
                s1.write(40)
                time.sleep(0.5)
                s1.write(80)
                time.sleep(0.5)
                s1.write(40)
                time.sleep(0.5)
                s1.write(80)

            elif (inp== False) and (a==1):
                s1.write(40)
                time.sleep(0.5)
                s1.write(100)
                time.sleep(1)
                s1.write(80)


            return 0
        def stt(x, y):
            if (x>=43 and x<=314) and (y>=340 and y<=460):
                ss3=((x-43)/9.03333)+120
                ss3=270-ss3
                ss2=90
                print(ss3)
                h = move_servo(2, ss2,ss3)
                return "HandShake"
            elif (x>=127 and x<=306) and (y>=58 and y<=260):
                ss2=150
                ss3=((x-127)/5.96666)+120
                ss3=270-ss3
                h = move_servo(1, ss2, ss3-10)
                return "HiFi"
            else:
                return "No"


        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
            if draw:
                cv2.circle(image,(cx,cy), 15 , (255,0,255), cv2.FILLED)
                cv2.putText(image, stt(cx, cy), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 255, 255), 1)

        return lmlist

def main():
    cap = cv2.VideoCapture(1)
    tracker = handTracker()

    while True:
        success,image = cap.read()
        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        if len(lmList) != 0:
            print(lmList[4])

        cv2.imshow("Video",image)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()