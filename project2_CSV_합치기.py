#드라이버 연결
import warnings
warnings.filterwarnings (action='ignore')

#지정 폴더 안에 csv 전부 합치기
import pandas as pd
import glob
# 디렉토리 내의 모든 CSV 파일을 읽어옵니다.
all_files = glob.glob('*.csv')
# 빈 DataFrame을 생성합니다.
combined_data = pd.DataFrame()
# 모든 CSV 파일을 순회하며 데이터를 합칩니다.
for file in all_files:
    data = pd.read_csv(file)
    combined_data = combined_data.append(data, ignore_index=True)

# 결과를 하나의 CSV 파일로 저장하거나 다른 작업을 수행합니다.
# combined_data.to_csv('컨텐츠-음악', index=False)

# 합친 데이터프레임을 출력하려면 다음과 같이 할 수 있습니다.
#print(combined_data)
print("합치기 성공!")

##합친 데이터의 특정 제목의 유튜브 지우기
# '동영상 제목' 열에서 유니크한 값 확인
unique_values = combined_data['동영상 제목'].unique()
# 유니크한 값 출력 확인
unique_values
# 제외할 키워드 설정
exclude_keywords = ['구글환불대행'] #, '판다스']

# 특정 키워드가 들어간 행을 제외
filtered_df = combined_data[~combined_data['동영상 제목'].str.contains('|'.join(exclude_keywords))]

# 데이터프레임에 '분류' 열을 맨 처음 열로 추가합니다.
filtered_df.insert(0, '게임', '검은사막')
filtered_df.insert(1, '분류', 'BM')

# CSV 파일로 저장할 경로와 파일명 설정
save_path = '검은사막 BM 라벨링.csv'

# filtered_df 데이터 프레임을 CSV 파일로 저장
filtered_df.to_csv(save_path, index=False)

print("특정 제목을 지우는 2차 가공이 끝났습니다.")

