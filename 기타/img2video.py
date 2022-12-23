from moviepy.editor import *

clips = []
clip1 = ImageClip('1.png').set_duration(3)
clip2 = ImageClip('2.png').set_duration(3)
clip3 = ImageClip('3.png').set_duration(3)

clips.append(clip1)
clips.append(clip2)
clips.append(clip3)

video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile('video-output.mp4', fps=24, remove_temp = True, codec="libx264", audio_codec="aac")