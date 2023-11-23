# CSV불러오기
data = a

# 특정 열만 불러오기
selected_columns = ['labels', '동영상 제목', '댓글', '댓글 작성일']
df_new = df[selected_columns]

#터미널 설치
#pip install tqdm
#pip install konlpy

import pandas as pd
import re

# 한글, 영어, 숫자, 공백을 제외한 문자에 일치하는 정규 표현식
regex = r'[^\sㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9]'

# 이모티콘과 특수문자가 포함된 '댓글'의 개수 계산
count_special_char = df_new['댓글'].apply(lambda x: bool(re.search(regex, x)) if isinstance(x, str) else False).sum()
count_special_char

# 특수문자를 포함하는 정규 표현식
regex = r'[^\w\s]'

# 특수문자가 포함된 '댓글'의 개수 계산
count_special_char_comments = df_new['댓글'].apply(lambda x: bool(re.search(regex, x)) if isinstance(x, str) else False).sum()
count_special_char_comments

#한번 더
# 한글, 영어, 숫자, 기본 공백 이외의 문자 및 \r, \n, \t를 포함하는 정규 표현식
regex_non_kor_eng_space = r'[^\sㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9]|\r|\n|\t'

# 한글 또는 영어가 포함된 행만 필터링
df_filtered = df_new[df_new['댓글'].apply(lambda x: isinstance(x, str) and bool(re.search(r'[ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z]', x)))].copy()

# 이모티콘, 특수문자, \r, \n, \t를 공백으로 제거
df_filtered['PRO'] = df_filtered['댓글'].apply(lambda x: re.sub(regex_non_kor_eng_space, ' ', x))

# 결과 확인
df_filtered

# 데이터 프레임을 CSV 파일로 저장
pro = '/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/정규표현식 적용.csv'

# UTF-8 인코딩을 지정하여 파일 저장
df_filtered.to_csv(pro, index=False, encoding='utf-8')

print(f'파일 저장 완료: {pro}')