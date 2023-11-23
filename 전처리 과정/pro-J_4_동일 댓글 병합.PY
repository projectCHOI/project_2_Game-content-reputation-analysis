# CSV불러오기
df

# 'PRO' 열을 기준으로 행 병합, 첫 번째 값을 유지
df_merged = df.groupby('PRO').first().reset_index()

# 병합 결과 확인
df_merged

# 병합된 데이터프레임을 Excel 파일로 저장
df_merged.to_excel('/content/drive/MyDrive/EE.xlsx', index=False)