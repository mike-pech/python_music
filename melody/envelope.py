from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

# Attack and Release cannot be equal to zero due to technical limitations
def adr_envelope(generator, attack=1, decay=1000, release=1):

    total_duration = sum([attack, decay, release])
    
    result = generator.to_audio_segment(duration=total_duration) \
                                            .fade_in(attack) \
                                            .fade_out(release)
    return result


# All arguments are positional and present
play(
    adr_envelope(
            Sine(100), 
            1500, 
            1500, 
            2000
    ) \
        .apply_gain(-8)
)
play(AudioSegment.silent(200))
# Positional argument "generator" and keyword argument "release"
play(
    adr_envelope(
        Sine(100),
        release=4000
    ) \
        .apply_gain(-8)
)

backing_melody = \
    adr_envelope(
            Sine(100), 
            1500, 
            1500, 
            2000
    ) + \
    AudioSegment.silent(200) + \
    adr_envelope(
        Sine(100),
        release=4000
    )

backing_melody.apply_gain(-7).export("./melody/backing_melody.mp3", format="mp3")
