POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note():
    def __init__(self, position, perspective = None):
        if isinstance(position, str):
            self.position = POSITIONS[position]
        if perspective is not None:
            self.perspective = perspective
        if isinstance(position, int):
            self.position = position % 12
        elif perspective is None and len(position) > 1:
            self.perspective == position[1]   
        else:
            self.perspective = perspective        
            
    def __invert__(self):
        """The expression ~note evaluates to a new Note object with the same 
        position but the opposite perspective.
        
        Side effects:
            changes the value of self.perspective
        """
        if self.perspective == "b":
            return Note(self.position, "#")
        elif self.perspective == "#":
            return Note(self.position, "b")
        else:
            return Note(self.position, None)
        
    def __add__(self, num):
        return Note((self.position + num) % 12, perspective = self.perspective)
    
    def __sub__(self, num):
        return Note((self.position - num) % 12, perspective = self.perspective)
    
    def __rshift__(self, other):
        return (self.position - other.position) % 12
    
    def __lshift__(self, other):
        return (other.position - self.position) % 12
    
    def __repr__(self):
        return f'Note({self.position},{self.perspective})'
    
    def __str__(self):
        if self.perspective == "#" and PITCHES[self.position] > 1:
            return PITCHES[self.position][0]
        elif self.perspective == "b":
            return PITCHES[self.position][1]
        elif len(PITCHES[self.position]) == 2 and self.perspective == None:
            return f'{PITCHES[self.position][0]} / {PITCHES[self.position][1]}'
        elif self.position == 0:
            return PITCHES[0]
        else:
            return PITCHES[self.position]
