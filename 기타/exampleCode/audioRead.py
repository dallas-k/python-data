# METHOD 2
import audioread
import math
  
# function to convert the information into 
# some readable format
def duration_detector(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
  
    return hours, mins, seconds
  
  
# alarm.wav is the name of the audio file
# f is the fileobject being created
with audioread.audio_open('./database/eng3.mp3') as f:
    
    # totalsec contains the length in float
    totalsec = f.duration
    hours, mins, seconds = duration_detector(math.ceil(totalsec))
    print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))