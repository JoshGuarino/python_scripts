#download a youtube video
import pytube
import os
link = input('Please enter the link for the youtube video you want to download:\n')
link_status = False
while link_status == False:
    try:
        yt = pytube.youtube(link)
        link_status = True
    except:
        link = input('Error video not found, please enter a correct link:\n')
