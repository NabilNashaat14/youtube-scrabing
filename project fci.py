from pytube import Playlist, YouTube
import pandas as pd
"""
---------------------------Youtube methods---------------------------------
Youtube.length  "video length"  -       Youtube.views         "video views"
Youtube.title   "video name"    -       Youtube.publish_date  "video date"
Youtube.description  "video description"  - Youtube.author  "channel name"
"""
"""
---------------------------Playlist methods---------------------------------
Playlist.length  "num of videos"             - Playlist.title  "playlist name"
Playlist.description  "playlist description" - Playlist.views  "playlist views"
Playlist.owner  "channel name"
"""


# function to convert the length from seconds to minutes
def calc(num):
    minute = int(num / 60)
    sec = num - (minute * 60)
    if sec < 9:
        sec = "0" + str(sec)
    if minute < 60:
        return str(minute)+":"+str(sec)
    elif minute >= 60:
        hour = int(minute/60)
        minute1 = minute - (hour * 60)
        if minute1 < 9:
            minute1 = "0"+str(minute1)
        return str(hour) + ":" + str(minute1) + ":" + str(sec)


url = "https://www.youtube.com/playlist?list=PL7JpMMpENaD3KL_lvmw4eS5U5AD746yKB"
play_list = Playlist(url)   # list [video1 url ,video2 url,video3 url.... ]

print("playlist name : "+play_list.title)
print("channel name : "+play_list.owner)
print("playlist number of videos : "+str(play_list.length))
print("playlist description : " + play_list.description)
print("playlist views : " + str(play_list.views)+" views")


video_names = []  # empty list to put the name of each video in "later"
for video in play_list:
    video_names.append(YouTube(video).title)

video_duration = []  # empty list to put the duration of each video in "later"
for video in play_list:
    video_duration.append(calc(YouTube(video).length))

dict = {"video name": [], "video duration": [], "video link": []}
dataframe = pd.DataFrame(dict)
dataframe["video name"] = video_names  # make a video names column
dataframe["video duration"] = video_duration  # make a video duration column
dataframe["video link"] = play_list  # Create a video links column

dataframe.to_excel("playlist scraping.xlsx")  # i must install openpyxl module
print("mission complete")





