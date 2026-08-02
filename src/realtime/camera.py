import cv2
class Camera:
    def __init__(self, camera_index=0):
        """
        Initialize the webcam.
        camera_index = 0 means the default webcam.
        """
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Error: Could not open webcam.")
    def get_frame(self):
        """
        Capture a single frame from the webcam.
        Returns:
            ret   -> True if frame captured successfully
            frame -> Captured image
        """
        ret, frame = self.cap.read()

        if not ret:
            return None
        return frame
    def release(self):
        """
        Release webcam and close all OpenCV windows.
        """
        self.cap.release()
        cv2.destroyAllWindows()