from pytube import Playlist
import os
import time

def download_with_progress(video):
    stream = video.streams.first()
    file_path = os.path.join("downloads", f"{video.title}.mp4")
    print(f'Downloading: {video.title}')
    stream.download(output_path="downloads", filename=f"{video.title}.mp4")
    while not os.path.exists(file_path):
        time.sleep(1)
    total_size = stream.filesize
    while os.path.getsize(file_path) < total_size:
        progress = (os.path.getsize(file_path) / total_size) * 100
        print(f'Downloading: {video.title} - {progress:.2f}% complete', end='\r')
        time.sleep(1)
    print(f'{video.title} downloaded successfully!')

p = Playlist('https://www.youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop')

print(f'Downloading playlist: {p.title}')

for video in p.videos:
    download_with_progress(video)

print('All videos downloaded successfully!')
