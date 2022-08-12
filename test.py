from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=S-kg8eVPXRQ')

def options():
    resolutions = ['720p', '1080p', '1440p']
    choices = {}

    for each_resolution in resolutions:
        choice = yt.streams.filter(res=each_resolution)
        choices[each_resolution] = choice

    try:
        for i in choices.values():
            print(i[0])
    except IndexError:
        message = f"Havn't found any video in such resolution:{each_resolution}"
        return message


options()
#stream = yt.streams.get_by_itag(137)

