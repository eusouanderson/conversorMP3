from youtube_mp3.youtube import download_youtube_audio
from flask import Flask, render_template, send_from_directory, jsonify, request, redirect, url_for
import os  

app = Flask(__name__)

@app.route('/')
def index():
    music_files = [f for f in os.listdir('radio/static/mp3') if f.endswith('.mp3')]
    music_files.sort(reverse=True)
    if not music_files:
        return render_template('index.html', music_files=["Nenhuma música disponível"])
    return render_template('index.html', music_files=music_files)

@app.route('/play/<filename>')
def play(filename):
    return send_from_directory('static/mp3', filename)

@app.route('/music-files')
def music_files():
    files = [f for f in os.listdir('radio/static/mp3') if f.endswith('.mp3')]
    files.sort(reverse=True)
    return jsonify(files)

@app.route('/download', methods=['POST'])
def download():
    youtube_url = request.form.get('youtubeURL')
    if youtube_url:
        try:
            download_youtube_audio(youtube_url)
            return redirect(url_for('index'))  
        except Exception as e:
            return f"Erro ao baixar o áudio: {str(e)}", 500
    return "URL do YouTube não fornecida", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

