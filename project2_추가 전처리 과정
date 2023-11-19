import pandas as pd
import re

# CSV 파일 불러오기
file_path = 'your_csv_file.csv'  # 파일 경로를 적절히 수정하세요
data = pd.read_csv(file_path)

# 특정 행 가져오기 'A'와 'B' 열 가져오기
column_a = data['A']
column_b = data['B']

# 특정행 'B' 열에서 영어와 한글만 추출하여 새로운 'C' 열에 저장
def extract_letters(text):
    # 정규 표현식을 사용하여 문자열에서 영어와 한글만 추출합니다.
    result = re.sub(r'[^a-zA-Z가-힣]+', '', text)
    return result

data['C'] = column_b.apply(extract_letters)

# 작업을 끝낸 CSV 파일로 저장
output_file_path = 'output.csv'  # 출력 파일 경로를 적절히 수정하세요
data.to_csv(output_file_path, index=False)

print(f"작업이 완료되었습니다. 결과는 {output_file_path}에 저장되었습니다.")
