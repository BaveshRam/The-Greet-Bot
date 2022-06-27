import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 20 :
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    cv2.putText(image, 'OpenCV', (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (225,0,0), 1)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Output", image)
    cv2.waitKey(1)