import cv2
import mediapipe as mp

# These define the tools for the rest of the script
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Initialize the hand tracking model
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

print("Starting Camera... wave at the webcam!")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    count = 0

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            # Draw the skeleton
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            # Simple finger counting logic
            # Tip of Finger (8, 12, 16, 20) vs Middle Joint (6, 10, 14, 18)
            landmarks = hand_lms.landmark
            if landmarks[8].y < landmarks[6].y: count += 1   # Index
            if landmarks[12].y < landmarks[10].y: count += 1 # Middle
            if landmarks[16].y < landmarks[14].y: count += 1 # Ring
            if landmarks[20].y < landmarks[18].y: count += 1 # Pinky
            if landmarks[4].x > landmarks[3].x: count += 1   # Thumb (simplified)

    cv2.putText(frame, f"Count: {count}", (50, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    cv2.imshow("Finger Counter", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

