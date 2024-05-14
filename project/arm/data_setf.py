
import os

# 학습 데이터셋의 경로
data = "/Users/heecjang/bksu/project/arm/color_block.v1i.yolov8/data.yaml"

# 학습 설정
epochs = 100
imgsz = 640

# 학습을 시작합니다.
os.system(f"python train.py --img {imgsz} --batch 16 --epochs {epochs} --data {data} --weights yolov5s.pt --name yolov5s_results")