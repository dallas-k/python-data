from moviepy.editor import *
import mod.audioLength as audiolen

clips = []

# 경로
img_path = './database/img/img{0}.png'.format(data)
korAudio_path = './database/kor{0}.mp3'.format(data)
engAudio_path = './database/eng{0}.mp3'.format(data)

# concat, save
duration = 4
picture = ImageClip(img_path, duration=duration)
print(picture)
eng_audio = AudioFileClip(engAudio_path)
kor_audio = AudioFileClip(korAudio_path)
main_audio = CompositeAudioClip([eng_audio, kor_audio])
picture.set_audio(main_audio)
picture.write_videofile('trial{0}.mp4'.format(data), fps=24)


# clip1 = ImageClip('1.png').set_duration(3)

# count = 3
# temp = ImageClip('./database/img/img{0}.png'.format(count))
# clips.append(temp)
# print(clips)


# for i in range(20) :
#     temp = ImageClip('./database/img/img{0}.png'.format(i))
#     if(temp) :
#         clips.append(temp)
