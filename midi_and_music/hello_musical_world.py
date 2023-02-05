#
# hello_musical_world.py
#
# Explorations working with midi files
#
# Checked into Github as:
#        https://github.com/seemsartless/generative_art/tree/master/midi_and_music
#
#  https://github.com/kiecodes/generate-music

# https://www.youtube.com/watch?v=w732EXqmfZU

# Reading the keys pressed on the midi keyboard
# Requirements:
#    mygame (for images)
#    mido
#    rtmidi  +1
#
# https://www.youtube.com/watch?v=Q40qEg8Yq5c
#
#  https://www.youtube.com/watch?v=aOsET8KapQQ
#
# https://pythonlang.dev/repo/rainbow-dreamer-musicpy/
# https://pythonlang.dev/repo/mido-mido/
#
# https://github.com/Miserlou/chords2midi/blob/master/chords2midi/c2m.py
#
# MIDIUtil - https://midiutil.readthedocs.io/en/latest/

# https://github.com/yuma-m/pychord/blob/main/examples/pychord-midi.py

# https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies

import pandas as pd
from midiutil import MIDIFile
from oneSong import *

print("Starting...")
t1 = oneSong(key="C", tempo=120, tracks=4)

print(f"Pitch for C is {t1.midiPitch('C4')}")
# D F A C
# C Bb F C
print(f"Pitch for D is {t1.midiPitch('D4')}")
print(f"Pitch for F is {t1.midiPitch('F4')}")
print(f"Pitch for A is {t1.midiPitch('A4')}")
print(f"Pitch for B is {t1.midiPitch('B4')}")
print(f"Pitch for Bb is {t1.midiPitch('Bb4')}")

# How about sus chords?

# And random
#   addRandom(self, chord, octave, totalDuration, volume, track=1, div=2, max=2):
for aChord in ["sus2", "sus4", "I", "sus2", "sus4", "I"]:
    t1.addChord(aChord, duration=2, volume=80, octave=4, track=1)
    t1.addRandom(aChord, totalDuration=2, volume=80, octave=4, track=2, div=4, max=2) # Add 4 random notes/pairs
    t1.addRandom(aChord, totalDuration=2, volume=80, octave=4, track=3, div=4, max=1) # Add 4 random notes/pairs
for aChord in ["sus2", "sus4", "I", "sus2", "sus4", "I"]:
    t1.addChord(aChord, duration=2, volume=80, octave=4, track=1)
    t1.addRandom(aChord, totalDuration=2, volume=80, octave=4, track=2, div=4, max=2) # Add 4 random notes/pairs
    t1.addRandom(aChord, totalDuration=2, volume=80, octave=4, track=3, div=4, max=1) # Add 4 random notes/pairs



# Common I V vi IV
if 1 == 1:
    for i in [1,2,]:
        t1.addChord(chord="I", duration=2, volume=80, octave=4)
        t1.addChord(chord="V", duration=2, volume=80, octave=4)
        t1.addChord(chord="vi", duration=2, volume=80, octave=4)
        t1.addChord(chord="IV", duration=2, volume=80, octave=4)
    # A break
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    t1.addNotes(intervs=['C4'], duration=1, volume=40)
    t1.addNotes(intervs=['D4'], duration=1, volume=40)
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)

    t1.changeKey(newKey="G")
    for i in [1,2]:
        t1.addChord(chord="I", duration=2, volume=80, octave=4)
        t1.addChord(chord="V", duration=2, volume=80, octave=4)
        t1.addChord(chord="vi", duration=2, volume=80, octave=4)
        t1.addChord(chord="IV", duration=2, volume=80, octave=4)


# Second common progression I IV V IV

if 1 == 2:
    # A break
    # t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    # t1.addNotes(intervs=['C4'], duration=1, volume=40)
    # t1.addNotes(intervs=['D4'], duration=1, volume=40)
    # t1.addChord(chord="IV", duration=1, volume=0, octave=4)

    t1.changeKey(newKey="C")
    for i in [1,2,3,4]:
        for aChord in ["I", "IV", "V", "IV"]:
            t1.addChord(aChord, duration=2, volume=80, octave=4, track=1)
            t1.addChord(aChord, duration=2, volume=80, octave=3, track=2)
        # t1.addChord(chord="I", duration=2, volume=80, octave=4)
        # t1.addChord(chord="IV", duration=2, volume=80, octave=4)
        # t1.addChord(chord="V", duration=2, volume=80, octave=4)
        # t1.addChord(chord="IV", duration=2, volume=80, octave=4)


# Jazz progressions - https://www.learnjazzstandards.com/blog/learning-jazz/jazz-theory/jazz-chord-progressions/
# 1. Major ii-V-I
# 2. Minor ii-V-i

# 3. Major I-vi-ii-V
# 4. Minor i-vi-ii-V


#Jazz progression ii-7 V7 Id7
if 1==2:
    # Used in https://www.youtube.com/watch?v=EwhosySVJO8
    # A break
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    t1.addNotes(intervs=['C4'], duration=1, volume=40)
    t1.addNotes(intervs=['D4'], duration=1, volume=40)
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    for aChord in ["ii-7", "V7", "Id7", "ii-7", "Id7", "ii-7", "V7"]:
            t1.addChord(aChord, duration=2, volume=80, octave=4)
    # t1.addChord(chord="ii-7", duration=2, volume=80, octave=4)
    # t1.addChord(chord="V7", duration=2, volume=80, octave=4)
    # t1.addChord(chord="Id7", duration=2, volume=80, octave=4)

if 1 == 2:
    # A break
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    t1.addNotes(intervs=['C4'], duration=1, volume=40)
    t1.addNotes(intervs=['D4'], duration=1, volume=40)
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    # Love songs and do-wop I vi IV V
    for i in [1, 2, 3, 4]:
        t1.addChord(chord="I", duration=2, volume=80, octave=4)
        t1.addChord(chord="vi", duration=2, volume=80, octave=4)
        t1.addChord(chord="IV", duration=2, volume=80, octave=4)
        t1.addChord(chord="V", duration=2, volume=80, octave=4)

if 1 == 2:
    # A break
    t1.addChord(chord="IV", duration=1, volume=0, octave=4)
    t1.addNotes(intervs=['C4'], duration=1, volume=40)
    t1.addNotes(intervs=['D4'], duration=1, volume=40)
    # Harmonic technique I bVII I
    for i in [1, 2, 3, 4]:
        t1.addChord(chord="I", duration=2, volume=80, octave=4)
        t1.addChord(chord="bVII", duration=2, volume=80, octave=4)
        t1.addChord(chord="I", duration=2, volume=80, octave=4)



# t1.addNotes(intervs=['C4', 'E4', 'G4'], duration=4, volume=100)
# t1.addNotes(intervs=['D3', 'F3', 'A3'], duration=2, volume=60)
# t1.addNotes(intervs=['C3', 'E3', 'F3'], duration=2, volume=70)
#
# t1.addChord(chord="I", duration=2, volume=80, octave=4)
#
# t1.addNotes(intervs=['C4', 'E4', 'G4'], duration=4, volume=100)
# t1.addNotes(intervs=['F3', 'A3', 'C4'], duration=2, volume=60)
# t1.addNotes(intervs=['C3', 'E3', 'G3'], duration=2, volume=70)
#
# t1.addChord(chord="I", duration=2, volume=80, octave=4)
#
# t1.addNotes(intervs=['C4', 'E4', 'G4'], duration=4, volume=100)
# t1.addNotes(intervs=['D3', 'F3', 'G3'], duration=2, volume=60)
# t1.addNotes(intervs=['C3', 'E3', 'G3'], duration=2, volume=70)
#
# t1.addChord(chord="I", duration=2, volume=80, octave=4)

print("Done")
t1.writeSong("/Users/davidsky/my_midi/test01.mid")
print("/Users/davidsky/my_midi/test01.mid")
exit(-123)

def inKey(nDF, keyS, typeS, interv=0, octave=4):
    """ Given a string for the key, and type of key, return the midi pitch"""
    # if interv=0 then return a random pitch from the key, otherwise return that note
    # Not quite ready for chords - http://www.piano-keyboard-guide.com/c-major-chord.html
    fullNoteName = f"{keyS}{octave}"
    basePitch = nDF[notesDF['note name'] == fullNoteName].pitch.iat[0]
    print(f"Pitch for {fullNoteName} is {basePitch}")
    if typeS == 'major':
        inc = -99
        inc = 0  if interv == 1 else inc
        inc = 2  if interv == 2 else inc
        inc = 4  if interv == 3 else inc
        inc = 5  if interv == 4 else inc
        inc = 7  if interv == 5 else inc
        inc = 9  if interv == 6 else inc
        inc = 11 if interv == 7 else inc
        inc = 12 if interv == 8 else inc
        return basePitch + inc
    else:
        return -888
    # 60 =           60 62 64 65 67 69 71 72
    #  x                +2 +2 +1 +2 +2 +2 +1
    #                  0 2  4  5  7  9 11 1

    #                  1  2  3  4  5  6  7  8

notesListCols = ['pitch', 'note name', 'note', 'octave']
notesList = [
    [21, 'A0', 'A', 0],
    [22, 'A#0', 'A#', 0],
    [22, 'Bb0', 'Bb', 0],
    [23, 'B0', 'B', 0],
    [24, 'C1', 'C', 1],
    [25, 'C#1', 'C#', 1],
    [25, 'Db1', 'Db', 1],
    [26, 'D1', 'D', 1],
    [27, 'D#1', 'D#', 1],
    [27, 'Eb1', 'Eb', 1],
    [28, 'E1', 'E', 1],
    [29, 'F1', 'F', 1],
    [30, 'F#1', 'F#', 1],
    [30, 'Gb1', 'Gb', 1],
    [31, 'G1', 'G', 1],
    [32, 'G#1', 'G#', 1],
    [32, 'Ab1', 'Ab', 1],
    [33, 'A1', 'A', 1],
    [34, 'A#1', 'A#', 1],
    [34, 'Bb1', 'Bb', 1],
    [35, 'B1', 'B', 1],
    [36, 'C2', 'C', 2],
    [37, 'Db2', 'Db', 2],
    [37, 'C#2', 'C#', 2],
    [38, 'D2', 'D', 2],
    [39, 'Eb2', 'Eb', 2],
    [39, 'D#2', 'D#', 2],
    [40, 'E2', 'E', 2],
    [41, 'F2', 'F', 2],
    [42, 'Gb2', 'Gb', 2],
    [42, 'F#2', 'F#', 2],
    [43, 'G2', 'G', 2],
    [44, 'Ab2', 'Ab', 2],
    [44, 'G#2', 'G#', 2],
    [45, 'A2', 'A', 2],
    [46, 'Bb2', 'Bb', 2],
    [46, 'A#2', 'A#', 2],
    [47, 'B2', 'B', 2],
    [48, 'C3', 'C', 3],
    [49, 'Db3', 'Db', 3],
    [49, 'C#3', 'C#', 3],
    [50, 'D3', 'D', 3],
    [51, 'Eb3', 'Eb', 3],
    [51, 'D#3', 'D#', 3],
    [52, 'E3', 'E', 3],
    [53, 'F3', 'F', 3],
    [54, 'Gb3', 'Gb', 3],
    [54, 'F#3', 'F#', 3],
    [55, 'G3', 'G', 3],
    [56, 'Ab3', 'Ab', 3],
    [56, 'G#3', 'G#', 3],
    [57, 'A3', 'A', 3],
    [58, 'Bb3', 'Bb', 3],
    [58, 'A#3', 'A#', 3],
    [59, 'B3', 'B', 3],
    [60, 'C4', 'C', 4],
    [60, 'middle C', 'middle C', 4],
    [61, 'Db4', 'Db', 4],
    [61, 'C#4', 'C#', 4],
    [62, 'D4', 'D', 4],
    [63, 'Eb4', 'Eb', 4],
    [63, 'D#4', 'D#', 4],
    [64, 'E4', 'E', 4],
    [65, 'F4', 'F', 4],
    [66, 'Gb4', 'Gb', 4],
    [66, 'F#4', 'F#', 4],
    [67, 'G4', 'G', 4],
    [68, 'Ab4', 'Ab', 4],
    [68, 'G#4', 'G#', 4],
    [69, 'A4', 'A', 4],
    [69, 'Concert pitch', 'A', 4],
    [70, 'Bb4', 'Bb', 4],
    [70, 'A#4', 'A#', 4],
    [71, 'B4', 'B', 4],
    [72, 'C5', 'C', 5],
    [73, 'Db5', 'Db', 5],
    [73, 'C#5', 'C#', 5],
    [74, 'D5', 'D', 5],
    [75, 'Eb5', 'Eb', 5],
    [75, 'D#5', 'D#', 5],
    [76, 'E5', 'E', 5],
    [77, 'F5', 'F', 5],
    [78, 'Gb5', 'Gb', 5],
    [78, 'F#5', 'F#', 5],
    [79, 'G5', 'G', 5],
    [80, 'Ab5', 'Ab', 5],
    [80, 'G#5', 'G#', 5],
    [81, 'A5', 'A', 5],
    [82, 'Bb5', 'Bb', 5],
    [82, 'A#5', 'A#', 5],
    [83, 'B5', 'B', 5],
    [84, 'C6', 'C', 6],
    [85, 'Db6', 'Db', 6],
    [85, 'C#6', 'C#', 6],
    [86, 'D6', 'D', 6],
    [87, 'Eb6', 'Eb', 6],
    [87, 'D#6', 'D#', 6],
    [88, 'E6', 'E', 6],
    [89, 'F6', 'F', 6],
    [90, 'Gb6', 'Gb', 6],
    [90, 'F#6', 'F#', 6],
    [91, 'G6', 'G', 6],
    [92, 'Ab6', 'Ab', 6],
    [92, 'G#6', 'G#', 6],
    [93, 'A6', 'A', 6],
    [94, 'Bb6', 'Bb', 6],
    [94, 'A#6', 'A#', 6],
    [95, 'B6', 'B', 6],
    [96, 'C7', 'C', 7],
    [97, 'Db7', 'Db', 7],
    [97, 'C#7', 'C#', 7],
    [98, 'D7', 'D', 7],
    [99, 'Eb7', 'Eb', 7],
    [99, 'D#7', 'D#', 7],
    [100, 'E7', 'E', 7],
    [101, 'F7', 'F', 7],
    [102, 'Gb7', 'Gb', 7],
    [102, 'F#7', 'F#', 7],
    [103, 'G7', 'G', 7],
    [104, 'Ab7', 'Ab', 7],
    [104, 'G#7', 'G#', 7],
    [105, 'A7', 'A', 7],
    [106, 'Bb7', 'Bb', 7],
    [106, 'A#7', 'A#', 7],
    [107, 'B7', 'B', 7],
    [108, 'C8', 'C', 8],
    [109, 'Db8', 'Db', 8],
    [109, 'C#8', 'C#', 8],
    [110, 'D8', 'D', 8],
    [111, 'Eb8', 'Eb', 8],
    [111, 'D#8', 'D#', 8],
    [112, 'E8', 'E', 8],
    [113, 'F8', 'F', 8],
    [114, 'Gb8', 'Gb', 8],
    [114, 'F#8', 'F#', 8],
    [115, 'G8', 'G', 8],
    [116, 'Ab8', 'Ab', 8],
    [116, 'G#8', 'G#', 8],
    [117, 'A8', 'A', 8],
    [118, 'Bb8', 'Bb', 8],
    [118, 'A#8', 'A#', 8],
    [119, 'B8', 'B', 8],
    [120, 'C9', 'C', 9],
    [121, 'Db9', 'Db', 9],
    [121, 'C#9', 'C#', 9],
    [122, 'D9', 'D', 9],
    [123, 'Eb9', 'Eb', 9],
    [123, 'D#9', 'D#', 9],
    [124, 'E9', 'E', 9],
    [125, 'F9', 'F', 9],
    [126, 'Gb9', 'Gb', 9],
    [126, 'F#9', 'F#', 9],
    [127, 'G9', 'G', 9],
    [128, 'Ab9', 'Ab', 9],
    [128, 'G#9', 'G#', 9]
]
notesDF = pd.DataFrame(notesList, columns=notesListCols)

# Scales - from https://en.wikipedia.org/wiki/Scale_(music)
# A major scale is a diatonic scale. The sequence of intervals between the notes of a major scale is:
#
# whole, whole, half, whole, whole, whole, half
# C major scale (C, D, E, F, G, A, B, C
# 60 =           60 62 64 65 67 69 71 72
#  x                +2 +2 +1 +2 +2 +2 +1

#                  0 2  4  5  7  9 11 1

#                  1  2  3  4  5  6  7  8

print(f"Midi pitch for middle C is: {notesDF[notesDF['note name'] == 'middle C'].pitch.iat[0]}")
print(f"Midi octave for middle C is: {notesDF[notesDF['note name'] == 'middle C'].octave.iat[0]}")
print(f"C5 is: pitch = {notesDF[notesDF['note name'] == 'C5'].pitch.iat[0]} and octave = {notesDF[notesDF['note name'] == 'C5'].octave.iat[0]}")
print(f"C4 is: pitch = {notesDF[notesDF['note name'] == 'C4'].pitch.iat[0]} and octave = {notesDF[notesDF['note name'] == 'C4'].octave.iat[0]}")
print(f"C3 is: pitch = {notesDF[notesDF['note name'] == 'C3'].pitch.iat[0]} and octave = {notesDF[notesDF['note name'] == 'C3'].octave.iat[0]}")


t1 = inKey(nDF=notesDF, keyS="C", typeS='major', interv=8, octave=4)
print(f"Key of C 8th note is {t1}")

print("Notes dataframe loaded")
# exit(-123)
# notesL2 = [
# {'pitch': 21, 'name': 'A0', 'note': 'A', 'octave': 0}
# {'pitch': 22, 'name': 'A#0', 'note': 'A#', 'octave': 0}
# {'pitch': 22, 'name': 'Bb0', 'note': 'Bb', 'octave': 0}
# {'pitch': 23, 'name': 'B0', 'note': 'B', 'octave': 0}
# {'pitch': 24, 'name': 'C1', 'note': 'C', 'octave': 1}
# {'pitch': 25, 'name': 'C#1', 'note': 'C#', 'octave': 1}
# {'pitch': 25, 'name': 'Db1', 'note': 'Db', 'octave': 1}
# {'pitch': 26, 'name': 'D1', 'note': 'D', 'octave': 1}
# {'pitch': 27, 'name': 'D#1', 'note': 'D#', 'octave': 1}
# {'pitch': 27, 'name': 'Eb1', 'note': 'Eb', 'octave': 1}
# {'pitch': 28, 'name': 'E1', 'note': 'E', 'octave': 1}
# {'pitch': 29, 'name': 'F1', 'note': 'F', 'octave': 1}
# {'pitch': 30, 'name': 'F#1', 'note': 'F#', 'octave': 1}
# {'pitch': 30, 'name': 'Gb1', 'note': 'Gb', 'octave': 1}
# {'pitch': 31, 'name': 'G1', 'note': 'G', 'octave': 1}
# {'pitch': 32, 'name': 'G#1', 'note': 'G#', 'octave': 1}
# {'pitch': 32, 'name': 'Ab1', 'note': 'Ab', 'octave': 1}
# {'pitch': 33, 'name': 'A1', 'note': 'A', 'octave': 1}
# {'pitch': 34, 'name': 'A#1', 'note': 'A#', 'octave': 1}
# {'pitch': 34, 'name': 'Bb1', 'note': 'Bb', 'octave': 1}
# {'pitch': 35, 'name': 'B1', 'note': 'B', 'octave': 1}
# {'pitch': 36, 'name': 'C2', 'note': 'C', 'octave': 2}
# {'pitch': 37, 'name': 'Db2', 'note': 'Db', 'octave': 2}
# {'pitch': 37, 'name': 'C#2', 'note': 'C#', 'octave': 2}
# {'pitch': 38, 'name': 'D2', 'note': 'D', 'octave': 2}
# {'pitch': 39, 'name': 'Eb2', 'note': 'Eb', 'octave': 2}
# {'pitch': 39, 'name': 'D#2', 'note': 'D#', 'octave': 2}
# {'pitch': 40, 'name': 'E2', 'note': 'E', 'octave': 2}
# {'pitch': 41, 'name': 'F2', 'note': 'F', 'octave': 2}
# {'pitch': 42, 'name': 'Gb2', 'note': 'Gb', 'octave': 2}
# {'pitch': 42, 'name': 'F#2', 'note': 'F#', 'octave': 2}
# {'pitch': 43, 'name': 'G2', 'note': 'G', 'octave': 2}
# {'pitch': 44, 'name': 'Ab2', 'note': 'Ab', 'octave': 2}
# {'pitch': 44, 'name': 'G#2', 'note': 'G#', 'octave': 2}
# {'pitch': 45, 'name': 'A2', 'note': 'A', 'octave': 2}
# {'pitch': 46, 'name': 'Bb2', 'note': 'Bb', 'octave': 2}
# {'pitch': 46, 'name': 'A#2', 'note': 'A#', 'octave': 2}
# {'pitch': 47, 'name': 'B2', 'note': 'B', 'octave': 2}
# {'pitch': 48, 'name': 'C3', 'note': 'C', 'octave': 3}
# {'pitch': 49, 'name': 'Db3', 'note': 'Db', 'octave': 3}
# {'pitch': 49, 'name': 'C#3', 'note': 'C#', 'octave': 3}
# {'pitch': 50, 'name': 'D3', 'note': 'D', 'octave': 3}
# {'pitch': 51, 'name': 'Eb3', 'note': 'Eb', 'octave': 3}
# {'pitch': 51, 'name': 'D#3', 'note': 'D#', 'octave': 3}
# {'pitch': 52, 'name': 'E3', 'note': 'E', 'octave': 3}
# {'pitch': 53, 'name': 'F3', 'note': 'F', 'octave': 3}
# {'pitch': 54, 'name': 'Gb3', 'note': 'Gb', 'octave': 3}
# {'pitch': 54, 'name': 'F#3', 'note': 'F#', 'octave': 3}
# {'pitch': 55, 'name': 'G3', 'note': 'G', 'octave': 3}
# {'pitch': 56, 'name': 'Ab3', 'note': 'Ab', 'octave': 3}
# {'pitch': 56, 'name': 'G#3', 'note': 'G#', 'octave': 3}
# {'pitch': 57, 'name': 'A3', 'note': 'A', 'octave': 3}
# {'pitch': 58, 'name': 'Bb3', 'note': 'Bb', 'octave': 3}
# {'pitch': 58, 'name': 'A#3', 'note': 'A#', 'octave': 3}
# {'pitch': 59, 'name': 'B3', 'note': 'B', 'octave': 3}
# {'pitch': 60, 'name': 'C4', 'note': 'C', 'octave': 4}
# {'pitch': 60, 'name': 'Middle C', 'note': 'Middle C', 'octave': 4}
# {'pitch': 61, 'name': 'Db4', 'note': 'Db', 'octave': 4}
# {'pitch': 61, 'name': 'C#4', 'note': 'C#', 'octave': 4}
# {'pitch': 62, 'name': 'D4', 'note': 'D', 'octave': 4}
# {'pitch': 63, 'name': 'Eb4', 'note': 'Eb', 'octave': 4}
# {'pitch': 63, 'name': 'D#4', 'note': 'D#', 'octave': 4}
# {'pitch': 64, 'name': 'E4', 'note': 'E', 'octave': 4}
# {'pitch': 65, 'name': 'F4', 'note': 'F', 'octave': 4}
# {'pitch': 66, 'name': 'Gb4', 'note': 'Gb', 'octave': 4}
# {'pitch': 66, 'name': 'F#4', 'note': 'F#', 'octave': 4}
# {'pitch': 67, 'name': 'G4', 'note': 'G', 'octave': 4}
# {'pitch': 68, 'name': 'Ab4', 'note': 'Ab', 'octave': 4}
# {'pitch': 68, 'name': 'G#4', 'note': 'G#', 'octave': 4}
# {'pitch': 69, 'name': 'A4', 'note': 'A', 'octave': 4}
# {'pitch': 69, 'name': 'Concert pitch', 'note': 'A', 'octave': 4}
# {'pitch': 70, 'name': 'Bb4', 'note': 'Bb', 'octave': 4}
# {'pitch': 70, 'name': 'A#4', 'note': 'A#', 'octave': 4}
# {'pitch': 71, 'name': 'B4', 'note': 'B', 'octave': 4}
# {'pitch': 72, 'name': 'C5', 'note': 'C', 'octave': 5}
# {'pitch': 73, 'name': 'Db5', 'note': 'Db', 'octave': 5}
# {'pitch': 73, 'name': 'C#5', 'note': 'C#', 'octave': 5}
# {'pitch': 74, 'name': 'D5', 'note': 'D', 'octave': 5}
# {'pitch': 75, 'name': 'Eb5', 'note': 'Eb', 'octave': 5}
# {'pitch': 75, 'name': 'D#5', 'note': 'D#', 'octave': 5}
# {'pitch': 76, 'name': 'E5', 'note': 'E', 'octave': 5}
# {'pitch': 77, 'name': 'F5', 'note': 'F', 'octave': 5}
# {'pitch': 78, 'name': 'Gb5', 'note': 'Gb', 'octave': 5}
# {'pitch': 78, 'name': 'F#5', 'note': 'F#', 'octave': 5}
# {'pitch': 79, 'name': 'G5', 'note': 'G', 'octave': 5}
# {'pitch': 80, 'name': 'Ab5', 'note': 'Ab', 'octave': 5}
# {'pitch': 80, 'name': 'G#5', 'note': 'G#', 'octave': 5}
# {'pitch': 81, 'name': 'A5', 'note': 'A', 'octave': 5}
# {'pitch': 82, 'name': 'Bb5', 'note': 'Bb', 'octave': 5}
# {'pitch': 82, 'name': 'A#5', 'note': 'A#', 'octave': 5}
# {'pitch': 83, 'name': 'B5', 'note': 'B', 'octave': 5}
# {'pitch': 84, 'name': 'C6', 'note': 'C', 'octave': 6}
# {'pitch': 85, 'name': 'Db6', 'note': 'Db', 'octave': 6}
# {'pitch': 85, 'name': 'C#6', 'note': 'C#', 'octave': 6}
# {'pitch': 86, 'name': 'D6', 'note': 'D', 'octave': 6}
# {'pitch': 87, 'name': 'Eb6', 'note': 'Eb', 'octave': 6}
# {'pitch': 87, 'name': 'D#6', 'note': 'D#', 'octave': 6}
# {'pitch': 88, 'name': 'E6', 'note': 'E', 'octave': 6}
# {'pitch': 89, 'name': 'F6', 'note': 'F', 'octave': 6}
# {'pitch': 90, 'name': 'Gb6', 'note': 'Gb', 'octave': 6}
# {'pitch': 90, 'name': 'F#6', 'note': 'F#', 'octave': 6}
# {'pitch': 91, 'name': 'G6', 'note': 'G', 'octave': 6}
# {'pitch': 92, 'name': 'Ab6', 'note': 'Ab', 'octave': 6}
# {'pitch': 92, 'name': 'G#6', 'note': 'G#', 'octave': 6}
# {'pitch': 93, 'name': 'A6', 'note': 'A', 'octave': 6}
# {'pitch': 94, 'name': 'Bb6', 'note': 'Bb', 'octave': 6}
# {'pitch': 94, 'name': 'A#6', 'note': 'A#', 'octave': 6}
# {'pitch': 95, 'name': 'B6', 'note': 'B', 'octave': 6}
# {'pitch': 96, 'name': 'C7', 'note': 'C', 'octave': 7}
# {'pitch': 97, 'name': 'Db7', 'note': 'Db', 'octave': 7}
# {'pitch': 97, 'name': 'C#7', 'note': 'C#', 'octave': 7}
# {'pitch': 98, 'name': 'D7', 'note': 'D', 'octave': 7}
# {'pitch': 99, 'name': 'Eb7', 'note': 'Eb', 'octave': 7}
# {'pitch': 99, 'name': 'D#7', 'note': 'D#', 'octave': 7}
# {'pitch': 100, 'name': 'E7', 'note': 'E', 'octave': 7}
# {'pitch': 101, 'name': 'F7', 'note': 'F', 'octave': 7}
# {'pitch': 102, 'name': 'Gb7', 'note': 'Gb', 'octave': 7}
# {'pitch': 102, 'name': 'F#7', 'note': 'F#', 'octave': 7}
# {'pitch': 103, 'name': 'G7', 'note': 'G', 'octave': 7}
# {'pitch': 104, 'name': 'Ab7', 'note': 'Ab', 'octave': 7}
# {'pitch': 104, 'name': 'G#7', 'note': 'G#', 'octave': 7},
# {'pitch': 105, 'name': 'A7', 'note': 'A', 'octave': 7},
# {'pitch': 106, 'name': 'Bb7', 'note': 'Bb', 'octave': 7},
# {'pitch': 106, 'name': 'A#7', 'note': 'A#', 'octave': 7},
# {'pitch': 107, 'name': 'B7', 'note': 'B', 'octave': 7},
# {'pitch': 108, 'name': 'C8', 'note': 'C', 'octave': 8},
# {'pitch': 109, 'name': 'Db8', 'note': 'Db', 'octave': 8},
# {'pitch': 109, 'name': 'C#8', 'note': 'C#', 'octave': 8},
# {'pitch': 110, 'name': 'D8', 'note': 'D', 'octave': 8},
# {'pitch': 111, 'name': 'Eb8', 'note': 'Eb', 'octave': 8},
# {'pitch': 111, 'name': 'D#8', 'note': 'D#', 'octave': 8},
# {'pitch': 112, 'name': 'E8', 'note': 'E', 'octave': 8},
# {'pitch': 113, 'name': 'F8', 'note': 'F', 'octave': 8},
# {'pitch': 114, 'name': 'Gb8', 'note': 'Gb', 'octave': 8},
# {'pitch': 114, 'name': 'F#8', 'note': 'F#', 'octave': 8},
# {'pitch': 115, 'name': 'G8', 'note': 'G', 'octave': 8},
# {'pitch': 116, 'name': 'Ab8', 'note': 'Ab', 'octave': 8},
# {'pitch': 116, 'name': 'G#8', 'note': 'G#', 'octave': 8},
# {'pitch': 117, 'name': 'A8', 'note': 'A', 'octave': 8},
# {'pitch': 118, 'name': 'Bb8', 'note': 'Bb', 'octave': 8},
# {'pitch': 118, 'name': 'A#8', 'note': 'A#', 'octave': 8},
# {'pitch': 119, 'name': 'B8', 'note': 'B', 'octave': 8},
# {'pitch': 120, 'name': 'C9', 'note': 'C', 'octave': 9},
# {'pitch': 121, 'name': 'Db9', 'note': 'Db', 'octave': 9},
# {'pitch': 121, 'name': 'C#9', 'note': 'C#', 'octave': 9},
# {'pitch': 122, 'name': 'D9', 'note': 'D', 'octave': 9},
# {'pitch': 123, 'name': 'Eb9', 'note': 'Eb', 'octave': 9},
# {'pitch': 123, 'name': 'D#9', 'note': 'D#', 'octave': 9},
# {'pitch': 124, 'name': 'E9', 'note': 'E', 'octave': 9},
# {'pitch': 125, 'name': 'F9', 'note': 'F', 'octave': 9},
# {'pitch': 126, 'name': 'Gb9', 'note': 'Gb', 'octave': 9},
# {'pitch': 126, 'name': 'F#9', 'note': 'F#', 'octave': 9},
# {'pitch': 127, 'name': 'G9', 'note': 'G', 'octave': 9},
# {'pitch': 128, 'name': 'Ab9', 'note': 'Ab', 'octave': 9},
# {'pitch': 128, 'name': 'G#9', 'note': 'G#', 'octave': 9},
# ]

degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
degreeD = [72, 71, 69, 67, 65, 64, 62, 60 ]
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 50  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(3) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)
MyMIDI.addNote(1, channel, inKey(nDF=notesDF, keyS="C", typeS='major', interv=1, octave=4), time, duration-0.2, volume)
MyMIDI.addNote(1, channel, inKey(nDF=notesDF, keyS="C", typeS='major', interv=3, octave=4), time+1, duration-0.2, volume)
MyMIDI.addNote(1, channel, inKey(nDF=notesDF, keyS="C", typeS='major', interv=5, octave=4), time+2, duration-0.2, volume)
MyMIDI.addNote(1, channel, inKey(nDF=notesDF, keyS="C", typeS='major', interv=3, octave=4), time+3, duration-0.2, volume)

MyMIDI.addNote(1, channel,   inKey(nDF=notesDF, keyS="C", typeS='major', interv=1, octave=4), time+4, duration-0.4, volume)
MyMIDI.addNote(1, channel+1, inKey(nDF=notesDF, keyS="C", typeS='major', interv=3, octave=4), time+4, duration-0.4, volume)
MyMIDI.addNote(1, channel+2, inKey(nDF=notesDF, keyS="C", typeS='major', interv=5, octave=4), time+4, duration-0.4, volume)

MyMIDI.addNote(1, channel,   inKey(nDF=notesDF, keyS="C", typeS='major', interv=1, octave=3), time+5, duration-0.4, volume)
MyMIDI.addNote(1, channel+1, inKey(nDF=notesDF, keyS="C", typeS='major', interv=3, octave=3), time+5, duration-0.4, volume)
MyMIDI.addNote(1, channel+2, inKey(nDF=notesDF, keyS="C", typeS='major', interv=5, octave=3), time+5, duration-0.4, volume)

MyMIDI.addNote(1, channel,   inKey(nDF=notesDF, keyS="C", typeS='major', interv=1, octave=4), time+6, duration-0.4, volume)
MyMIDI.addNote(1, channel+1, inKey(nDF=notesDF, keyS="C", typeS='major', interv=3, octave=4), time+6, duration-0.4, volume)
MyMIDI.addNote(1, channel+2, inKey(nDF=notesDF, keyS="C", typeS='major', interv=5, octave=5), time+6, duration-0.4, volume)

MyMIDI.addNote(1, channel,   inKey(nDF=notesDF, keyS="C", typeS='major', interv=1, octave=3), time+6, duration-0.4, volume)
MyMIDI.addNote(1, channel+1, inKey(nDF=notesDF, keyS="C", typeS='major', interv=3, octave=3), time+6, duration-0.4, volume)
MyMIDI.addNote(1, channel+2, inKey(nDF=notesDF, keyS="C", typeS='major', interv=5, octave=3), time+6, duration-0.4, volume)

# for pitch in degrees:
#     MyMIDI.addNote(track, channel, pitch, time, duration, volume)
#     MyMIDI.addNote(track, channel, pitch, time, duration, volume)
#
#
#     MyMIDI.addNote(2, channel, pitch-12, time, duration-0.5, volume)
#
#     time = time + 1

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

print("Done!")
