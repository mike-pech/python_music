from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

# Create an empty AudioSegment
result = AudioSegment.silent(duration=0)

# ---------------------------------------------------------------

# Make a list of pre-calculated frequencies
octave_four = [
    261.63, 277.18, 293.66, 311.13,
    329.63, 349.23, 369.99, 392,
    415.3, 440, 466.16, 493.88
    ]

# ---------------------------------------------------------------

# Make a function that calculates the note frequency
def calculate_frequency(note: int):

    frequency = round(440 * 2**((note-49)/12), 2)

    return frequency


# Calculate the notes inside the list using list comprehension
octave_four = [calculate_frequency(key) for key in range(40, 52)]

# ---------------------------------------------------------------

# You can even put the formula inside the list comprehension
octave_four = [round(440 * 2**((key-49)/12), 2) for key in range(40, 52)]

# ---------------------------------------------------------------

# Loop over the notes 40 to 52 (octave 4)
for i in octave_four:

    # Make a generator with the given frequency and print it
    gen = Sine(i)
    print(f"Current frequency: {i} Hz")

    # Use it to generate an AudioSegment with duration 200 ms
    tone = gen.to_audio_segment(duration=500)

    # Fade in / out, gain -3, low-pass filter
    tone = tone \
        .fade_in(50) \
        .fade_out(200) \
        .apply_gain(-5) \
        .low_pass_filter(15000)

    # Append the tone to our result
    result += tone


# Play the result
play(result)

# Export the result
# result.export("sine.mp3", format="mp3")
