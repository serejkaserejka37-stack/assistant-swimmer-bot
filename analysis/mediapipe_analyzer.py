import cv2
import mediapipe as mp
import numpy as np
from utils.formatters import format_analysis_result

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    pose = mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.7
    )
    
    errors = []
    frame_count = 0
    valid_frames = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)
        
        if results.pose_landmarks:
            valid_frames += 1
            # Анализ позы (упрощенный)
            landmarks = results.pose_landmarks.landmark
            
            # Пример анализа: угол руки
            if valid_frames % 10 == 0:  # Анализируем каждые 10 кадров
                if check_arm_angle(landmarks) < 80:
                    errors.append("Низкий угол захвата руки")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    summary = f"Анализировано {valid_frames} кадров из {frame_count}"
    recommendations = generate_recommendations(errors)
    
    return {
        'summary': summary,
        'errors': '\n'.join(errors) if errors else "Ошибок не найдено",
        'recommendations': recommendations
    }

def check_arm_angle(landmarks):
    # Упрощенный расчет угла (заменить на реальный)
    return np.random.uniform(60, 120)

def generate_recommendations(errors):
    if not errors:
        return "Отличная техника! Продолжай в том же духе."
    
    recs = []
    for error in errors:
        if "руки" in error:
            recs.append("Упражнение: 'Ловля' - тренируй захват воды")
    
    return '\n'.join(recs) if recs else "Общие рекомендации по технике"
