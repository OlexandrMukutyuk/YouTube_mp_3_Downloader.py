from pytube import YouTube
from moviepy.editor import *
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    return yt.default_filename.split('.')[0]

def convert_mp4_to_mp3(path):
    mp4_file = fr'./videos/{path}.mp4'
    mp3_file = fr'./music/{path}.mp3'

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()
    os.remove(f'./videos/{path}.mp4')

if __name__ == '__main__':
    path = 'https://www.youtube.com/watch?v=rWT1Q9c3eEk'
    convert_mp4_to_mp3(downloadYouTube(path, './videos'))
