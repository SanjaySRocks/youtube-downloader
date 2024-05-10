# youtube-downloader
A tool to download youtube playlist in highest quality


#### Installation

1. Install Module

```
pip install git+https://github.com/ytdl-org/youtube-dl.git
``` 

2. Install FFMPEG for Windows/Linux

3. Run `02_run.py` for windowsn and `03_run.py` for linux



#### Docker

1. Download the python script 03_run.py

2. Run Docker command
```
docker run --rm -it -v /root/youtube-dl/:/app sanjaysinghg2u/youtubedl python 03_run.py
```