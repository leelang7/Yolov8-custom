import os

YOLOV8_LABEL_ROOT = f"E:\AI_Project\Smart_Construction_Project\inference\output\\"  # yolov8이 내보낸 추론 이미지의 txt
DATASET_LABEL_ROOT = f"E:\AI_Project\AI_Learning\Dataset\VOC2028\Labels\\"  # 사람이 없는 원본 데이터셋의 라벨 경로

yolo_file = os.listdir(YOLOV8_LABEL_ROOT)

# .txt로 끝나는 파일 탐색
for file_name in yolo_file:

    if not file_name.endswith(".txt"):
        continue

    file_path = YOLOV8_LABEL_ROOT + file_name
    with open(file_path, "r") as f:
        for line in f.readlines():

            # 0 -> person 데이터만 추출
            if line.split()[0] != '0':
                continue

            data_path = DATASET_LABEL_ROOT + file_name
            print(data_path)
            # 주석파일에 추가
            with open(data_path, "a") as fd:
                fd.write(line)
