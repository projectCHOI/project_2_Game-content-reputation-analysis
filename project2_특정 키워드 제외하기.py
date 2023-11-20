#특정 키워드 제외하기

import pandas as pd

file_path = '231115-296583_댓글.csv'

# CSV 파일을 으로 불러오기
try:
    data = pd.read_csv(file_path)
except Exception as e:
    print(f"파일 로딩 중 오류 발생: {e}")
    exit()

# 확인용 print
print(data.head())

# 제외할 키워드 목록
exclude_keywords = ['오버워치', '롤']

# 원하는 열에서 exclude_keywords에 해당하는 키워드가 있는 행 제외하기
try:
    filtered_df = data[~data['keyword 제외'].str.contains('|'.join(exclude_keywords), na=False)]
except Exception as e:
    print(f"필터링 중 오류 발생: {e}")
    exit()

# 확인용 print
print(filtered_df.head())

# CSV 파일로 저장
save_path = '2차-전처리-키워드제외.csv'
filtered_df.to_csv(save_path, index=False)
print("2차 전처리 성공된 파일 저장 : ", save_path)
