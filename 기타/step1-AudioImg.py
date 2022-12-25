#작업현황
#1. (O)  json file read
#2. (O)  개별 img 생성
#3. (O)  text clip add
#4. (0)  tts create

import json
from moviepy.editor import *
from gtts import gTTS

with open('text.json', 'r', encoding='utf-8') as f :
    json_data = json.load(f)
# print(json.dumps(json_data, ensure_ascii=False))

# :root
rgb_White = [255,255,255]
text_Black = "black"
root_fontLarge = 18
panel = "source/panel.png"

# panel image version
# for data in json_data :
#     each_data = json_data[data]
#     length = len(each_data['eng'])
#     img_clip = ImageClip(panel)
#     txt_clip = TextClip(each_data['eng'], fontsize=root_fontLarge, color=text_Black)
#     txt_clip = txt_clip.set_position((100,100))
#     final = CompositeVideoClip([img_clip, txt_clip])
#     final.save_frame('img/eng/img{0}.png'.format(data))

# color panel version
for data in json_data :
    #clip setting
    each_data = json_data[data]
    color_clip = ColorClip(size = (1920, 1080), color=rgb_White)
    txt_clip_eng = TextClip(each_data['eng'], font="NanumGothic", fontsize=root_fontLarge, color=text_Black)
    txt_clip_kor = TextClip(each_data['kor'], font="NanumGothic", fontsize=root_fontLarge, color=text_Black)
    txt_clip_eng = txt_clip_eng.set_position(('center',500))
    txt_clip_kor = txt_clip_kor.set_position(('center',600))

    # Each Img create
    final = CompositeVideoClip([color_clip, txt_clip_eng, txt_clip_kor])
    final.save_frame('./database/img/img{0}.png'.format(data))

    # Each Audio create
    eng = gTTS(text=each_data['eng'], lang='en', tld='com.au')
    eng.save('./database/eng{0}.mp3'.format(data))
    kor = gTTS(text=each_data['kor'], lang='ko')
    kor.save('./database/kor{0}.mp3'.format(data))