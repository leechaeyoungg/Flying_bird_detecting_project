import os
import shutil
from glob import glob

# 데이터셋 경로 설정
base_dir = r"H:\이채영님\AirBirds"
train_dir = os.path.join(base_dir, "structured_dataset", "train")
valid_dir = os.path.join(base_dir, "structured_dataset", "valid")
test_dir = os.path.join(base_dir, "structured_dataset", "test")

# 폴더 생성
os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(valid_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(valid_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "labels"), exist_ok=True)

# 이미지와 라벨 경로 설정
image_dirs = [os.path.join(base_dir, f"images{i}") for i in range(10)]
label_dirs = [os.path.join(base_dir, f"labels{i}", f"labels{i}") for i in range(10)]

# 전체 이미지 파일 리스트 불러오기
all_images = []
for image_dir in image_dirs:
    all_images.extend(glob(os.path.join(image_dir, "*.png")))

# 데이터셋 분할 비율
train_ratio = 0.8
valid_ratio = 0.1
test_ratio = 0.1

# 파일 개수 확인
total_images = len(all_images)
train_count = int(total_images * train_ratio)
valid_count = int(total_images * valid_ratio)

# train, valid, test 분할
train_images = all_images[:train_count]
valid_images = all_images[train_count:train_count + valid_count]

# 이미지와 라벨 파일 이동 함수
def move_files(image_list, target_image_dir, target_label_dir, label_dirs):
    for image_path in image_list:
        # 이미지 파일명과 라벨 파일명 설정
        image_name = os.path.basename(image_path)
        label_name = os.path.splitext(image_name)[0] + ".txt"
        
        # 라벨 파일 찾기
        label_path = None
        for label_dir in label_dirs:
            potential_path = os.path.join(label_dir, label_name)
            if os.path.exists(potential_path):
                label_path = potential_path
                break
        
        # 이미지와 라벨 파일 이동
        if label_path:
            shutil.move(image_path, os.path.join(target_image_dir, image_name))
            shutil.move(label_path, os.path.join(target_label_dir, label_name))

# Train 파일 이동
move_files(train_images, os.path.join(train_dir, "images"), os.path.join(train_dir, "labels"), label_dirs)

# Valid 파일 이동
move_files(valid_images, os.path.join(valid_dir, "images"), os.path.join(valid_dir, "labels"), label_dirs)

# Test는 기존 test 폴더에서 가져오기
test_image_dirs = [
    r"H:\이채영님\AirBirds\test\images\test_D02_20210628090856",
    r"H:\이채영님\AirBirds\test\images\test_D02_20210721142744"
]
test_label_dirs = [
    r"H:\이채영님\AirBirds\test\labels\labels_test_D02_20210628090856",
    r"H:\이채영님\AirBirds\test\labels\labels_test_D02_20210721142744"
]

# Test 데이터셋 이동
for test_image_dir, test_label_dir in zip(test_image_dirs, test_label_dirs):
    test_images = glob(os.path.join(test_image_dir, "*.png"))
    move_files(test_images, os.path.join(test_dir, "images"), os.path.join(test_dir, "labels"), [test_label_dir])

print("데이터셋 구성 완료")
