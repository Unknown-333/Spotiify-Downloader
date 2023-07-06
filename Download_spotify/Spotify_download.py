

import requests
import subprocess

playlist_id = ""  # Put your playlist ID here
api_key = ""  # Put your API key here [you can get from https://apilayer.com]
dir = "~/Documents"  # Specify the directory where you want the downloaded files to be saved

url = f"https://api.apilayer.com/spotify/playlist_tracks?id={playlist_id}"
headers = {"apikey": api_key}

def youtube_download(song_name):
    command = [
        "yt-dlp",
        f'ytsearch1:{song_name}',
        "--no-playlist",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "-o",
        f"{dir}/%(title)s.%(ext)s"
    ]
    print(f"Downloading {song_name}.....")
    result = subprocess.run(command)
    if result.returncode == 0:
        print(f"Successfully downloaded {song_name}")
    else:
        print(f"Could not download {song_name} from YouTube")

def request_spotify_api():
    response = requests.get(url, headers=headers)
    data = response.json()
    songs_meta = data["tracks"]["items"]
    for song_meta in songs_meta:
        song_name = song_meta["track"]["name"]
        artists = song_meta["track"]["album"]["artists"]
        for artist in artists:
            song_name += f" {artist['name']}"
        youtube_download(song_name)

request_spotify_api()
