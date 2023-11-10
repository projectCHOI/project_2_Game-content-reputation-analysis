# 시각화 때문에 다운그레이트
#!pip install pandas==1.5.3

# 전처리
# !pip install konlpy

# 형태소 분석기 Mecab
#!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
#%cd Mecab-ko-for-Google-Colab/
#!bash ./install_mecab-ko_on_colab_light_220429.sh

# 형태소 분석기 Mecab
from konlpy.tag import Mecab
tokenizer = Mecab()

# "POS" 열을 생성하고 형태소 분석 결과 저장
for i, row in df.iterrows():
    content = row['댓글']
    if isinstance(content, str):
        nouns = ' '.join(tokenizer.nouns(content))
        df.at[i, 'POS'] = nouns

# 데이터프레임의 구조 확인
print(df[['POS']].head())

# 정규표현식
import re
# 정규 표현식 패턴
regex_pattern = r'\<[^\>]*\>|\&#8203;``&#8203;``【oaicite:0】``&#8203;``&#8203;]*\】|\[[^\)]*\]|\([^\)]*\)|[0-9]*\.[0-9]*?[a-zA-Z]*@[a-zA-Z]*\.[a-zA-Z]*\.?[a-zA-Z]'

# "RE" 열을 생성하고 정규 표현식을 적용하여 분류된 결과 저장
df['RE'] = df['POS'].apply(lambda text: re.sub(regex_pattern, ' ', str(text)))

# 데이터프레임의 구조 확인
print(df[['RE']].head())

# 정규표현식
import re
# 정규 표현식 패턴
regex_pattern = r'\<[^\>]*\>|\&#8203;``&#8203;``【oaicite:0】``&#8203;``&#8203;]*\】|\[[^\)]*\]|\([^\)]*\)|[0-9]*\.[0-9]*?[a-zA-Z]*@[a-zA-Z]*\.[a-zA-Z]*\.?[a-zA-Z]'

# "RE" 열을 생성하고 정규 표현식을 적용하여 분류된 결과 저장
df['RE'] = df['POS'].apply(lambda text: re.sub(regex_pattern, ' ', str(text)))

# 데이터프레임의 구조 확인
print(df[['RE']].head())

# 한글자 제거
# "RE-1" 열을 생성하고 글자 수 1 이하인 데이터를 제거하여 저장
df['RE-1'] = df['RE'].apply(lambda text: ' '.join(word for word in text.split() if len(word) > 1))

# 데이터프레임의 구조 확인
print(df[['RE-1']].head())

# 불용어 처리
stop_pos = ['Noun', 'Josa', 'Alpha', 'Punctuation', 'Suffix']
stop_word = ['은', '는', '이', '가', '을', '를', '에', '에서', '로', '으로',
             '와', '과', '의', '처럼']  # 이어지는 불용어 리스트

# "PRO" 열을 생성하고 불용어 처리된 결과 저장
def preprocess(text):
  text = str(text).split()
  text = [i for i in text if len(i) > 1]
  text = [i for i in text if i not in stop_pos]
  text = [i for i in text if i not in stop_word]
  return text

df['PRO'] = df['RE-1'].apply(preprocess)

# 데이터프레임의 구조 확인
print(df[['PRO']].head())

# 토클리스트 
def make_tokens (df):
    for i, row in df.iterrows():
        if i%100==0:
            print(i, '/',len (df))
        token = preprocess(df ['PRO'][i])
        df['PRO'][i] = ' '.join(token)
    return df
df = make_tokens (df)

# 피키지
# !pip install gensim
# from gensim import corpora
# from gensim.models import LdaModel, TfidfModel

tokenized_docs = df['PRO'].apply(lambda x : x.split())

id2word = corpora. Dictionary (tokenized_docs)
corpus_TDM = [id2word.doc2bow (doc) for doc in tokenized_docs]
tfidf = TfidfModel (corpus_TDM)
corpus_TFIDF = tfidf[corpus_TDM]

n = 30

lda = LdaModel(corpus=corpus_TFIDF,
                id2word=id2word,
                num_topics=n,
                random_state=100)

for t in lda. print_topics():
    print(t)

#예시
# (1, '0.031*"[\'공부\'," + 0.023*"\'저작\']" + 0.019*"\'절벽\']" + 0.019*"[\'금지\'," + 0.016*"\'에피소드\']" + 0.016*"\'적막\'," + 0.016*"\'음악\'," + 0.015*"[\'설원\'," + 0.014*"[\'브금\'," + 0.014*"\'최고\',"')
# (2, '0.026*"[\'시간\'," + 0.024*"\'노래\']" + 0.023*"[\'눈물\'," + 0.023*"[\'플리\'," + 0.022*"\'최고\']" + 0.019*"[\'판테온\'," + 0.019*"\'자체\']" + 0.017*"\'감사\']" + 0.015*"\'신전\'," + 0.014*"[\'메이플\',"')
# (3, '0.025*"\'최고\']" + 0.023*"\'브금\'," + 0.020*"\'눈물\']" + 0.019*"\'메이플\'," + 0.019*"\'편곡\'," + 0.016*"\'눈물흘림\']" + 0.016*"[\'감탄\'," + 0.015*"\'하나하나\'," + 0.014*"[\'아리안트\'," + 0.014*"[\'선정\',"')
# 30개가 출력 된다.

# 판다스 다운그레이트
# !pip install pyLDAvis==3.4.1
# !pip install pandas

import gensim
import pyLDAvis
import pyLDAvis.gensim
import pyLDAvis.gensim_models as gensimvis

# pip install "pandas<2.0.0"

pyLDAvis.enable_notebook()
lda_display = pyLDAvis.gensim.prepare(lda, corpus_TFIDF, id2word)
pyLDAvis.display(lda_display)