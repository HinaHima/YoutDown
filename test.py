from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=869p-_qZkRc')

def options():
    for option in yt.streams:
        print(option)

#options()

stream = yt.streams.get_by_itag(137)
stream.download(output_path='A:\Python_projects\ViDown\media')
