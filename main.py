
from pytubefix import YouTube
from pytubefix.cli import on_progress
import ssl
import certifi

ssl._create_default_https_context = ssl._create_unverified_context
 
url = ["https://youtu.be/SmYAwwZOVG0?si=gtUaQnkWzRrVHaxP"]
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_audio_only()
ys.download(mp3=True)