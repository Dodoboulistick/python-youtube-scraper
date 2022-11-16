from Video import Video

video = Video("https://www.youtube.com/watch?v=4whD6uAryMs") #Valid video
mock_video = Video("https://www.youtube.com/watch?v=4whD6uAryMs") #Invalid video -> Wrong ID

def test_real_video_info() -> None:
    assert video.title == "Daft Punk - Digital Love (Official Audio)"
    assert video.author == "Daft Punk"
    assert video.description == "“Digital Love” is taken from “Discovery” available on all platforms: https://daftpunk.lnk.to/Discovery\nSubscribe to the official Daft Punk YouTube channel: https://daftpunk.lnk.to/subscribeonY\n\nWatch more videos of Daft Punk: https://daftpunk.lnk.to/listenY\nListen to Daft Punk’s Essentials here: https://daftpunk.lnk.to/essentials\n\nWritten by Thomas Bangalter, Guy-Manuel de Homem-Christo, Carlos Sosa and George Duke\n\nFollow Daft Punk:\nOfficial website: https://www.daftpunk.com/\nInstagram: https://daftpunk.lnk.to/instagram\nTiktok: https://daftpunk.lnk.to/tiktok\nTwitch: https://daftpunk.lnk.to/twitch\nTwitter: https://daftpunk.lnk.to/twitter\nYouTube: https://daftpunk.lnk.to/youtube\nFacebook: https://daftpunk.lnk.to/facebook\nSpotify: https://daftpunk.lnk.to/spotify\nApple Music: https://daftpunk.lnk.to/applemusic\nAmazon Music: https://daftpunk.lnk.to/amazonmusic\nDiscord: https://daftpunk.lnk.to/discord \n\n↓ LYRICS ↓\n\nLast night I had a dream about you\nIn this dream, I'm dancing right beside you\nAnd it looked like everyone was having fun\nThe kind of feeling I've waited so long\n\nDon't stop, come a little closer\nAs we jam, the rhythm gets stronger\nThere's nothing wrong with just a little little fun\nWe were dancing all night long\n\nThe time is right to put my arms around you\nYou're feeling right, you wrap your arms around too\nBut suddenly I feel the shining sun\nBefore I knew it, this dream was all gone\n\nOoh, I don't know what to do\nAbout this dream and you\nI wish this dream comes true\n\nOoh, I don't know what to do\nAbout this dream and you\nWe'll make this dream come true\n\nWhy don't you play the game?\nWhy don't you play the game?\n\n℗ 2001 Daft Life\n\n#DaftPunk #Discovery #DigitalLove"
    assert video.exists == True

def test_fake_video_info() -> None: 
    assert mock_video.title == ""
    assert mock_video.author == ""
    assert mock_video.description == ""
    assert mock_video.exists == False

def test_real_video_links() -> None:
    assert video.links == [
        "https://daftpunk.lnk.to/Discovery",
        "https://daftpunk.lnk.to/subscribeonY",
        "https://daftpunk.lnk.to/listenY",
        "https://daftpunk.lnk.to/essentials",
        "https://www.daftpunk.com/",
        "https://daftpunk.lnk.to/instagram",
        "https://daftpunk.lnk.to/tiktok",
        "https://daftpunk.lnk.to/twitch",
        "https://daftpunk.lnk.to/twitter",
        "https://daftpunk.lnk.to/youtube",
        "https://daftpunk.lnk.to/facebook",
        "https://daftpunk.lnk.to/spotify",
        "https://daftpunk.lnk.to/applemusic",
        "https://daftpunk.lnk.to/amazonmusic",
        "https://daftpunk.lnk.to/discord"
        ]

def test_fake_video_links() -> None:
    assert mock_video.links == []
