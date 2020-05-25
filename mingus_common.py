import mingus.core.notes as notes
import mingus.core.intervals as intervals # core.diatonic as diatonic
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.progressions as progressions
from mingus.midi import  fluidsynth
def is_valid():
    print(notes.is_valid_note("C"))
    print(notes.is_valid_note("C#"))
    print(notes.is_valid_note("Cb"))
def note_to_int():
    print(notes.note_to_int("C"))
    print(notes.note_to_int("C#"))
    print(notes.note_to_int("D"))
    print(notes.note_to_int("B"))
    #notes.int_to_note(0) -- this gives "C"
def augment_diminish():
    print(notes.augment("C"))
    print(notes.diminish("C#"))
    print(notes.diminish("Cb"))

def to_major_to_minor(): #not working
    print(notes.to_minor("C"))
    print(notes.to_major("C"))

def tut_intervals():
    print(intervals.second("C", "C"))
    print(intervals.second("E", "D"))
    print(intervals.minor_second("C"))

def tut_chords():
    print (chords.triad("E", "C"))
    print(chords.major_triad("C"))
    print(chords.minor_triad("C"))
    print(chords.minor_triad("D"))
    print(chords.determine(["C", "E", "G"]))
    print(chords.determine(["C", "E", "G", "B"], True))
def tut_scales(): #Not working
    #print (scales.("C"))
    return None
def tut_progressions():
    a = progressions.to_chords(["I", "bIV", "VIIdim7"])
    print (a)
def tut_fluidsynth():
    fluidsynth.init("soundfont.SF2")
#is_valid()
#note_to_int()
#augment_diminish()
#to_major_to_minor()

#tut_intervals()
#tut_chords()
#tut_scales() #not working
#tut_progressions()
tut_fluidsynth()