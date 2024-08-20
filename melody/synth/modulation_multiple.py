from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine, Sawtooth, Triangle

# Create two generators of different shapes
generator1 = Sawtooth(600)
generator2 = Sine(80)
generator3 = Triangle(100)

# Use each generator to synthesize a sound for 2 seconds (2000ms)
sawtooth = generator1.to_audio_segment(duration=4000)
sine = generator2.to_audio_segment(duration=4000)
triangle = generator3.to_audio_segment(duration=4000)

def modulate(*tones):
    
    result = tones[0]

    for tone in tones[1:]:
        result.overlay(tone)   

    return result

# Though you rarely need to modulate more than two generators
play(
    modulate(triangle, sawtooth, sine) \
        .apply_gain(-15) \
        .low_pass_filter(15000)
)

melody = \
    modulate(triangle, sawtooth) \
        .apply_gain(-15) \
        .low_pass_filter(15000) \
        .fade_out(250) \
    + AudioSegment.silent(500) \
    + modulate(sine, triangle) \
        .apply_gain(-15) \
        .low_pass_filter(15000) \
        .fade_out(250) \
    + AudioSegment.silent(500) \
    + modulate(sine, sawtooth) \
        .apply_gain(-15) \
        .low_pass_filter(15000) \
        .fade_out(250) 

play(melody)
