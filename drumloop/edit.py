from pydub import AudioSegment
from pydub.playback import play

# Create a new AudioSegment from a file
drum = AudioSegment.from_wav("./drumloop/drumloop.wav")

# Make it loop (I mean, it says drum loop on the tin...)
drum_loop = drum * 5

# Make it 3db louder!
louder = drum_loop + 3

# Add a smooth fade in the end that lasts for 250ms
result = louder.fade_out(250)

# Play it!
play(result)

# Nice! Let's save it!
result.export("./drumloop/drumloop.mp3", format="mp3")
