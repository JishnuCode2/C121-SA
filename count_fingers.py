import cv2
import mediapipe as mp

wCam, hCam = 720,640

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

tip_id = [4,8,12,16,20]

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)

def drawHandLandmarks(image,hand_landmarks):
    if(hand_landmarks):
     for landmarks in hand_landmarks:
      mp_drawing.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)

def countFingers(image,hand_no=0):
    lm_list = []
    if(results.multi_hand_landmarks):
      my_hand = results.multi_hand_landmarks[hand_no]

      for id,lm in enumerate(my_hand.landmark):
          h,w,c = image.shape
          cx,cy = int(lm.x*w),int(lm.y*h)
          lm_list.append([id,cx,cy])
          print(id,lm)
      return lm_list



 
while True:
    success, image = cap.read()
    
    image = cv2.flip(image,1)

  # Detect the hand landmarks
    results = hands.process(image)
    
  # Get Landmark position from the processed result
    hand_landmarks = results.multi_hand_landmarks
  # Draw landmarks
    drawHandLandmarks(image,hand_landmarks)
    
    countFingers(image)

    cv2.imshow("Media Controller", image)
    
    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

