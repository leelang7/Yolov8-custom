import os

YOLOV8_LABEL_ROOT = 'C:\\Users\\leesc\\PycharmProjects\\ultralytics\\runs\\detect\\predict2\\labels\\'  # yolov8이 내보낸 추론 이미지의 txt
DATASET_LABEL_ROOT = 'C:\\Users\\leesc\\PycharmProjects\\ultralytics\\results\\'   # 사람이 없는 데이터셋의 라벨 경로

yolo_file = os.listdir(YOLOV8_LABEL_ROOT)

# .txt로 끝나는 파일 탐색
for file_name in yolo_file:

    if not file_name.endswith(".txt"):
        continue

    file_path = YOLOV8_LABEL_ROOT + file_name
    with open(file_path, "r") as f:
        for line in f.readlines():
            # 0 : person 을 다른 class로 일괄 변경
            if line.split()[0] == '0':
                line = list(line)
                line[0] = '1'
                line = ''.join(line).strip()
                print(line)
                # 주석파일에 추가
                data_path = DATASET_LABEL_ROOT + file_name
                with open(data_path, "a") as fd:
                    fd.write("\n")
                    fd.write(line)
                    #line.strip() # 빈 줄 제거