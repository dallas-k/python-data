1. pip install moviepy // moviepy 설치
2. pip install ez_setup
3. imagemagick 설치
4. moviepy/config_defaults.py 에서 ff & imagemagick 경로 변경
5. bat파일로 일부 자동화


// 현재 계획 :
1. json 파일로 원문 작성
2. img 개별 이미지 시퀀시 생성 (-> 나중에 PDF 만들어서 Script 만들 수 있게) & 개별 audio 생성
3. img sequence별 화면 + 오디오 생성
4. sequence 합쳐서 하나의 영상으로 만들기


// img : text length -> set duration -> color clip -> text clip -> img sequence
// 주요 기능
- overlay text to img/color panel
(https://amhajja.medium.com/overlaying-text-on-images-using-moviepy-a396b028e14f)
- creating img sequence clip
(https://www.geeksforgeeks.org/moviepy-creating-image-sequence-clip/?ref=rp) -> fps 별도 설정이 불가능할지도..?
- creating audio clip
(https://www.geeksforgeeks.org/moviepy-creating-audio-clip/?ref=rp)
- inserting text in video
(https://www.geeksforgeeks.org/moviepy-inserting-text-in-the-video/)
- set audio to video
(https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/)
- video concatenate
(https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/)
- composite clips
(https://www.geeksforgeeks.org/moviepy-composite-video-setting-position-of-clip/)
- creating color clip
(https://www.geeksforgeeks.org/moviepy-creating-color-clip/?ref=rp)