from moviepy.editor import *
import audioread
import math
import mod.audioLength as audiolen

clips = []

for x in range(0,2) :
    # Path
    img_path = './database/img/img{0}.png'.format(x)
    korAudio_path = './database/kor{0}.mp3'.format(x)
    engAudio_path = './database/eng{0}.mp3'.format(x)

    # Audio Set
    eng_audio = AudioFileClip(engAudio_path)
    kor_audio = AudioFileClip(korAudio_path)

    # Audio Length
    with audioread.audio_open(engAudio_path) as eng:
        eng_len = math.ceil(eng.duration)
    with audioread.audio_open(korAudio_path) as kor:
        kor_len = math.ceil(kor.duration)
    total_len = eng_len + kor_len

    clip1 = ImageClip(img_path).set_duration(eng_len)
    clip1 = clip1.set_audio(eng_audio)
    clip2 = ImageClip(img_path).set_duration(kor_len)
    clip2 = clip1.set_audio(kor_audio)

    clips.append(clip1)
    clips.append(clip2)

video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile('translator.mp4', fps=24, remove_temp = True, codec="libx264", audio_codec="aac")