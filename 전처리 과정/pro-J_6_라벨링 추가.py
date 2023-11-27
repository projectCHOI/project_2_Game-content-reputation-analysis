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
#combined_data.to_csv('공백추가', index=False)

# 합친 데이터프레임을 출력하려면 다음과 같이 할 수 있습니다.
print(combined_data)
print("합치기 성공!")

# 제외할 키워드 설정
exclude_keywords = ['닌텐도', '문구수정', 'CCTV', '프레스티지', '괴물쥐', '여자친구가', '공군숙소', '발로란트', '근황', '현금으로', '페리시치가',
                    '불화설', '생방도중', '아이폰', '디아블로', '재조합', '부부싸움', '스트리머', '환불소송', '민사소송', '토스', '한국', '모먼트',
                    '비트코인으로', '컴퓨터로', '다크소울', '후진이', '바하8', '좋더라', '다크웹', '로벅스', '사용금지 ', '자녀환불', '여자',
                    '이근대위', '유튜버', '홍진영','생방송', '카람빗', '기만', '상자깡', '박아버린', '무료로벅스', '연합뉴스', '청약철회',
                    '리얼함', '오마이갓', '오디움', '놀장강이', '중2병', '당신이', '입고', '로블록스', '더블비', '무료주차', '플스5',
                    '중소와', '선생님','당하기', '누나', '메창의', '잼민이', '잼민이가', '노브라로', '유일한', '환불받기']

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