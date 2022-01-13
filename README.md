# Ok Mugle! :musical_note:
## 장르부터 멜로디까지, Content-based Music Recommendation

- 'Ok Mugle!'은 [제13회 투빅스 컨퍼런스](http://www.datamarket.kr/xe/board_lhOx96/77271)(2022.01.15)에서 진행한 음악 추천 프로젝트입니다.

![발표 ppt(1차)_1](https://user-images.githubusercontent.com/87759826/149263884-f381c26d-18b0-43ba-9bda-a338cec3e53b.jpg)

## Description 📖

- 본 프로젝트에서는 Kakao Arena에서 제공하는 [Melon Playlist Continuation 데이터](https://arena.kakao.com/c/7)를 활용하여, **사용자가 검색한 노래와 유사한 노래 추천**을 구현하였습니다.

![발표 ppt(1차)_8](https://user-images.githubusercontent.com/87759826/149267879-04742886-9df8-4e6f-885f-a23dab38ec14.jpg)

1. **[Model]** '유사성'의 기준을 멜로디, 분위기, 상황, 장르 등으로 정의
   - 해당 요소 반영하여 Music2Vec, Time Convolutional AutoEncoder, ConsineEmbeddingLoss Multimodal 등의 모델 Building
2. **[Retrieval]** Embedding의 Cosine Similarity를 구하여 Retrieval 구성
3. **[Ranking]** 다양한 Ranking Method 사용 → 추천 결과 Ensemble
4. **[Serving]** 최종적으로 Score Total Top 10 Ranking Method의 추천 결과 활용하여 Web 구현 & 모델 Serving

## Usage ✔️

- Windows Shell에 아래 명령을 입력하여 실행합니다.
```
set FLASK_APP=server
set FLASK_ENV=development
flask run
```

## Result (Web) 💻

- [웹(ToBigs 13th Conference Music Recommendation) 바로가기](http://kimkwonho.pythonanywhere.com/)
- 웹 메인화면
 
![웹 메인](https://user-images.githubusercontent.com/87759826/149278035-0165d162-b50e-4a49-86a2-8890597324c8.PNG)

- 검색창에 '비투비 - 비밀 (Insane) (Acoustic Ver.)'를 검색한 결과 화면

![웹 검색결과](https://user-images.githubusercontent.com/87759826/149282039-b572e682-198c-4e71-bcbe-4d99cfe1bea9.PNG)

## Presentation 🙋

- (데이터마켓 게시글 링크)
- (유튜브 영상 링크)

## Contributor 🧑‍🤝‍🧑

- 본 프로젝트에는 [빅데이터 분석 및 인공지능 대표 연합동아리 ToBig's](http://www.datamarket.kr/xe/) 멤버들이 참여하였습니다.

|기수|이름|
|:-----:|:-----:|
|15기|[이성범](https://github.com/SeongBeomLEE)|
|16기|[김권호](https://github.com/kkhv)|
|16기|[박한나](https://github.com/hanna56)|
|16기|[이승주](https://github.com/duduuman)|
|16기|[이예림](https://github.com/YerimLee00)|
|16기|[주지훈](https://github.com/jihunju8589)|
|7기|[이광록](https://github.com/krlee407)(멘토)|

## File Directory 📂

```shell
Ok Mugle!
├── 1. preprocessig
│   ├── make_song_meta_and_playlist.ipynb       # 노래, 플레이리스트 데이터 전처리
│   ├── make_mel_data.ipynb                     # 멜 데이터 전처리
│   └── make_mel_batch_data.ipynb               # 멜 데이터 배치 단위로 전처리
│
├── 2. model
│   ├── genre_embedding_model.ipynb             # Music2Vec
│   ├── mel_embedding_model.ipynb               # Time Convolutional Autoencoder
│   └── genre_and_mel_embedding_model.ipynb     # CosineEmbeddingLoss Multimodal
│
├── 3. embedding-visualization
│   └── embedding_visualization_tsne.ipynb      # t-SNE를 활용한 각 임베딩별 시각화
│
├── 4. ranking
│   ├── make_ranking_data_preprocessig.ipynb    # 각 임베딩별 코사인 유사도 Top50 데이터 셋 제작 
│   ├── make_ranking_data_multiprocessig.py     # make_ranking_data_preprocessig의 multiprocessig을 위한 함수
│   ├── make_ranking_data.ipynb                 # 순위별 가중치 ranking, 각 임베딩 별 상위 Top3 ranking
│   └── cos_sim_music_serving.ipynb             # 각 임베딩, ranking 별 결과
│
└── 5. web
     ├── crawling                                # 결과창 구현을 위한 데이터 수집
     │   └── melon_crawling.py 
     │ 
     ├── data                                    # 웹 제작에 활용된 데이터
     │    ├── ranking_song_id2playlist.json
     │    ├── song_id2artist_name_basket.json
     │    ├── song_id2song_name.json
     │    └── song_name_artist_name2song_id.json
     │ 
     ├── static                                  # 웹 제작에 활용된 css, font, image, js
     │    ├── css
     │    ├── fonts
     │    ├── images
     │    └── js
     │ 
     ├── templates                               # 프론트 구현
     │    ├── about.html
     │    ├── index.html
     │    ├── people.html
     │    └── result.html
     │ 
     └── server.py                               # 백엔드 구현
     │
     └── requirements.txt                        # 필요 패키지 목록
      
```
