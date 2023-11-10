# csv불러오기
import warnings
warnings.filterwarnings (action='ignore')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/2.project_2_YouTube 크롤링/게임_크롤링/넥슨_메이플/메이플 음악 2차 가공.csv')

# 터미널 pip install transformers
# 모델 불러오기
import pandas as pd
import torch
from torch.nn import functional as F
from transformers import AutoTokenizer, ElectraForSequenceClassification
import numpy as np
import time

# GPU 사용 여부 확인
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"사용하고 있는 건? → {device}")

# 모델 불러오기
model = ElectraForSequenceClassification.from_pretrained("monologg/koelectra-base-v3-discriminator").to(device)
model.load_state_dict(torch.load("/content/drive/MyDrive/2.project_2_YouTube 크롤링/model.pt"), strict=False)
model.eval()

# 토크나이저 설정
tokenizer = AutoTokenizer.from_pretrained("monologg/koelectra-small-v2-discriminator")

# 댓글 예측 함수 정의
def predict_comments(df):
    inputs = tokenizer(df["댓글"].tolist(), return_tensors='pt', truncation=True, max_length=256, pad_to_max_length=True, add_special_tokens=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = F.softmax(outputs.logits, dim=1)
    _, predicted_labels = torch.max(predictions, 1)
    return predicted_labels.cpu().tolist()

# 진행상황 출력
def print_progress(count, total, start_time):
    percent = count / total * 100
    elapsed_time = time.time() - start_time
    print(f"{count} / {total}({percent:.2f}%) ({elapsed_time:.2f} seconds)")

# 자료가 1만개가 넘어서 분배해서 돌려야함
# 댓글을 500개씩 split
df_split = np.array_split(df, len(df) // 500 + 1)

# 진행시간 측정
start_time = time.time()

# 각 split된 데이터프레임의 댓글 예측
predictions_list = []
for i, df_split_item in enumerate(df_split):
    predictions_list.append(predict_comments(df_split_item))
    print_progress(i + 1, len(df_split), start_time)

# 예측 결과 합치기
predictions_df = np.concatenate(predictions_list)

# 예측 결과 출력
print("댓글 예측 결과:", predictions_df)

# 예측 결과를 "긍정" 또는 "부정"으로 변환하는 함수 정의
def convert_to_sentiment(predictions):
    sentiment_labels = ["부정", "긍정"]
    return [sentiment_labels[prediction] for prediction in predictions]

# 예측 결과를 "긍정" 또는 "부정"으로 변환
sentiments_df = convert_to_sentiment(predictions_df)

# 예측 결과를 데이터프레임에 추가
df["예측 감정"] = sentiments_df

df.to_csv('predictions.csv', index=False, encoding='utf-8')

