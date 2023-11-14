#Excel > CSV 편의성 이슈로 분리함.
from google.colab import drive
import pandas as pd

# Excel 파일의 경로를 지정합니다.
excel_file_path = "/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/CSV_1000/랜덤_5000개_GPT4.xlsx"

# Excel 파일을 불러옵니다.
excel_data = pd.read_excel(excel_file_path)

# CSV 파일로 저장할 경로와 파일명 설정
csv_save_path = "/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/랜덤_5000개_GPT4.csv"

# Excel 데이터를 CSV 파일로 저장합니다.
excel_data.to_csv(csv_save_path, index=False)

# 결과를 확인합니다.
print("Excel 파일을 CSV 파일로 변환 및 저장했습니다.")

# CSV 파일의 경로를 지정합니다.
csv_file_path = "/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/랜덤_5000개_GPT4.csv"

# CSV 파일을 불러옵니다.
csv_data = pd.read_csv(csv_file_path)

# 결과 확인
#print(csv_data.head())
csv_data.head(500)