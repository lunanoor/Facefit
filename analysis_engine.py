import cv2
import mediapipe as mp
import numpy as np

class FaceAnalyzer:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

    def analyze_image(self, image_bytes):
        # Convert image bytes to numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return None

        # Convert to RGB for MediaPipe
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_image)

        if not results.multi_face_landmarks:
            return None

        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = image.shape

        # Face Shape Analysis
        shape = self._determine_face_shape(landmarks, w, h)
        
        # Skin Tone Analysis
        skin_tone = self._determine_skin_tone(image, landmarks, w, h)

        return {
            "face_shape": shape,
            "skin_tone": skin_tone
        }

    def _determine_face_shape(self, landmarks, w, h):
        # Key landmarks for face shape
        # Chin: 152
        # Forehead top: 10
        # Left cheek: 234
        # Right cheek: 454
        # Jawline: 132, 361 (approx)

        chin = landmarks[152]
        forehead = landmarks[10]
        left_cheek = landmarks[234]
        right_cheek = landmarks[454]

        face_width = abs(right_cheek.x - left_cheek.x) * w
        face_height = abs(chin.y - forehead.y) * h

        # Ratio
        ratio = face_height / face_width

        # Simplified logic for demo purposes
        # Real logic would involve jaw width, forehead width comparison etc.
        
        # Checking jaw width (using approximate jaw landmarks)
        # Left jaw: 58, Right jaw: 288
        jaw_width = abs(landmarks[288].x - landmarks[58].x) * w
        forehead_width = abs(landmarks[338].x - landmarks[109].x) * w # Approx forehead width

        shape = "Oval" # Default
        
        if ratio > 1.5:
            if jaw_width >= face_width * 0.9: 
                shape = "Oblong"
            else:
                shape = "Oval"
        elif ratio < 1.1:
            shape = "Round"
        else:
            if jaw_width >= forehead_width * 1.05:
                shape = "Square" # Strong jaw
            elif jaw_width <= forehead_width * 0.8:
                shape = "Heart"
            elif face_width > forehead_width and face_width > jaw_width:
                 shape = "Diamond"
            else:
                 shape = "Oval" # Fallback

        return shape

    def _determine_skin_tone(self, image, landmarks, w, h):
        # Extract skin patch from cheek area
        # Left cheek area around landmark 116 (approx)
        cx, cy = int(landmarks[116].x * w), int(landmarks[116].y * h)
        
        # Get a small patch
        patch_size = 10
        y1 = max(0, cy - patch_size)
        y2 = min(h, cy + patch_size)
        x1 = max(0, cx - patch_size)
        x2 = min(w, cx + patch_size)
        
        patch = image[y1:y2, x1:x2]
        
        if patch.size == 0:
            return "Medium"

        # Calculate average color in LAB space for L (Lightness)
        lab_patch = cv2.cvtColor(patch, cv2.COLOR_BGR2LAB)
        l_channel, a_channel, b_channel = cv2.split(lab_patch)
        
        avg_l = np.mean(l_channel)
        
        # Very simplified categorization based on Lightness
        if avg_l > 180:
            tone = "Fair"
        elif avg_l > 130:
            tone = "Medium"
        else:
            tone = "Dark"
            
        # Determine undertone (Warm/Cool) using A and B channels
        # A: Green-Red, B: Blue-Yellow
        avg_a = np.mean(a_channel)
        avg_b = np.mean(b_channel)
        
        undertone = "Neutral"
        if avg_b > avg_a + 5: # More yellow
            undertone = "Warm"
        elif avg_a > avg_b + 5: # More red/pink (simplified)
            undertone = "Cool"
            
        return f"{tone} ({undertone})"
