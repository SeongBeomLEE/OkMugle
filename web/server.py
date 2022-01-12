# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, redirect
from crawling.melon_cawling import get_melon_url
import json

with open('data/song_id2artist_name_basket.json', 'r', encoding = 'utf-8') as f:
    song_id2artist_name_basket = json.load(f)

with open('data/song_id2song_name.json', 'r', encoding = 'utf-8') as f:
    song_id2song_name = json.load(f)

with open('data/ranking_song_id2playlist.json', 'r', encoding = 'utf-8') as f:
    song_id2playlist = json.load(f)

with open('data/song_name_artist_name2song_id.json', 'r', encoding = 'utf-8') as f:
    song_name_artist_name2song_id = json.load(f)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        fail_msg1 = '❗ 존재하지 않는 노래 입니다 ❗' 
        fail_msg2 = '다시 검색해주세요'
        return render_template('index.html', fail_msg1 = fail_msg1, fail_msg2 = fail_msg2)

@app.route("/people", methods=['GET'])
def people():
    if request.method == 'GET':
        return render_template('people.html')

@app.route("/about", methods=['GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            song_name_artist_name = request.form['song_name_artist_name']
            now_song_id = song_name_artist_name2song_id[song_name_artist_name]
            playlist = song_id2playlist[str(now_song_id)]

            result = [[song_id2song_name[str(song_id)], song_id2artist_name_basket[str(song_id)]] for song_id in playlist]
            result = [[song_name, artist_name] + get_melon_url(song_name, artist_name) for song_name, artist_name in result]

            return render_template('result.html', output_song_list = result)
        except:
            return redirect(url_for('index'), code=307)


if __name__ == '__main__':
   app.run(debug = True)