import yt_dlp

def download_youtube_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'radio/static/mp3/%(title)s.%(ext)s',
        'quiet': False,  # Exibe informações detalhadas
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"An error occurred: {e}")

# Exemplo de uso
download_youtube_audio('https://www.youtube.com/watch?v=O4irXQhgMqg')
