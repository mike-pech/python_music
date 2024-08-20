from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

# Note the annotations that hint types for you and your fellow programmers!
def sequence(generator, notes: list) -> AudioSegment:

    # Assign the first note and the rest
    first_note, *other_notes, last_note1, last_note2 = notes

    # Create a new AudioSegment to base the sequence on
    result = generator(first_note).to_audio_segment(duration=200)

    for note in other_notes:
        
        # Append new notes to the base sequence
        result += generator(note).to_audio_segment(duration=200)

    # Repeat second-to-last note twice
    result += generator(last_note1).to_audio_segment(duration=200) * 2

    # Make the last note longer
    result += generator(last_note2).to_audio_segment(duration=500)

    return result

MELODY = [ 260, 290, 200, 180, 150 ]

play(
    sequence(Sine, MELODY) \
        .apply_gain(-5)
)
