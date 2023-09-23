import cv2
import numpy as np

cap = cv2.VideoCapture(0)

calibration_color_1 = [0, 0, 0]
calibration_color_2 = [0, 0, 0]


def same_color(c1, c2):
    return c1[0] - 10 <= c2[0] <= c1[0] + 10 and c1[1] - 10 <= c2[1] <= c1[1] + 10 and c1[2] - 10 <= c2[2] <= c1[2] + 10


# 600x120????
readers_w = 500
readers_h = 120

iterations = 0
while True:
    ret, frame = cap.read()

    frame_height = frame.shape[0]
    frame_width = frame.shape[1]

    readers_x = int((frame_width - readers_w) / 2)  # Center readers coordinates
    readers_y = int((frame_height - readers_h) / 2)

    top_left = np.full((200, 200, 3), frame[readers_y + 10, readers_x + 10], dtype=np.uint8)
    bottom_right = np.full((200, 200, 3),
                           frame[int(readers_y + readers_h * (2 / 3) + 10), int((readers_w + 100) * (14 / 15))],
                           dtype=np.uint8)
    image2 = np.full((200, 200, 3), calibration_color_1, dtype=np.uint8)
    image3 = np.full((200, 200, 3), calibration_color_2, dtype=np.uint8)

    if same_color(frame[readers_y + 10, readers_x + 10], calibration_color_1) and same_color(
            frame[int(readers_y + readers_h * (2 / 3) + 10), int((readers_w + 100) * (14 / 15))], calibration_color_2):
        print(f"Same Color #{iterations}")

    # Set calibration color
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print(f"calibration_color1: {frame[readers_y + 10, readers_x + 10]}")
        print(
            f"calibration_color2: {frame[int(readers_y + readers_h * (2 / 3) + 10), int((readers_w + 100) * (14 / 15))]}")
        calibration_color_1 = frame[readers_y + 10, readers_x + 10]
        calibration_color_2 = frame[int(readers_y + readers_h * (2 / 3) + 10), int((readers_w + 100) * (14 / 15))]

    cv2.rectangle(frame, (readers_x, readers_y), (readers_x + readers_w, readers_y + readers_h), (0, 255, 0), 2)

    cv2.imshow('Current color', top_left)
    cv2.imshow('Current color2', bottom_right)
    cv2.imshow('Calibration Color1', image2)
    cv2.imshow('Calibration Color2', image3)
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    iterations += 1

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
