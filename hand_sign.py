import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier, StackingClassifier
import mediapipe as mp
import cv2
import time
import pickle


with open("model_03.pkl", "rb") as f:
    rf = pickle.load(f)


vid = cv2.VideoCapture(1)


mp_hands = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils
hand_tracker = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.9,
    min_tracking_confidence=0.9
)


text = ""
prev_sign = ""
start_time = 0
t = 1.5  

while True:
    s, f = vid.read()
    if not s:
        break

    rgb = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    op = hand_tracker.process(rgb)

    if op.multi_hand_landmarks:
        hand_landmarks = op.multi_hand_landmarks[0]
        drawing_utils.draw_landmarks(f, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        hand = []
        for i in hand_landmarks.landmark:
            hand.extend([i.x, i.y, i.z])

        if len(hand) == 63:
            reshape_hand = np.array(hand).reshape(1, 21, 3)
            ref_i = reshape_hand[:, 0, :]
            relative_positions = reshape_hand - ref_i[:, np.newaxis, :]
            formatted_input = relative_positions.reshape(1, -1)
            predicted = rf.predict(formatted_input)[0]

            if predicted == prev_sign:
                time_elapsed = time.time() - start_time
                if time_elapsed > t:
                    if predicted == "BACKSPACE":
                        text = text[:-1]
                    elif predicted == "SPACE":
                        text += " "
                    else:
                        text += predicted

                    prev_sign = ""
                    start_time = 0
                    time.sleep(0.5)  
            else:
                prev_sign = predicted
                start_time = time.time()

            cv2.putText(f, f"Sign: {predicted}", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    
    cv2.putText(f, f"Text: {text}", (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 155), 2)

    cv2.imshow("signs_to_text", f)
    if cv2.waitKey(1) & 255 == ord("c"):
        break

vid.release()
cv2.destroyAllWindows()
