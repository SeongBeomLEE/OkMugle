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
│   ├── genre_embedding_model.ipynb             # Word2Vec을 활용한 Genre Embedding
│   ├── mel_embedding_model.ipynb               # Causal Dilated Convolution Autoencoder을 활용한 Mel Embedding
│   └── genre_and_mel_embedding_model.ipynb     # CosineEmbeddingLoss Multimodal을 활용한 Genre, Mel Embedding
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
    ├── ....                      
    ├── ....                       
    ├── ....      
    └── ....

```