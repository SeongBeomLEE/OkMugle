# Ok Mugle! 
### 장르부터 멜로디까지, Content-based Music Recommendation
투빅스 제 13회 컨퍼런스에서 진행한 음악 추천 프로젝트

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
│   ├── make_ranking_data.ipynb                 # 순위별 가중치 rangking, 각 임베딩 별 상위 Top3 rangking
│   └── cos_sim_music_serving.ipynb             # 각 임베딩, rangking 별 결과
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

```