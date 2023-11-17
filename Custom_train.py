# train 폴더와 test 폴더 생성 확인
from glob import glob

train_img_list = glob('C:\\Users\\leesc\\Downloads\\HardHat\\train\\images\\*.jpg')
train_txt_list = glob('C:\\Users\\leesc\\Downloads\\HardHat\\train\\images\\labels\\*.txt')
test_img_list = glob('C:\\Users\\leesc\\Downloads\\HardHat\\test\\images\\*.jpg')
test_txt_list = glob('C:\\Users\\leesc\\Downloads\\HardHat\\test\\images\\labels\\*.txt')

print(len(train_img_list), len(test_img_list))
print(len(test_txt_list), len(test_img_list))

# train 데이터와 val 데이터 나누기
from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(train_img_list, test_size=0.2, random_state=2000)
print(len(train_img_list), len(val_img_list))

# 파일 쓰기
with open('C:\\Users\\leesc\\PycharmProjects\\ultralytics\\train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('C:\\Users\\leesc\\PycharmProjects\\ultralytics\\val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')

# yaml 파일 수정
import yaml

with open('C:\\Users\\leesc\\PycharmProjects\\ultralytics\\data.yaml', 'r') as f:
  data = yaml.full_load(f) # yaml.load -> yaml.full_load
print(data)

data['train'] = 'C:\\Users\\leesc\\PycharmProjects\\ultralytics\\train.txt'
data['val'] = 'C:\\Users\\leesc\\PycharmProjects\\ultralytics\\val.txt'

with open('C:\\Users\\leesc\\PycharmProjects\\ultralytics\\data.yaml', 'w') as f:
  yaml.dump(data, f)
