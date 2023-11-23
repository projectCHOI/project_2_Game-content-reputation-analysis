# CSV불러오기
data = a

# '동영상 제목' 열에서 유니크한 값 추출
unique_titles = df['동영상 제목'].unique()
# 유니크한 값들로 새로운 데이터프레임 생성
unique_titles_df = pd.DataFrame(unique_titles, columns=['동영상 제목'])
unique_titles_df

# 제거하고 싶은 키워드 리스트
keywords_to_remove = ['각성닌자', '활대', '에임으로', '무선으로', 'Shorts',
                      'N년차가', '스킨이 타격감이', '소울이터', 'SBS', '말이 필요없는',
                      '발헤임', '공감주의', '시청자사연', '알렉산더를', '손소리',
                      'SUB', '보스돌이', '엘든링', '광고', '구글',
                      '도깨비', '우리말더빙', '젤다', '도트작품', '제보영상',
                      '알아볼께요', '각성레이드', '서버터짐', '롤', '매드형',
                      '김창옥', '나라카', 'CHOSUN', '씨네21', '유퀴즈',
                      '슈퍼히어러', '프리한19', '응답하라', '종결합니다', '대해적',
                      '초능력자', '전승닌자', '불후의 명곡', '청담샵', 'Wizardry',
                      '마약왕', '불후의명곡', '정국', '바람의 노래', '바람의 미래로',
                      '엘리오스의전설', '넷게임즈', '나혼자만레벨업', '테일즈위버', '비켄디',
                      '모배', 'MISSIONS', '수면유도', '에임 상승', '무협',
                      '가사있는노래', '부스터', '개발자 서신', '게임 달력', 'Zelda',
                      '포켓몬', '영화리뷰', '긴급', '기뉴다', '구스따라',
                      '김제국', '', '', '', '',
                      '', '', '', '', '',
                      '', '', '', '', '',
                      '', '', '', '', '',]

# 정규 표현식으로 여러 키워드 조합
regex_pattern = '|'.join(keywords_to_remove)

# 특정 키워드를 포함하지 않는 행만 필터링
filtered_df = df[~df['동영상 제목'].str.contains(regex_pattern)]

# 결과 출력
filtered_df

# CSV 파일로 저장할 경로 지정
output_file_path = '/content/drive/MyDrive/엑셀로 변환.csv'

# 데이터프레임을 CSV 파일로 저장
filtered_df.to_csv(output_file_path, index=False)

# 저장 완료 메시지 출력
print(f'File saved successfully at {output_file_path}')