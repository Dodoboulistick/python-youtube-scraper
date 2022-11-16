from utils import get_output, get_videos, fetch_videos
from Video import Video

videos = ["iUdssFpteeQ","4whD6uAryMs", "oimefjzeiufenriumgbremugibriu"] # The last one is invalid, thus should not pass the filter
basepath = "https://www.youtube.com/watch?v="
video1 = Video(basepath + videos[0])
video2 = Video(basepath + videos[1])
video3 = Video(basepath + videos[2])

def test_fetch_videos():
    manual_videos = [video1, video2]
    for i in range(len(manual_videos)):
        assert manual_videos[i].title == fetch_videos(videos[0:2])[i].title
        assert manual_videos[i].author == fetch_videos(videos[0:2])[i].author
        assert manual_videos[i].description == fetch_videos(videos[0:2])[i].description
        assert manual_videos[i].links == fetch_videos(videos[0:2])[i].links

def test_fetch_videos_with_one_invalid():
    manual_videos = [video1, video2, video3]
    assert len(fetch_videos(videos)) != len(manual_videos)
    

def test_get_videos():
    assert len(get_videos('input.json')) >= 0

def test_get_output():
    assert get_output('input.json', 'output.json') == None
