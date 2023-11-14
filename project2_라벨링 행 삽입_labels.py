import pandas as pd
# CSV 파일의 경로를 지정합니다.
file_path = "/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/13종게임_39계열_358713개댓글_수집"
# CSV 파일을 불러옵니다.
data = pd.read_csv(file_path)

# 새로운 값을 설정합니다. 여기서는 빈 문자열로 설정합니다.
new_value = ' '

# 기존 "labels" 열의 값을 업데이트합니다.
data.insert(0, 'labels', new_value)

# 결과를 확인합니다.
# print(data.head())
data.head()

# 수정된 데이터프레임을 새로운 CSV 파일로 저장할 경로와 파일명 설정
save_path = '/content/drive/MyDrive/2.project_2_YouTube 크롤링/358713댓글_labels값 추가.csv'

# 수정된 데이터프레임을 CSV 파일로 저장합니다.
data.to_csv(save_path, index=False)

print("새로운 열을 추가하고 저장했습니다.")