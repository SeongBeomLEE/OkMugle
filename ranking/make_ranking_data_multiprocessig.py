import numpy as np

def get_json_data(song_id, word2vec_embedding, mel_embedding, cos_embedding, song_id2song_embedding_idx, song_embedding_idx2song_id, song_id2playlist):
    
    song_embedding_idx = song_id2song_embedding_idx[song_id]

    word2vec_dot_ret = np.sum(word2vec_embedding[song_embedding_idx].reshape(1, -1) * word2vec_embedding, axis=1)
    mel_dot_ret = np.sum(mel_embedding[song_embedding_idx].reshape(1, -1) * mel_embedding, axis=1)
    cos_dot_ret = np.sum(cos_embedding[song_embedding_idx].reshape(1, -1) * cos_embedding, axis=1)

    word2vec_norm_ret = np.linalg.norm(word2vec_embedding[song_embedding_idx]) * np.linalg.norm(word2vec_embedding, axis=1)
    mel_norm_ret = np.linalg.norm(mel_embedding[song_embedding_idx]) * np.linalg.norm(mel_embedding, axis=1)
    cos_norm_ret = np.linalg.norm(cos_embedding[song_embedding_idx]) * np.linalg.norm(cos_embedding, axis=1)

    word2vec_ret = word2vec_dot_ret / word2vec_norm_ret
    mel_ret = mel_dot_ret / mel_norm_ret
    cos_ret = cos_dot_ret / cos_norm_ret

    sorted_idx_word2vec_ret = np.argsort(word2vec_ret)[::-1]
    sorted_idx_mel_ret = np.argsort(mel_ret)[::-1]
    sorted_idx_cos_ret = np.argsort(cos_ret)[::-1]

    word2vec_ret_song_id_li = [song_embedding_idx2song_id[idx] for idx in sorted_idx_word2vec_ret[:50]]
    mel_ret_song_id_li = [song_embedding_idx2song_id[idx] for idx in sorted_idx_mel_ret[:50]]
    cos_ret_song_id_li = [song_embedding_idx2song_id[idx] for idx in sorted_idx_cos_ret[:50]]

    song_id2playlist[str(song_id) + 'w'] = word2vec_ret_song_id_li
    song_id2playlist[str(song_id) + 'm'] = mel_ret_song_id_li
    song_id2playlist[str(song_id) + 'c'] = cos_ret_song_id_li