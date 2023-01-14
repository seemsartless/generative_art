#
# oneSong.py - a Python object used to create a song
#
import pandas as pd
from midiutil import MIDIFile

class oneSong:
    def __init__(self, key, tempo, tracks):
        self.key = key
        print(f"Creating a song in the key of {self.key}")

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
        self.notesDF = pd.DataFrame(notesList, columns=notesListCols)

        # THe actual midi file object
        self.t = MIDIFile(3)
        self.t.addTempo(tracks, 0, tempo)
        self.time=0
        self.channel = 0
        # duration = 1  # In beats
        # volume = 100
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=1, octave=4), self.time, duration, volume)
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=3, octave=4), self.time, duration, volume)
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=5, octave=4), self.time, duration, volume)
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=8, octave=4), self.time, duration, volume)
        #
        # self.time = self.time + 1
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=2, octave=4), self.time, duration, volume)
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=4, octave=4), self.time, duration, volume)
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=6, octave=4), self.time, duration, volume)
        # self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS="C", typeS='major', interv=1, octave=5), self.time, duration, volume)



    def inKey(self, nDF, keyS, typeS, interv=0, octave=4):
        """ Given a string for the key, and type of key, return the midi pitch"""
        # if interv=0 then return a random pitch from the key, otherwise return that note
        # Not quite ready for chords - http://www.piano-keyboard-guide.com/c-major-chord.html
        fullNoteName = f"{keyS}{octave}"
        basePitch = nDF[nDF['note name'] == fullNoteName].pitch.iat[0]
        # print(f"Pitch for {fullNoteName} is {basePitch}")
        if typeS == 'major':
            inc = -99
            inc = 0 if interv == 1 else inc
            inc = 2 if interv == 2 else inc
            inc = 4 if interv == 3 else inc
            inc = 5 if interv == 4 else inc
            inc = 7 if interv == 5 else inc
            inc = 9 if interv == 6 else inc
            inc = 11 if interv == 7 else inc
            inc = 12 if interv == 8 else inc
            return basePitch + inc
        else:
            return -888

    def addNotes(self, intervs, duration, volume):
        for notes in intervs:
            self.t.addNote(1, self.channel, self.notesDF[self.notesDF['note name'] == notes].pitch.iat[0], self.time, duration=duration, volume=volume)
        self.time = self.time + duration

    def addChord(self, chord, octave, duration, volume):
        # Manual to start with
        if chord=="I":
            # Major chord of the given key
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=1, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=3, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=5, octave=octave), self.time, duration, volume)
        elif chord=="vi":  # A minor say, in key of C - A C E 9 1 4
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=6, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=1, octave=octave+1), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=3, octave=octave+1), self.time, duration, volume)
        elif chord=="IV":  # F major say, in key of C - F A C
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=4, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=6, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=1, octave=octave+1), self.time, duration, volume)
        elif chord=="V":  # G major say, in key of C - G B D
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=5, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=7, octave=octave), self.time, duration, volume)
            self.t.addNote(1, self.channel, self.inKey(nDF=self.notesDF, keyS=self.key, typeS='major', interv=2, octave=octave+1), self.time, duration, volume)


        self.time = self.time + duration

    def changeKey(self, newKey):
        self.key = newKey
    def midiPitch(self, noteName):
        return(self.notesDF[self.notesDF['note name'] == noteName].pitch.iat[0])

    def writeSong(self, fullFileName):
        with open(fullFileName, "wb") as output_file:
            self.t.writeFile(output_file)