from sahi import AutoDetectionModel
import cv2
from ultralytics import YOLO
import os
from utils_sahi import get_model_with_sahi_cuda,get_model_with_sahi_cpu,get_sahi_prediction,get_yolo_prediction,merge_img_horizen,test_performance,get_video_sahi_prediction,get_video_prediction_with_fallback

"""
#image_test
yolov11_path='Player_Tracking/detect/train/weights/best.pt'
model = get_model_with_sahi_cpu(yolov11_path)

input_path=r'D:\SIT220\Player_Tracking\test_background.jpg' 
out_path=r'D:\SIT220\Player_Tracking\output' 

out1 = os.path.join(out_path, "small-vehicles1.jpeg")
test_performance(input_path,out1,model,480,480)
"""


video_path = r"/applications/Tinkle/7af2646350d53c554cab6287094d384d.mp4" 
out_path= r'/applications/Tinkle/output' 
output_video_path = os.path.join(out_path, "output_video2.mp4")

yolov11_path='/applications/Tinkle/runs/detect/train/weights/best.pt'
# sahi_model= get_model_with_sahi_cpu(yolov11_path)
sahi_model= get_model_with_sahi_cuda(yolov11_path)
yolo_model = YOLO(yolov11_path)
"""
#video_test_sahi_only
get_video_sahi_prediction(
    video_path, 
    sahi_model, 
    slice_height=512, 
    slice_width=512, 
    overlap_height_ratio=0.1, 
    overlap_width_ratio=0.1, 
    output_video_path=output_video_path
)
"""


#video_test_sahi_partly
get_video_prediction_with_fallback(
    video_path, 
    sahi_model, 
    yolo_model,
    slice_height=480, 
    slice_width=480, 
    overlap_height_ratio=0.2, 
    overlap_width_ratio=0.2, 
    output_video_path=output_video_path,
    dis_thres=100
)






