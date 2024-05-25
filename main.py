import moviepy.editor
import tkinter.filedialog
print("press Y to choose the video file to enter:")
if input().casefold()=='y':
    video_path=tkinter.filedialog.askopenfilename()
    video=moviepy.editor.VideoFileClip(video_path)
    audio=video.audio
    audio.write_audiofile('Audio1.mp3')
else:
    print("You need to choose a file to move ahead") 