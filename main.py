import os
from pydub import AudioSegment
from pydub.playback import play


if __name__ == '__main__':
    song = AudioSegment.from_mp3("data/start.mp3")
    # song = AudioSegment.from_wav("audio_file.wav")
    # you can also read from other formats such as MP4
    # song = AudioSegment.from_file("audio_file.mp4", "mp4")
    play(song)

