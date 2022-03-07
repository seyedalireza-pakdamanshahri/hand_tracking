import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands # mpHands is a class 
hands = mpHands.Hands() # hands is an object of mpHands class
mpDraw =  mp.solutions.drawing_utils # Drawing utils
while True:
    success , img = cap.read() # Read the frame , success is boolean , img is the frame
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # Convert the frame to RGB
    results = hands.process(imgRGB) # Process the frame
    if results.multi_hand_landmarks: # If there are multiple hands
        for handLms in results.multi_hand_landmarks: # For each hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # Draw the hand

    cv2.imshow("image",img) # Show the frame
    cv2.waitKey(1) # Wait for 1 millisecond
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # Break if the user presses 'q' key