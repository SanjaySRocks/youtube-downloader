from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop')

print(f'Downloading: {p.title}')

for video in p.videos:
    stream = video.streams.get_highest_resolution()
    file_size = stream.filesize_approx
    file_size_mb = file_size / (1024 * 1024) if file_size is not None else 'Unknown'
    print(f'Downloading video: {video.title} ({stream.resolution}, {stream.mime_type}, {file_size_mb:.2f} MB)')
    stream.download()