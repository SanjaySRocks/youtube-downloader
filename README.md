# youtube-downloader
A tool to download youtube playlist in highest quality


#### Installation

1. Install Python Module

```
pip install git+https://github.com/ytdl-org/youtube-dl.git
``` 

<br>

2. Install ffmpeg package (https://github.com/BtbN/FFmpeg-Builds/releases)

- Win - https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip

- Linux - https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz

<br>

3. Run `02_run.py` for windows and `03_run.py` for linux


<br><br>

#### Docker

1. Download the python script 03_run.py

2. Run Docker command
```
docker run --rm -it -v /root/youtube-dl/:/app sanjaysinghg2u/youtubedl python 03_run.py
```

<br><br>

#### Command Line

1. Download playlist in bestaudio+bestvideo quality and if not best then whatever available download (using ffmpeg windows)

```
youtube-dl --ffmpeg-location "C:\Users\admin\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"  -i -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "https://www.youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop"
```

2. Download playlist in available quality

```
youtube-dl -i -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "https://www.youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop"
```
