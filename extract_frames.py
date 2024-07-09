import cv2

video_path = "/home/Ascent-openMVG/fireplace.MOV"
video_cap = cv2.VideoCapture(video_path)

fps = video_cap.get(cv2.CAP_PROP_FPS)
frame_count = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
num_frames_to_use = round(frame_count / (fps / 2.0))

print((fps, frame_count, num_frames_to_use))

frames_to_use = [round(i * frame_count / (num_frames_to_use - 1)) for i in range(num_frames_to_use)]
frame_count = 0

image_save_path = "/home/Ascent-openMVG/SfM_data/images"

while video_cap.isOpened():
    ret, frame = video_cap.read()
    if not ret:
        break
    if frame_count not in frames_to_use:
        frame_count += 1
        continue
    cv2.imwrite(f"{image_save_path}/frame_{frame_count}.jpg", frame)
    frame_count += 1