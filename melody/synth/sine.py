from pydub.playback import play
from pydub.generators import Sine

# Create a generator of frequency 400Hz
generator = Sine(400)

# Use this generator to synthesize a sound for 2 seconds (2000ms)
tone = generator.to_audio_segment(duration=2000)

# Play it!
play(tone)
