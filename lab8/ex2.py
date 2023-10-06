import cv2
import time


def detect_label_on_video(template_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    cap = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for scale in [0.5, 0.8, 1.0, 1.2, 1.5]:
            resized_template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
            result = cv2.matchTemplate(gray_frame, resized_template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            threshold = 0.8
            if max_val > threshold:
                top_left = max_loc
                bottom_right = (top_left[0] + resized_template.shape[1], top_left[1] + resized_template.shape[0])

                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

                label_coordinates = f"({top_left[0]}, {top_left[1]})"
                if i % 5 == 0:
                    a = top_left[0]
                    b = top_left[1]
                    print(a, b)

                cv2.putText(frame, label_coordinates, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    label_template_path = 'ref-point.jpg'
    detect_label_on_video(label_template_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
