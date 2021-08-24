import requests, json, re

url = "https://youtube-mp36.p.rapidapi.com/dl"

headers = {
    'x-rapidapi-host': "youtube-mp36.p.rapidapi.com",
    'x-rapidapi-key': "5beaa74967mshf3577ef449407c9p11be8bjsn8aa15de9dbbd"
    }

songs_failed_download = ""

with open('song-list.txt', "r") as song_file:
    song_list = song_file.readlines()

    for song_id in song_list:
        querystring = {"id":song_id}

        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            download_link = json.loads(response.text)['link']
            r = requests.get(download_link, allow_redirects=True)
            title = re.sub(r'([\,\.\?\-\[\]\(\)]+|Lyrics|Official|Video|audio|Music)', '', json.loads(response.text)['title'], flags=re.IGNORECASE).strip()
            open("Music/" + title + '.mp3', 'wb').write(r.content)
            print(song_id + " downloaded")

        except Exception as e:
            songs_failed_download += song_id + "\n"
            print("Could not download " + song_id)

with open('song-list.txt', "w") as song_file:
    song_file.write(songs_failed_download)
        