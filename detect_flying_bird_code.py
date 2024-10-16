import ultralytics
from ultralytics import YOLO

# YOLOv11m 모델 불러오기
model = YOLO('yolo11m.pt')  

# 데이터셋 경로 설정
data_path = '/mnt/storage/chaeyoung/YSC bird.v1i.yolov11/data.yaml'

# 모델 훈련
model.train(
    data=data_path,  # YAML 파일 경로
    epochs=100,      # 학습할 epoch 수
    imgsz=960,      # 입력 이미지 해상도 (높은 해상도 사용)
    batch=16,        # 배치 크기 (GPU 성능을 고려하여 설정)
    workers=8,       # 데이터 로드할 때 사용할 CPU 쓰레드 수
    optimizer='Adam', # Adam 옵티마이저 사용
    device=0,        # GPU 사용
    lr0=0.001,       # 초기 학습률
    weight_decay=0.0005, # 가중치 감소 (정규화)
    patience=20,     # 조기 종료를 위한 patience 값
    augment=True     # 데이터 증강 적용
)

# 훈련 후 최종 결과 확인
model.val()  # validation 데이터셋 평가
