import warnings
# 경고메세지 끄기
warnings.filterwarnings (action='ignore')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/1_라벨링 대기실/제2의나라')

# '동영상 제목' 열에서 유니크한 값 확인
unique_values = df['동영상 제목'].unique()

# 유니크한 값 출력
unique_values

#특정 키워드 영상 지우고, 앞에 라벨 추가
# 제외할 키워드 설정
#exclude_keywords = ['최윤석'] #, '판다스']
exclude_keywords = ['나훈아', '아나운서 ', '블랙핑크', '이비온','덕분에', '마약', '발원지', '원창연', '이강인', '키보드']
#', '각성'], '', '']

# 특정 키워드가 들어간 행을 제외
filtered_df = df[~df['동영상 제목'].str.contains('|'.join(exclude_keywords))]

# 데이터프레임에 '분류' 열을 맨 처음 열로 추가합니다.
filtered_df.insert(0, '게임', '제2의나라')
filtered_df.insert(1, '분류', '기초')

# CSV 파일로 저장할 경로와 파일명 설정
save_path = '제2의나라 기초 라벨링.csv'

# filtered_df 데이터 프레임을 CSV 파일로 저장
filtered_df.to_csv(save_path, index=False)

print("2차 가공이 끝났습니다.")