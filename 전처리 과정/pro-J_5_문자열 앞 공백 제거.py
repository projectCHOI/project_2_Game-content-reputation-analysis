# PRO 열의 앞쪽 공백 제거
df['PRO'] = df['PRO'].str.lstrip()

# 문자열 길이가 10개 미만인 행 제거
df = df[df['PRO'].str.len() >= 10]

# 문자열 길이가 100개를 초과하는 행 제거
df = df[df['PRO'].str.len() <= 100]

# PRO 열의 데이터가 동일한 경우 하나로 병합
df = df.groupby('PRO').first().reset_index()

# name 열의 NaN 값을 공백으로 대체
df['name'] = df['name'].fillna('')

# PRO 열을 데이터프레임의 마지막으로 이동
pro_column = df['PRO']
df = df.drop('PRO', axis=1)
df['PRO'] = pro_column

# 새 열 'theme'를 세 번째 열로 추가
df.insert(2, 'theme', '')

# 변경된 데이터 확인
# print(df.head())
df