from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play

kick1 = AudioSegment.from_wav("./drumloop/kick1.wav")
kick2 = AudioSegment.from_mp3("./drumloop/kick2.mp3")
kick3 = AudioSegment.from_wav("./drumloop/kick3.wav")

kick1 = split_on_silence(kick1, min_silence_len=10)[0]
kick2 = kick2.strip_silence(silence_thresh=-32)
kick3 = kick3[:600]


kick1 = kick1.apply_gain(2)

kick2 = kick2 \
            .apply_gain(2) \
            .reverse() \
            .speedup(playback_speed=2, chunk_size=50)


drumloop = kick3 + \
            AudioSegment.silent(100) + \
            kick2*3 + \
            AudioSegment.silent(200) + \
            kick1 + \
            AudioSegment.silent(100) + \
            kick2*3 + \
            AudioSegment.silent(500)


