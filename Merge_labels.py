import os

YOLOV8_LABEL_ROOT = "C:\\Users\\leesc\\PycharmProjects\\ultralytics\\results\\"  # 사람 클래스가 들어있는 txt
DATASET_LABEL_ROOT = "C:\\Users\\leesc\\PycharmProjects\\ultralytics\\runs\\detect\\predict3\\labels\\"  # 사람이 없는 커스텀 모델이 내보낸 원본 train set 추론 결과 라벨 경로(백업 추천)

yolo_file = os.listdir(YOLOV8_LABEL_ROOT)

# .txt로 끝나는 파일 탐색
cnt = 0
for file_name in yolo_file:

    if not file_name.endswith(".txt"):
        continue

    file_path = YOLOV8_LABEL_ROOT + file_name
    with open(file_path, "r") as f:
        for line in f.readlines():

            # class가 person인 라인만 추출
            if line.split()[0] != '2':
                continue

            data_path = DATASET_LABEL_ROOT + file_name
            print(data_path)
            # 주석파일에 추가
            with open(data_path, "a") as fd:
                cnt += 1
                fd.write(line)
print(f'{cnt} 라인 추가 완료')
