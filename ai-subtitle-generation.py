from subtitle_merger import add_soft_subtitles
from video_to_transcript import video_transcribe
import os
video_path = input("Enter : ")

srt_path = video_transcribe(video_path)

final_path = os.path.splitext(os.path.basename(video_path))[0]
add_soft_subtitles(video_path,srt_path,f"subtitle-{final_path}.mp4")

