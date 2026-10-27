import ffmpeg

def add_soft_subtitles(video_path, srt_path, output_path):
   
    input_video = ffmpeg.input(video_path)
    input_srt = ffmpeg.input(srt_path)
    
    
    ffmpeg.output(
        input_video['v'],            
        input_video['a'],            
        input_srt['s'],              
        output_path,
        vcodec='copy',               
        acodec='copy',               
        scodec='mov_text'            
    ).overwrite_output().run()

