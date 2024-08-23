from pydub import AudioSegment
from pydub.generators import Sine, Triangle
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


def delay(sound, repeat=1, fade=1, ping_pong=False):
    if ping_pong == True:
        pan_value = 1
        result = sound

        for i in range(repeat):
            result += sound.pan(pan_value)
            pan_value *= -1

        return result.fade_out(fade)

    return (sound+sound*repeat).fade_out(fade)


bass = Sine(144).to_audio_segment(200) + \
                 delay(
                    Sine(144).to_audio_segment(200), 
                    repeat=4, fade=400, ping_pong=True
                    )

bass = bass.apply_gain(-9) + AudioSegment.silent(400)


# Attack and Release cannot be equal to zero due to technical limitations
def adr_envelope(generator, attack=1, decay=1000, release=1):

    total_duration = sum([attack, decay, release])
    
    result = generator.to_audio_segment(duration=total_duration) \
                                            .fade_in(attack) \
                                            .fade_out(release)
    return result


octave_four = [round(440 * 2**((key-49)/12), 2) for key in range(40, 52)]

lead_melody = adr_envelope(Triangle(octave_four[2]), attack=500, release=4000) + \
              adr_envelope(Triangle(octave_four[6]), attack=1000, release=500) + \
              adr_envelope(Triangle(octave_four[1]), attack=500, release=2000) + \
              AudioSegment.silent(2000) + \
              adr_envelope(Triangle(octave_four[2]), attack=500, release=4000) + \
              adr_envelope(Triangle(octave_four[6]), attack=1000, release=500) + \
              adr_envelope(Triangle(octave_four[8]), attack=500, release=4000) + \
              AudioSegment.silent(2000)

lead_melody = lead_melody.low_pass_filter(14000)


def play_chords(attack=1, decay=200, release=1, **chords):

    track = AudioSegment.silent(0)
    total_duration = sum([attack, decay, release])

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

        track += chord

    return track

backing_melody = play_chords(
    attack=1000, decay=500, release=1500, 
    Am=[440, 523.25, 659.25],
    Cm=[523.25, 659.25, 783.99],
    # Duplicate keys in kwargs are not allowed
    Cm_2=[523.25, 659.25, 783.99],
).low_pass_filter(14000)

bassline = bass*18

mixdown = bassline.apply_gain(-7) \
            .overlay(AudioSegment.silent(len(bass*2)) + drumloop.apply_gain(-6)*9) \
            .overlay(AudioSegment.silent(len(bass*2)) + lead_melody.apply_gain(-10)*2) \
            .overlay(              # Take roughly a half of the lead melody
                AudioSegment.silent(len(bass*2) + int(len(lead_melody)/2)) + backing_melody.apply_gain(-16)*5
            ) \
            + bass

play(mixdown)
