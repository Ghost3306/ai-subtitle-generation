import whisper
from whisper.utils import get_writer
import os
model = whisper.load_model("small")

def video_transcribe(video_path):
    result  = model.transcribe(video_path)
    output_directory = "."
    srt_writer = get_writer("srt", output_directory)
    srt_writer(result, video_path)
    srt_path = os.path.splitext(os.path.basename(video_path))[0] + ".srt"
    return os.path.abspath(srt_path)