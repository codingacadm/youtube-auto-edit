
# 영상을 가져온다.

# from pytube import YouTube
# YouTube('https://www.youtube.com/watch?v=o9_wmHcCFag')\
#     .streams\
#     .filter(progressive=True, file_extension='mp4')\
#     .order_by('resolution').first().download(outputpathfilename='downloaded_video.mp4')
    
    #  download(output_path: Optional[str] = None, filename: Optional[str] = None, filename_prefix: Optional[str] = None, skip_existing: bool = True, timeout: Optional[int] = None, max_retries: Optional[int] = 0) → str[source]

    # Write the media stream to disk.
    # Parameters:	

    #     output_path (str or None) – (optional) Output path for writing media file. If one is not specified, defaults to the current working directory.
    #     filename (str or None) – (optional) Output filename (stem only) for writing media file. If one is not specified, the default filename is used.
    #     filename_prefix (str or None) – (optional) A string that will be prepended to the filename. For example a number in a playlist or the name of a series. If one is not specified, nothing will be prepended This is separate from filename so you can use the default filename but still add a prefix.
    #     skip_existing (bool) – (optional) Skip existing files, defaults to True
    #     timeout (int) – (optional) Request timeout length in seconds. Uses system default.
    #     max_retries (int) – (optional) Number of retries to attempt after socket timeout. Defaults to 0.

#  >>> yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#  >>> yt.streams
#   ... .filter(progressive=True, file_extension='mp4')
#   ... .order_by('resolution')
#   ... .desc()
#   ... .first()
#   ... .download()

#https://www.youtube.com/watch?v=o9_wmHcCFag

# def fetch_yt_video_by_link(link: str, path: str = '.', fname: str ='downloaded_video', format='mp4'):
#     """링크를 통해 가장 좋은 해상도의 유튜브 영상을 다운로드"""
#     from pytube import YouTube
#     YouTube(link)\
#     .streams\
#     .filter(progressive=True, file_extension=format)\
#     .order_by('resolution').first()\
#     .download(output_path=path,filename=fname +'.'+ format)

# fetch_yt_video_by_link('https://www.youtube.com/watch?v=o9_wmHcCFag', fname='윤하_기다리다')



# video = fetch_yt_video_link(link)
# save_video(video, path='./downloaded_video', format='mp4')


# loaded_video = load_video(video)


# editor = VideoEditor(loaded_video)
# editor.by_span(start=40, end=50)
# editor.has_keyword(['파이썬', '개발'], min=2)


# from moviepy.editor import *

# # 윤하_기다리다.mp4
# video = VideoFileClip("윤하_기다리다.mp4").subclip(10,20)

# # Make the text. Many more options are available.
# txt_clip = ( TextClip("윤하짱",fontsize=70,color='red').set_duration(10) )
#                 # .with_position('center')
#                 # .with_duration(10) )

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("윤하짱_기다리다.webm",fps=25) # Many options...


# edited = editor.edited_video
# save_video(edited, path='./edited_video', format='mp4')


from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcripts(['o9_wmHcCFag'], languages=['ko'])
print(transcript)
print(transcript[0]['o9_wmHcCFag'])
# YouTubeTranscriptApi.get_transcript('o9_wmHcCFag')


editor = VideoEditor(loaded_video)
editor.by_span(start=40, end=50)
editor.has_keyword(['파이썬', '개발'], min=2)

