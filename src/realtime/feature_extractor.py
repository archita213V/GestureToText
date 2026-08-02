class FeatureExtractor:
    def extract(self, hand_landmarks):
        wrist = hand_landmarks.landmark[0]
        features = []
        for landmark in hand_landmarks.landmark:

            features.append(landmark.x - wrist.x)
            features.append(landmark.y - wrist.y)
            features.append(landmark.z - wrist.z)
            
        return features