# project_2_Game-content-reputation-analysis
## project2 주제
- 콘텐츠의 반응을 즉각적이게 알 수 있는 댓글을 수집
- 유튜브의 댓글을 크롤링 하여 분류, 게임 콘텐즈의 평판을 분석한다.
- 분석된 자료를 기반으로 기획 방향 도출

## 주제선정 이유
- [확률형 아이템 정보공개] 법적 의무화에 따른 시장 환경 변화
- 유튜브 댓글의 특징 : 장기간 기록, 불특정 다수노출
- 유튜브의 데이터 적극 활용방안 고안

## project 사용언어 
- python(VScode, google colab)

## 수집 대상 [358,713개]
- 기간 : 2013.01. ~ 2023.11. (11년)
- 대상 : FC 온라인, 바람의나라, 메이플스토리, 어둠의 전설, 워헤이븐, 베일드 엑스퍼트, 검은사막, 로스트아크,  리니지, 배틀그라운드, 제2의 나라, 신의탑, 몬스터 길들이기 (13종 게임)
- 분야 : 음악, 시스템, 게임성, BM, 운영, 그래픽 (6개)
- 세부 분야 : 36개 키워드
1. 음악 : 노래, BGM, 명곡, 브금, 음악, 사운드
2. 시스템 : 레이드, 렙업, 공성전, PVP, 스토리, 몬스터
3. BM :과금, 현질, 현금, 추천, 확률, 환불
4. 운영 : 업데이트, 해킹, 패치, 리부트, 광고, 이벤트
5. 게임성 : 무빙, 데미지, 타격감, 직업, 사냥, 밸런스
6. 그래픽 : 도트, 캐릭터, 배경, 디자인, 커스텀, 커스터 마이징

## Framework(프레임워크)
- 데이터 수집 > 전처리 > 자연어 처리(NLP) > LDA 토큰화 > 시각화

## Sentiment Analysis
- 전문가 : (금융뉴스 분석 모델) [https://github.com/ukairia777/finance_sentiment_corpus]
- GPT-4 : 5000개 무작위 댓글 샘플링 감정 학습 시킨 뒤 댓글 분석
- CHOI-Me : 5000개 무작위 댓글 샘플링 감정 학습 시킨 뒤 댓글 분석

## 시각화
- pyLDAvis
- Goole Looker Studio
- PPT

## 참고자료
- 2023 게임이용자 실태조사
- 2023_게임트렌드_10개
- 성별·연령대별 유튜브 및 넷플릭스 콘텐츠 이용행태 분석
