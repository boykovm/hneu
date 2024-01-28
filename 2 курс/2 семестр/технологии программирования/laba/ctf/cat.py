from moviepy.editor import VideoFileClip
import matplotlib.pyplot as plt

# Load the MP4 file
video = VideoFileClip('talk.mp4')

# Extract frames from the video
frames = video.iter_frames()

# Display the frames
for frame in frames:
    plt.imshow(frame)
    plt.show()
