import json
from Video import Video

# import threading
# import asyncio

### MULTITHREADING ATTEMPT ###
# def create_video(url: str, l:list, loop) -> Video:
#     asyncio.set_event_loop(loop)
#     return Video(url)


# def fetch_videos(videos: list) -> list:
#     basepath = "https://www.youtube.com/watch?v="
#     urls = list(map(lambda x: (basepath + x), videos))
#     l = []
#     loop = asyncio.new_event_loop()
#     threads = [threading.Thread(target=create_video, args=(url,l,loop,)) for url in urls]
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#         thread.join()
#     return list(filter(lambda x: x.exists, l))

def fetch_videos(videos: list) -> list:
    basepath = "https://www.youtube.com/watch?v="
    all_videos = list(map(lambda x: Video(basepath + x), videos))
    return list(filter(lambda x: x.exists, all_videos))

def get_videos(input_file: str) -> list:
    with open(input_file, 'r') as f:
        data = json.load(f)
    videos_ids = data['videos_id']
    videos = fetch_videos(videos_ids)
    return videos

def get_output(input_file: str, output_file: str) -> None:
    dic = []
    list(map(lambda x: dic.append({'title': x.title, 'author': x.author, 'description': x.description, 'links': x.links}), get_videos(input_file)))
    with open(output_file, 'w') as f:
        json.dump(dic, f, ensure_ascii=False, default=lambda o: o.__dict__, indent=4)