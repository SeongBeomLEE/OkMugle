import requests
from bs4 import BeautifulSoup
import re

def get_melon_url(song_name, artist_name):
    headers = {'User-Agent': 'Mozilla/5.0'}
    query = song_name + ' ' + artist_name
    url = f'https://www.melon.com/search/total/index.htm?q={query}&section=&mwkLogType=T'

    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        # 전체에서 검색
        melon_song_id = soup.select('#frm_songList > div > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3) > div > div > a.btn.btn_icon_detail')[0]['href']
    except:
        try:
            # 곡명으로 검색
            melon_song_id = soup.select('#frm_searchSong > div > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3) > div > div > a.btn.btn_icon_detail')[0]['href']
        except:
            query = song_name
            url = f'https://www.melon.com/search/total/index.htm?q={query}&section=&mwkLogType=T'

            req = requests.get(url, headers = headers)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            try:
                # 아티스트 명이 잘못 되었을 때
                melon_song_id = soup.select('#frm_searchSong > div > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3) > div > div > a.btn.btn_icon_detail')[0]['href']
            except:
                query = re.sub('\(.*\)', '', query).rstrip()
                url = f'https://www.melon.com/search/total/index.htm?q={query}&section=&mwkLogType=T'

                req = requests.get(url, headers = headers)
                html = req.text
                soup = BeautifulSoup(html, 'html.parser')
                try:
                    # 곡 명이 잘못 되었을 때
                    melon_song_id = soup.select('#frm_searchSong > div > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3) > div > div > a.btn.btn_icon_detail')[0]['href']
                except:
                    # 곡이 존재하지 않음
                    melon_song_id = []

    if melon_song_id:
        melon_song_id = re.findall('goSongDetail\(\'(.*?)\'\)', melon_song_id)
        melon_song_id = melon_song_id[0]
        melon_song_id_url = f'https://www.melon.com/song/detail.htm?songId={melon_song_id}'

        req = requests.get(melon_song_id_url, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        melon_song_img_url = soup.select('#downloadfrm > div > div > div.thumb > a > img')
        melon_song_img_url = melon_song_img_url[0]['src']

    else:
        melon_song_id_url = f'https://www.melon.com/search/total/index.htm?q={song_name}&section=&mwkLogType=T'
        melon_song_img_url = 'static/images/wait_img.jpg'

    return [melon_song_id_url, melon_song_img_url]
