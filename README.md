# mp4-to-mp3
# Extract audio from vedio
The project uses Python to separate and save audio tracks from video files.<br>
It converts video soundtracks into standalone audio files for various uses.<br>
import moviepy.editor: This line imports the moviepy.editor module, which provides functionality for editing and manipulating video files.<br>

import tkinter.filedialog: This line imports the tkinter.filedialog module, which allows for opening file dialogs to select files from the file system.<br>

print("press Y to choose the video file to enter:"): This line prints a message prompting the user to press 'Y' to choose a video file.<br>

if input().casefold()=='y':: This line takes user input and checks if it is 'y' (case insensitive). If the user inputs 'y', the program proceeds to the next steps; otherwise, it prints a message indicating that a file needs to be chosen.<br>

video_path=tkinter.filedialog.askopenfilename(): This line opens a file dialog window, allowing the user to select a video file. The selected file's path is stored in the variable video_path.<br>

video=moviepy.editor.VideoFileClip(video_path): This line reads the video file located at video_path and creates a VideoFileClip object named video. This object represents the video file and allows for further operations like extracting audio.<br>

audio=video.audio: This line extracts the audio component from the video object and stores it in the variable audio.<br>

audio.write_audiofile('Audio1.mp3'): This line writes the extracted audio to a new audio file named 'Audio1.mp3' in the current directory.<br>

else:: This line starts an else block for the if statement started in line 4.<br>

print("You need to choose a file to move ahead"): This line prints a message indicating that the user needs to choose a file to proceed.<br>



