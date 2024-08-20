from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

def play_note(note):

    tone = AudioSegment.silent(0)

# -------- match statement example --------
    flag = False

    if note in "AaA#a#BbD#d#EeFfF#f#GgG#g#":
        flag = True

    match note:
        case "C" | "c":
            tone = Sine(261.63) \
                    .to_audio_segment(duration=1000) 
        case "C#" | "c#":
            tone = Sine(277.18) \
                    .to_audio_segment(duration=1000) 
        case "D" | "d":
            tone = Sine(293.66) \
                    .to_audio_segment(duration=1000) 
        case _ if flag:
            print("I can't play all 12 notes yet!")
            return
        # Default case
        case _:
            print("I don't know this note!")
            return

# -------- if statements example --------
    # if note == "C":
    #     tone = Sine(261.63) \
    #             .to_audio_segment(duration=1000) 
    # elif note == "C#":
    #     tone = Sine(277.18) \
    #             .to_audio_segment(duration=1000) 
    # elif note == "D":
    #     tone = Sine(293.66) \
    #             .to_audio_segment(duration=1000) 
    # else:
    #     print("I don't know this note")
    #     return

    play(
        tone \
            .apply_gain(-7) \
            .fade_in(50) \
            .fade_out(100)
    )

while True:
    play_note(input("Enter a note to play: "))
