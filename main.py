import os
import json
from pydub import AudioSegment
from pydub.playback import play

if __name__ == '__main__':

    with open("configs/settings.json") as file:
        settings = json.load(file)

    if settings['restart'] == 'true':
        settings['restart'] = 'false'
        with open('configs/settings.json', 'w') as f:
            json.dump(settings, f)
        print("restart")
        os.system("/bin/sh -c 'exit'")
    else:
        settings['restart'] = 'true'
        with open('configs/settings.json', 'w') as f:
            json.dump(settings, f)
        print("done")

        song = AudioSegment.from_ogg(os.path.join(os.getcwd(), "data/start.ogg"))
        play(song)
        song = AudioSegment.from_ogg(os.path.join(os.getcwd(), "data/about_me.ogg"))
        play(song)


        def play_azaliya(url):
            print(url)
            music = AudioSegment.from_mp3(url)
            play(music)


        dir_music = os.scandir("data/music")

        while True:
            for _ in dir_music:
                play_azaliya(os.path.join(os.getcwd(), _))
            print(os.path.join("data", "music", _))
            print(_)
    # print(dir_music)

    # while True:
    #     pass
    #
