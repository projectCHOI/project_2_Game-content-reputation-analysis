# Jupyter환경에서 진행 해야한다.
# 폰트도 Jupyter에 있음

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as font_manager

# 사용자 입력을 받는 함수
def get_scores(category_name):
    while True:
        try:
            # 사용자에게 카테고리별 점수를 입력받음
            scores = input(f"'{category_name}'의 값 입력 (음악, 시스템, BM, 운영, 게임성, 그래픽 순으로 공백으로 구분하여 입력): ")
            # 입력받은 값을 공백으로 구분하여 숫자 배열로 변환
            scores = [int(score) for score in scores.split()]
            if len(scores) != 6:
                raise ValueError("정확히 6개의 숫자를 입력해야 합니다.")
            return scores
        except ValueError as e:
            print("잘못된 입력입니다. 다시 시도해주세요. 오류:", e)

# 경로는 실제 폰트 파일 위치에 따라.
# NanumGothic 폰트 설정
font_path = 'NanumGothic.ttf'
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'

# 데이터 설정
categories = ["음악", "시스템", "BM", "운영", "게임성", "그래픽"]
advantages = get_scores('긍정')
disadvantages = get_scores('부정')
neutral = get_scores('중립')
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# 점수 배열의 마지막 요소를 다시 추가하여 배열의 길이를 angles 배열과 일치시킵니다.
advantages += [advantages[0]]
disadvantages += [disadvantages[0]]
neutral += [neutral[0]]

# 그래프 초기화
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 축의 최대값을 20으로 설정 및 5단위로 설정
ax.set_ylim(0, 20)
ax.set_yticks(np.arange(0, 21, 5))

# 장점(긍정), 단점(부정), 중립의 영역을 채우기
ax.fill(angles, advantages, color='blue', alpha=0.25)
ax.fill(angles, disadvantages, color='red', alpha=0.25)
ax.fill(angles, neutral, color='green', alpha=0.25)

# 각 점수에 대한 마커 추가
for i in range(len(categories)):
    ax.plot(angles[i], advantages[i], 'o', color='green', markersize=8)   # 긍정
    ax.plot(angles[i], disadvantages[i], '^', color='red', markersize=8)  # 부정
    ax.plot(angles[i], neutral[i], 's', color='blue', markersize=8)       # 중립

# 카테고리 레이블
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontdict={'fontsize': 12, 'fontfamily': 'NanumGothic'})

# 제목과 범례
ax.set_title("GPT-4 학습", size=20, fontfamily='NanumGothic')
ax.legend(['긍정', '부정', '중립'], loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()