from youtubesearchpython import VideosSearch
from youtubesearchpython import ChannelsSearch

def youtubeVideo(text, n=1):
    videosSearch = VideosSearch(text, limit = n)
    link = videosSearch.result().get('result')[0].get('link')
    return link

def youtubeChannel(text):
    channelSearch = ChannelsSearch(text, limit = n)
    link = channelSearch.result().get('result')[0].get('link')
    return link