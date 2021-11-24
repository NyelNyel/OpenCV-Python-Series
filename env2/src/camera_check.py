def camer():
    import cv2

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame
        ret, img = cap.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", img)
        cv2.imshow('Gray Image', gray)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (10,159,255), 2)

        # Display
        cv2.imshow('Webcam Check', img)

        # Stop if escape key is pressed
        if cv2.waitKey(20) & 0xFF == ord('q'):
            img_name = "opencv_frame_{}.png".format(cap)
            cv2.imwrite(img_name, img)
            print("{} written!".format(img_name))
            cap +=1
            break

    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()