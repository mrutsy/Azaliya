import os
from pydub import AudioSegment
from pydub.playback import play


if __name__ == '__main__':
    # song = AudioSegment.from_mp3("data/start.mp3")
    # # song = AudioSegment.from_wav("audio_file.wav")
    # # you can also read from other formats such as MP4
    # # song = AudioSegment.from_file("audio_file.mp4", "mp4")
    # play(song)

    song = AudioSegment.from_ogg(os.path.join(os.getcwd(), "/opt/Azaliya/data/start.ogg"))
    play(song)
    song = AudioSegment.from_ogg(os.path.join(os.getcwd(), "/opt/Azaliya/data/about_me.ogg"))
    play(song)

    def play_azaliya(url):
        print(url)
        music = AudioSegment.from_mp3(url)
        play(music)

    dir_music = os.scandir("/opt/Azaliya/data/music")

    while True:
        for _ in dir_music:
            play_azaliya(os.path.join(os.getcwd(), _))
        # print(os.path.join("data", "music", _))
        # print(_)
    # print(dir_music)

    # while True:
    #     pass
    #