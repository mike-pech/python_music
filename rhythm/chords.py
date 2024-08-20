from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

def play_chords(name, attack=1, decay=200, release=1, **chords) -> None:

    total_duration = sum([attack, decay, release])

    print(f"\t\tNow playing: {name}")

    for written_chord in chords.keys():

        chord = AudioSegment.silent(duration=decay)
        print(f"\nChord: {written_chord}")

        for note in chords[written_chord]:

            tone = Sine(note) \
                .to_audio_segment(duration=total_duration)\
                                            .fade_in(attack) \
                                            .fade_out(release)

            chord = chord.overlay(tone.normalize(10))

            print(f"\tNote frequency: {note} Hz")

        play(chord)

# A declared keyword argument "decay" with user-specified chords
play_chords(
    "My beautiful rhythm!",
    decay=1000,
    C=[261.63, 329.63, 392],
    Cm7=[261.63, 311.12, 391.99, 466.16],
    Dmaj7=[146.83, 184.99, 220, 277.18]
)
