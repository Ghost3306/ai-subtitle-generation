import whisper
from whisper.utils import get_writer
model = whisper.load_model("small")
video_path = "iPhone.mp4"
result  = model.transcribe(video_path)
output_directory = "."
srt_writer = get_writer("srt", output_directory)
srt_writer(result, video_path)