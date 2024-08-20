from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Triangle

pluck = Triangle(200).to_audio_segment(200) \
                        .apply_gain(-7)

# Pan to the left
play(pluck.pan(-0.8))

play(AudioSegment.silent())

# Pan to the right
play(pluck.pan(1.0))

