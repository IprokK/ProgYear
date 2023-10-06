import cv2


def fly_on_video(template_path, fly_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    fly = cv2.imread(fly_path, cv2.IMREAD_UNCHANGED)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.8
        if max_val > threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

            fly_resized = cv2.resize(fly, (bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]))

            roi = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

            mask = fly_resized[:, :, 3] / 255.0
            mask_inv = 1.0 - mask

            for c in range(0, 3):
                roi[:, :, c] = roi[:, :, c] * mask_inv + fly_resized[:, :, c] * mask

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    label_template_path = 'ref-point.jpg'
    fly64 = 'fly64.png'

    fly_on_video(label_template_path, fly64)
