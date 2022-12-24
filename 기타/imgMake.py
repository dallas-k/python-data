#작업현황
#1. (O)  json file read
#2. (O)  개별 img 생성   

import json
from moviepy.editor import *

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
    each_data = json_data[data]
    length = len(each_data['eng'])
    color_clip = ColorClip(size = (1920, 1080), color=rgb_White)
    txt_clip = TextClip(each_data['eng'], fontsize=root_fontLarge, color=text_Black)
    txt_clip = txt_clip.set_position((100,100))
    final = CompositeVideoClip([color_clip, txt_clip])
    final.save_frame('img/eng/final{0}.png'.format(data))