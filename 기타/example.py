import os
from moviepy.editor import *
from moviepy.video.VideoClip import *


video = VideoFileClip("ball.mp4").subclip(10,20)

txt_clip = TextClip("my holiday 2013", fontsize=30, color='white')

#Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
            .set_position('center')
            .set_duration(10) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...