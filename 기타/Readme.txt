1. pip install moviepy // moviepy 설치
2. pip install ez_setup
3. imagemagick 설치
4. moviepy/config_defaults.py 에서 ff & imagemagick 경로 변경


// 현재 계획 : json 파일로 원문 작성 -> 이를 바탕으로 TTS, img 생성 -> 두 개 하나로 합치기 (즉, 싱크로율 및 duration 중요)
// img : text length -> set duration -> color clip -> text clip -> img sequence
// 주요 기능
1. json 파일 read
2. creating img sequence clip (https://www.geeksforgeeks.org/moviepy-creating-image-sequence-clip/?ref=rp) -> fps 별도 설정이 불가능할지도..?
3. creating audio clip (https://www.geeksforgeeks.org/moviepy-creating-audio-clip/?ref=rp)
4. inserting text in video (https://www.geeksforgeeks.org/moviepy-inserting-text-in-the-video/)
5. set audio to video (https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/)
6. video concatenate (https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/)
7. composite clips (https://www.geeksforgeeks.org/moviepy-composite-video-setting-position-of-clip/)
8. 