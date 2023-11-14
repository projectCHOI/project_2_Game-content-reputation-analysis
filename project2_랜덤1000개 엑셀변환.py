#자연어 처리 과정 감정분석 단계에서 편의 성을 위해서 사용한다.

import pandas as pd
# CSV 파일의 경로를 지정합니다.
file_path = "/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/제목_키워드 분류.csv"
# CSV 파일을 불러옵니다.
data = pd.read_csv(file_path)

# 겹치지 않는 1000개의 행을 랜덤하게 5번 선택하고 CSV 파일로 저장.
# exclude_indices = 제외할_인덱스
# sampled_indices = 선택한_인덱스

for i in range(5):
    # 이전에 선택한 인덱스 제외
    if i > 0:
        exclude_indices = sampled_indices.flatten()
        data = data.drop(exclude_indices)

    # 1000개의 행을 랜덤하게 선택
    random_sample = data.sample(n=1000, random_state=i)

    # 선택한 인덱스 추적
    sampled_indices = random_sample.index.values.reshape(-1, 1)

    # CSV로 저장
    csv_save_path = f"/content/drive/MyDrive/2.project_2_YouTube 크롤링/랜덤_1000개_{i+1}.csv"
    random_sample.to_csv(csv_save_path, index=False)
    print(f"랜덤 샘플 {i+1}을 CSV 파일로 저장했습니다.")

    # CSV 파일을 Excel 파일로 변환
    excel_save_path = f"/content/drive/MyDrive/2.project_2_YouTube 크롤링/랜덤_1000개_{i+1}.xlsx"
    random_sample.to_excel(excel_save_path, index=False)
    print(f"랜덤 샘플 {i+1}을 Excel 파일로 저장했습니다. 경로: {excel_save_path}")
