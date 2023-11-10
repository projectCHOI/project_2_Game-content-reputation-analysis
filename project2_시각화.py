#주피터 환경이 편하다.

# 나눔고딕 폰트 설치
#!sudo apt-get install -y fonts-nanum
#!sudo fc-cache -fv
#!rm ~/.cache/matplotlib -rf

#시작하기
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

# 나눔고딕 폰트 설치
#!apt-get -qq -y install fonts-nanum

# 나눔고딕 폰트 경로 설정
path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = fm.FontProperties(fname=path, size=10).get_name()
plt.rc('font', family=font_name)

#불러오기
df = pd.read_csv("/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/predictions.csv")

# 시각화하기
# "긍정"과 "부정"의 빈도 계산
sentiment_counts = df["예측 감정"].value_counts()

# 파이 차트를 그리기 위한 데이터 준비
labels = ["긍정", "부정"]
sizes = [sentiment_counts.get("긍정", 0), sentiment_counts.get("부정", 0)]

# 파이 차트 그리기
fig, axs = plt.subplots(1, figsize=(15, 5))

axs.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs.set_title('메이플 음악')

plt.show()