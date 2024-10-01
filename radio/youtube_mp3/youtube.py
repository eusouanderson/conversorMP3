import yt_dlp
import os

def download_youtube_audio(video_url):
    os.makedirs('static/mp3', exist_ok=True)
    path = 'static/mp3'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{path}/%(title)s.%(ext)s',  
        'postprocessor_args': [
            '-ar', '44100',  
            '-ac', '2',      
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

